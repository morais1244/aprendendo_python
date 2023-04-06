ingredientes = ["requeijão" , "pepperoni" , "tomate"]
for ingrediente in ingredientes:
    print("Adicionando",ingrediente+".")
print("pronto, sua pizza está pronta!")


#Se a pizzaria ficasse sem tomate?
for ingrediente in ingredientes:
    if ingrediente == "tomate":
        print("Desculpe, estamos sem tomate!")
    else:
        print("Adicionando",ingrediente+".")
print("pronto, sua pizza está pronta!")

#Verificando se a lista está vázia, se usar um instrução if numa lista, ele irá devolver true se tiver ao menos um elemento, caso contrário false
ingredientes = []
if ingredientes:
    for ingrediente in ingredientes:
        print("Adicionando",ingrediente+".")
else:
    print("Tem certeza que quer sua pizza simples?")



#Exercícios 
#5.8
users = ['danilo', 'nicolas' , 'henrique' , 'admin' , 'guilherme']
if users:
    for user in users:
        if user == 'admin':
            print("\nBem vindo admin, gostaria de olhar os relatórios?")
        else:
            print("\nBem vindo "+user.title()+".")
#5.9
users = []
if users:
    for user in users:
        if user == 'admin':
            print("\nBem vindo admin, gostaria de olhar os relatórios?")
        else:
            print("\nBem vindo "+user.title()+".")
else:
    print("\nPrecisamos encontrar alguns usuários!!")
#5.10
current_users = ['danilo' , 'caio' , 'gui' , 'henrique' , 'nick']
new_users = ['danilo' , 'gui' , 'carol' , 'ale' , 'carlos']
for new_user in new_users:
    if new_user.lower() in current_users:
        print("\nEste nome de usuário já foi usado, por favor escolha um novo nome.")
    else:
        print("\nEste nome de usuário está disponível!")

#5.11
numbers = list(range(1,10))
for number in numbers:
    if number == 1:
        print("1st")
    elif number == 2:
        print("2nd")
    elif number == 3:
        print("3rd")
    else:
        print(str(number)+"th")

