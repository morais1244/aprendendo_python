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

class ElectricCar(Car): #precisamos adotar esse modelo quando queremos tratar uma herança e uma classe-filha
    def __init__(self,model,make,year):
        super().__init__(make,model,year) #Super serve parar criar uma ligação entre a classe-pai e classe-filho, vem de superclasse e subclasse
        self.battery_size = 70
    def describe_battery_size(self):
        print("A capacidade da bateria é de "+
              str(self.battery_size)+"-KWh")
my_tesla = ElectricCar('tesla', 'model s', 2016) 
my_tesla.describe_car()
my_tesla.describe_battery_size()
#podemos simplesmente adicionar métodos e atributos para nossa classe nova conforme for conveniente
#também podemos sobrescrever metodos que não forem convientes para a classe-filha
"""como por exemplo, suponhamos que tenha um fill_gas_tank() na classe car
e então na classe electriccar basta escrevermos fill_gas_tank(): print("Um c
   um carro eletrico não precisa disso!")"""
"""Podemos também criar uma classe de outra classe caso estejamos muito espe
cificos e extensos em alguma lista"""
class Battery():
    def __init__(self,battery_size):
        self.battery_size = 70
    def describe_battery_size(self):
        print("A capacidade da bateria é de "+
              str(self.battery_size)+"-KWh")
    class ElectricCar(Car):
        def __init__(self,model,make,year):
            super().__init__(model, make, year)
            self.battery = Battery()
            
my_tesla.battery.describe_battery_size()