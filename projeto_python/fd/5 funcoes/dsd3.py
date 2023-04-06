#exercicios 
#8.9
magicians = ['carlos', 'pablo' , 'mister m' , 'joao']
def show_magicians(lista):
    for magician in lista:
        print(magician.title())
show_magicians(magicians)

#8.10   
print('\n')
completed_magicians = []
def make_great_magicians(magicians, completed_magicians):
    while magicians:
        current_magicians = "O grande " + magicians.pop()
        completed_magicians.append(current_magicians)
def great_magicians(lista):
    for magician in lista:
        print(magician.title())
make_great_magicians(magicians, completed_magicians)
great_magicians(completed_magicians)

print("\n")
#podemos fazer uma função que aceite um número arbitrário de argumentos, basta usarmos * 
def make_pizza(*toppings):
    for topping in toppings:
        print("-"+topping)
make_pizza('pepperoni','cream cheese' , 'mushrooms')

#temos sempre que colocar a parte que aceita mais parâmetros pra mais a direita
#def make_pizza(size,*toppings):

#podemos armazenar valores nomeados que não sabemos ainda:

def make_profile(first,last,**user_info): #os ** servem para criar um dicionário imaginário com este nome
    profile={}
    profile["first_name"] = first
    profile['last_name'] = last
    for key,value in user_info.items():
        profile[key] = value
    return profile
user_infos = make_profile('albert' , 'einsten' , location = 'pricenton')
print(user_infos)

#exercicios
#8.12
def sanduiches(*ingredientes):
    print("\nO sanduiche terá os seguintes ingredientes:")
    for ingrediente in ingredientes:
        print("-"+ingrediente)
sanduiches('queijo','presunto','manteiga')

#8.14
def make_car(manufacturer, model , **car_type):
    car={}
    car['manufacturer'] = manufacturer
    car['model'] = model
    for key, value in car_type.items():
        car[key] = value
    return car

car = make_car('outback' , 'subaru' , color = 'blue' , tow_package = True)
print(car)




import pizza
from pizza import make_pizza
from pizza import make_pizza as mp
import pizza as p
p.make_pizza()
from pizza import * #importar tudo!
