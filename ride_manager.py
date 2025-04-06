class Ridemanager:
    def __init__(self):
        print('Ride Manager Activated')
        self.__available_cars = []
        self.__available_bikes = []
        self.__available_cng = []
        
    def add_a_vehicle(self,vehicle_type, vehicle):
         self.__available_cars.append(vehicle)
         self.__available_bikes.append(vehicle)
         self.__available_cng.append(vehicle)
        
uber = Ridemanager()