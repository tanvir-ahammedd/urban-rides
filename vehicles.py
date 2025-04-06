from abc import ABC, abstractmethod

class Vehicle(ABC):
    speed = {
        'car': 30,
        'bike': 50,
        'cng': 20
    }
    def __init__(self, vehicle_type, license_plate, rate, driver):
        self.vehicle_type = vehicle_type
        self.rate = rate
        self.driver = driver
        self.status = 'available'
        self.license_plate = license_plate
        self.speed = self.speed[vehicle_type]
    
    @abstractmethod
    def start_driving(self):
        pass
    
    @abstractmethod
    def trip_finished(self):
        pass
    
class Car(Vehicle):
    def __init__(self, vehicle_type, license_plate, rate, driver):
        super().__init__(vehicle_type, license_plate, rate, driver)
        
    def start_driving(self):
        self.status = 'navailable'
        print(self.vehicle_type, self.license_plate, 'Started')
        return super().start_driving()
    
    def trip_finished(self):
        self.status = 'available'
        print(self.vehicle_type, self.license_plate, 'Completed trip')
        
class Bike(Vehicle):
    def __init__(self, vehicle_type, license_plate, rate, driver):
        super().__init__(vehicle_type, license_plate, rate, driver)
        
    def start_driving(self):
        self.status = 'navailable'
        print(self.vehicle_type, self.license_plate, 'Started')
        return super().start_driving()
    
    def trip_finished(self):
        self.status = 'available'
        print(self.vehicle_type, self.license_plate, 'Completed trip')
        
class Cng(Vehicle):
    def __init__(self, vehicle_type, license_plate, rate, driver):
        super().__init__(vehicle_type, license_plate, rate, driver)
        
    def start_driving(self):
        self.status = 'navailable'
        print(self.vehicle_type, self.license_plate, 'Started')
        return super().start_driving()
    
    def trip_finished(self):
        self.status = 'available'
        print(self.vehicle_type, self.license_plate, 'Completed trip')
        
