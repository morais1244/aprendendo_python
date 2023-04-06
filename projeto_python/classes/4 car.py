class Car():
    def __init__(self, model, make, year):
        self.model = model
        self.make = make
        self.year = year
        self.odometro_reading = 0
    def describe_car(self):
        print(str(self.year),self.make,self.model)
    def read_odometro(self):
        print('this car has '+str(self.odometro_reading)+' miles on it.')

new_car = Car('A4', 'Audi', 2016)
new_car.describe_car()
new_car.read_odometro()
#o metodo mais simples para alterar um valor é mudar diretamente ou 
#seja colocar new_car.odometro_reading = 23 por exemplo.
new_car.odometro_reading = 23
new_car.read_odometro()
#Outro metodo seria adicionar um metodo especifico para isso, ou seja:
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
new_car = Car('A4', 'Audi', 2016)
new_car.att_odometro(50)
new_car.read_odometro()
new_car.att_odometro(12)
#também podemos incrementar um valor ao inves de definir um novo = 
new_car.increment_odometro(10)
new_car.read_odometro()
new_car.increment_odometro(-1)
