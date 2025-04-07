import hashlib
from random import random, randint
from brta import BRTA
from vehicles import Bike, Car, Cng, Vehicle
from ride_manager import uber

class UserAlreadyExistst(Exception):
    def __init__(self, email, *args):
        print(f'User: {email} already exists')
        super().__init__(*args)

license_authority = BRTA()

class User:
    def __init__(self, name, email, password):
        self.name = name
        self.email = email
        pwd_encrypted = hashlib.md5(password.encode()).hexdigest()
        already_exists = False
        with open('users.txt', 'r') as file:
            if email in file.read():
                already_exists = True
                UserAlreadyExistst(email)
        file.close()
        if already_exists == False:         
            with open('users.txt', 'a') as file:
                file.write(f'{email} {pwd_encrypted}\n')
            file.close()
            print(self.name, 'user created')
        
    @staticmethod
    def log_in(email, password):
        stored_password = ''
        with open('users.txt', 'r') as file:
            lines = file.readlines()
            for line in lines:
                if email in line:
                    stored_password = line.split(' ')[1]
        file.close()
        
        hashed_password = hashlib.md5(password.encode()).hexdigest()
        if stored_password == hashed_password:
            print('Valid User')
            # print('Password Found', stored_password)
        else:
            print('Invalid User')   

class Rider(User):
    def __init__(self, name, email, password, location, balance):
        super().__init__(name, email, password)
        self.location = location
        self.balance = balance
    
    # updated location
    def set_location(self, location):
        self.location = location
    
    def get_location(self):
        return self.location
    
    def request_trip(self, destination):
        pass
    
    def start_a_trip(self, fare):
        self.balance -= fare

class Driver(User):
    def __init__(self, name, email, password, location, license):
        super().__init__(name, email, password)
        self.location = location
        self.license = license
        self.valid_driver = license_authority.validate_license(email, license)
        self.earning = 0
    
    def take_driving_test(self):
        result = license_authority.take_driving_test(self.email)
        if result == False:
            self.valid_driver = False
            print('Sorry you Failed, try again..')
        else:
            self.license = result
            self.valid_driver = True
    
    def register_a_vehicle(self, vehicle_type, license_plate, rate):
        if self.valid_driver is True:
            if vehicle_type == 'car':
                new_vehicle = Car(vehicle_type, license_plate, rate, self)
                uber.add_a_vehicle(vehicle_type, new_vehicle)
            elif vehicle_type == 'bike':
                new_vehicle = Bike(vehicle_type, license_plate, rate, self)
                uber.add_a_vehicle(vehicle_type, new_vehicle)
            else:
                new_vehicle = Cng(vehicle_type, license_plate, rate, self)
                uber.add_a_vehicle(vehicle_type, new_vehicle)
        else:
            print('You are not a valid user')
    
    def start_a_trip(self, destination, fare):
        self.location = destination
        self.earning += fare
                    

rider_1 = Rider('rider1', 'rider1@gmail.com', 'rider1', randint(1, 30), 5000)
rider_2 = Rider('rider2', 'rider2@gmail.com', 'rider1', randint(1, 30), 5000)
rider_3 = Rider('rider3', 'rider3@gmail.com', 'rider1', randint(1, 30), 5000)

driver_1 = Driver('driver1', 'driver1@gmail.com', 'driver1', randint(1, 30), 5645)
driver_1.take_driving_test()
driver_1.register_a_vehicle('car', 1245, 10)

driver_2 = Driver('driver2', 'driver2@gmail.com', 'driver2', randint(1, 30), 5645)
driver_2.take_driving_test()
driver_2.register_a_vehicle('car', 1245, 10)

driver_3 = Driver('driver3', 'driver3@gmail.com', 'driver3', randint(1, 30), 5645)
driver_3.take_driving_test()
driver_3.register_a_vehicle('car', 2145, 10)

driver_4 = Driver('driver4', 'driver4@gmail.com', 'driver4', randint(1, 30), 5645)
driver_4.take_driving_test()
driver_4.register_a_vehicle('car', 3245, 10)

print(uber.get_available_cars())
uber.find_a_vehicle(rider_1, 'car', 90)