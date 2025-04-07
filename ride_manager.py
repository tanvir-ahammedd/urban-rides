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
    
    def get_available_cars(self):
        return self.__available_cars
    
    def find_a_vehicle(self, rider, vehicle_type, destination):
        if vehicle_type == 'car':
            if len(self.__available_cars) == 0:
                print('Sorry, no car is available')
                return False
            else:
                for car in self.__available_cars:
                    # print('Potential: ', rider.location, car.driver.location)
                    if abs(rider.location - car.driver.location < 10):
                        distance = abs(rider.location - destination)
                        fare = distance * car.rate
                        if fare > rider.balance:
                            print("You don't have enough money", fare, rider.balance)
                            return False
                        if car.status == 'available':
                            car.status = 'unavailable'
                            self.__available_cars.remove(car)
                            rider.start_a_trip(fare) 
                            print('Find a match for', fare)
                            return True
        
uber = Ridemanager()