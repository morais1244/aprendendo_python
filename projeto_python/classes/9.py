class Car():
    def __init__(self, model, make, year):
        self.model = model
        self.make = make
        self.year = year
        self.odometro_reading = 0
    def att_odometro(self, number):
        if number >= self.odometro_reading:    
            self.odometro_reading = number
        else:
            print("you cant roll back an odometro")
    def increment_odometro(self, miles):
        if miles > 0:
            self.odometro_reading += miles
        else:
            print("The car cant roll back")
    def describe_car(self):
        print(str(self.year),self.make,self.model)
    def read_odometro(self):
        print('this car has '+str(self.odometro_reading)+' miles on it.')

class Battery():
    def __init__(self, battery_size=70):
        self.battery_size = battery_size
    def describe_battery_size(self):
        print("A capacidade da bateria é de "+
              str(self.battery_size)+"-KWh")
    def get_range(self):
        if self.battery_size == 70:
            range = 240
        elif self.battery_size == 85:
            range = 270
        message = "This car can go approximately " + str(range) 
        message += " miles on a full charge."
        print(message)
class ElectricCar(Car):
    def __init__(self, model, make, year):
        super().__init__(model, make, year)
        self.battery = Battery() 
        
my_tesla = ElectricCar('tesla', 'model s', 2016) 
my_tesla.describe_car()
my_tesla.battery.describe_battery_size()
my_tesla.battery.get_range()