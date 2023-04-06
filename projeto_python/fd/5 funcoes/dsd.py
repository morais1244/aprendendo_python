#Função serve para guardar um laço ou trecho de código numa variável usando def de definition e ()
def greet_user():
    print("\nhello world!")
greet_user()

#podemos armazenar uma variável numa função para especificá-la depois
def greet_user(username):
    print("\nhello "+ username.title()+"!")
greet_user('jesse')
#se chama parametro, uma informação que a função precisa pra executar e argumento

#exercicio
#8.1
def message():
    print("\nNeste capítulo do livro estou aprendendo sobre funções!")
message()
#8.2
def book(name):
    print("\nMeu livro favorito é "+name.title()+"!")
book('musashi')

#argumento posicional, leva em consideração a posição com qual é colocado o parametro e o argumento e usa isso para definir qual é qual

def animal(animal_type, animal_name):
    print("\nMeu "+animal_type.title()+
     " se chama "+ animal_name.title())
animal('cachorro','carlos')

#argumento nomeado, é um par de nome-valor usado para parametro e argumento
def animal(animal_type, animal_name):
    print("\nMeu "+animal_type.title()+
     " se chama "+ animal_name.title())
animal(animal_type = 'cachorro',animal_name = 'carlos')

#valores default servem para facilitar o código e anexar de cara um valor para aquele parametro
def animal(animal_name, animal_type='dog'):#se atentar a colocar o parametro com default depois dos que não tem default sempre!
    print("\nMeu",animal_type.title(),"se chama"
    ,animal_name.title())
animal('joao')
animal(animal_name='pablo',animal_type='peixe')
animal('pablo','peixe')

#exercicio
#8.4
def make_shirt(size,phrase):
    print('\nO tamanho da camiseta é',size.title(),"e a frase estampada é", phrase)
make_shirt('M','no pain no gain')

#8.5
def make_shirt(size = 'large' , phrase = 'eu amo python!'):
    print('\nO tamanho da camiseta é',size.title(),"e a frase estampada é", phrase)
make_shirt()
make_shirt(size = 'medium')
make_shirt('medium','danilo é lindo!')

#8.6
def describe_city(city, country = 'iceland'):
    print("\nThe city", city.title(), 'is on', country.title())
describe_city('reykjavik')
describe_city('rome', 'italy')
describe_city(city = 'barcelona' , country='spain')

#a função também pode processar alguns dados e dar um valor de retorno para o terminal, e se chama função de retorno ou return()

def get_formated_name(first_name,last_name):
    full_name = first_name+" "+last_name
    return full_name.title()
musician = get_formated_name('jimi','hendrix')
print(musician)

def get_formated_name(first_name,last_name,middle_name =""):
    if middle_name:
        full_name = first_name+" "+middle_name+" "+last_name
    else:
        full_name = first_name+" "+last_name
    return full_name.title()
name = get_formated_name('guilherme','araujo')
print(name)

#armazenando um dicionário na função;

def build_person(first_name,last_name):
    person = {
        'first':first_name , 'last':last_name
    }
    return person
musician = build_person('jimi','hendrix')
print(musician)
#caso queiramos adicionar mais coisas:
def build_person(first_name, last_name, age=""):
    person = {
        'first':first_name , 'last':last_name
    }
    if age:
        person['age'] = age
    return person

