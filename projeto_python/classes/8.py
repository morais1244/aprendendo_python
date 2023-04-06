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
class ElectricCar(Car):
    def __init__(self, model, make, year):
        super().__init__(model, make, year)
        self.battery = Battery() #utiliza battery como definido na classe anterior

my_tesla = ElectricCar('model s', 'tesla' , 2016)
my_tesla.battery.describe_battery_size() #precisa usar o .battery, já que é vindo desta classe!