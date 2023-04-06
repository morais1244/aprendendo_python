#Aqui usamos while para adicionar ou verificar usuários enquanto existe usuários na parte de não_verificados e assim vão sendo adicionados na lista de verificados.
unsub_users = ['guilherme', 'nicolas','danilo','henrique']
confirmed_users =[]
while unsub_users:
    current_users = unsub_users.pop() #storage with pop()
    print("Verificando "+current_users.title())
    confirmed_users.append(current_users)#add with append.()
for confirmed_user in confirmed_users:
    print(confirmed_user.title()) #verificando 

#para remover todos os valores de um mesmo valor de uma lista
pets = ['cat', 'dog','cat','dolphin','cat','fish']
while 'cat' in pets :
    pets.remove('cat')
print(pets)
#ele continuara removendo até que tenha se extinguido todos os valores iguais aquele definido no while.

responses = {}
polling_active = True
while polling_active :
    name = input("\ninsira seu nome aqui: ")
    city = input("\nInsira sua cidade natal aqui: ")
    responses[name] = city #armazena as respotas no dicionário
    yes_no=input("\nVocê gostaria de continuar essa  pesquisa :")
    if yes_no == 'no':
        polling_active = False
for name, response in responses.items():
    print(name.title()+" mora na cidade de "+response.title())

#exercicios
#7.8
print('\n')
finished_sandwich =[]
unfinished_sandwich = ['calabresa' , 'atum' , 'pepperoni' , 'queijo' , 'presunto' , 'misto']
while unfinished_sandwich:
    current_sandwich = unfinished_sandwich.pop()
    print(current_sandwich+ " está pronto!")
    finished_sandwich.append(current_sandwich)
print(finished_sandwich)

#7.9
unfinished_sandwich = ['calabresa' , 'atum' , 'pepperoni' , 'queijo' , 'presunto' , 'misto','pastache','pastache','pastache']
while 'pastache' in unfinished_sandwich:
    unfinished_sandwich.remove('pastache')
print(unfinished_sandwich)

#7.10

responses = {}
topping = True
while topping:
    name = input("insira seu nome aqui: ")
    city = input("insira uma cidade que queira visitar: ")
    responses[name]  = city 
    yes_no = input("voce deseja continuar a enquete?")
    if yes_no == 'no' :
        topping = False
for name, city in responses.items():
    print("Olhe aqui os resultados da nossa enquete: ")
    print("Nome: " + name.title() + "\t Cidade: " + city.title())
