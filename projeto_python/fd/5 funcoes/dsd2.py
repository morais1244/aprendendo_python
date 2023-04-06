def get_formated_name(first_name,last_name):
    full_name= first_name +" "+last_name
    return full_name.title()
while True:
    f_name = input("Insira aqui seu primeiro nome: ")
    if f_name == 'q':
        break
    l_name = input("Insira aqui seu último nome: ")
    if l_name =='q':
        break
    formated_name = get_formated_name(f_name,l_name)
    print(formated_name)

#exercicios
#8.6
def city_country(city,country):
    local = city +", "+country
    return local.title()
while True:
    cidade = input("Insira a cidade que você mora: ")
    if cidade == 'q':
        break
    pais = input("Insira seu pais: ")
    if pais == 'q':
        break
    localidade = city_country(cidade, pais)
    print(localidade)

#8.7 e 8.8
def make_album(musician, name , number =""):
    album ={
        'name_album':name , 'autor': musician 
    } 
    if number :
        album['number'] = number #não serviu para o caso do input
    return album
while True:
    number=[]
    name_album = input("insira o nome do album: ")
    if name_album == 'q':
        break
    autor = input("insira o nome do autor: ")
    if autor == 'q':
        break
    continuar = input("gostaria de continuar a enquete: ") #para tornar o numero de faixas opcional
    if continuar == 'no':
        break
    number = input("insira o número de faixas: ")
    if number =='q':
        break
    if number:
        album = make_album(autor, name_album, number) #caso exista
    else:
        album = make_album(autor, name_album) #caso não exista
    print(album)

#agora usando lista ao inves de dicionario com funções 
def greet_names(names):
    for name in names:
        msg = "Welcome " + name.title()
        print(msg)
username = ['hannah','david','guilherme']
greet_names(username)

unprinted_models = ['iphone case' , 'dodehacadron' , 'samsung case']
completed_models = []
while unprinted_models :
    current_models  = unprinted_models.pop()
    print("adicionando "+current_models)
    completed_models.append(current_models)
print("Todos os modelos feitos foram esses:")
for completed_model in completed_models:
    print(completed_model)

#usando duas funcoes para tudo isso

def print_models(unprinted_models, completed_models):
    while unprinted_models:
        current_models = unprinted_models.pop()
        print("adicionando "+ current_models)
        completed_models.append(current_models)
def show_printed_models(completed_models):
    for completed_model in completed_models:
        print(completed_model)
unprinted_models = ['iphone case' , 'dodehacadron' , 'samsung case']
completed_models = []
print_models(unprinted_models,completed_models) #caso queiramos que nao se percam os valores da lista podemos usar uma copia seria unprinted_models[:]
show_printed_models(completed_models)