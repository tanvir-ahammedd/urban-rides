import hashlib
from brta import BRTA


license_authority = BRTA()

class User:
    def __init__(self, name, email, password):
        self.name = name
        self.email = email
        pwd_encrypted = hashlib.md5(password.encode()).hexdigest()
        with open('users.txt', 'w') as file:
            file.write(f'{email} {pwd_encrypted}')
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
            print('Sorry you Failed, try again..')
        else:
            self.license = result
            self.valid_driver = True
    
    def start_a_trip(self, destination, fare):
        self.location = destination
        self.earning += fare
                    

tanvir = User('Tanvir Ahammed', 'tanvir@gmail.com', 'manisman')
tanvir.log_in('tanvir@gmail.com', 'manisman')

omor = Driver('Omor Faruk', 'omor@gmail.com', 'omorisomor', 'Chandpur', '9078')
print(omor.license)
result = license_authority.validate_license(omor.email, omor.license)
print(result)
omor.take_driving_test()
result = license_authority.validate_license(omor.email, omor.license)
print(result)