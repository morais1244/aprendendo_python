#Aninhar informações significa armazenar um conjunto de dicionários em uma lista ou usar uma lista como valor de um dicionário
alien_0 = {
    'color' : 'green' , 'points' : 5
}
alien_1 = {
    'color' : 'yellow' , 'points' : 10
}
alien_2 = {
    'color' : 'red' , 'points' : 15
}
aliens = [alien_0 , alien_1 , alien_2]
for alien in aliens:
    print(alien)

#Usamos o laço for para criar uma tropa de aliens, o range(x) diz ao python quantas vezes você quer que esse laço se repita.
aliens = []
for alien_number in range(30):
    new_alien = {
        'color' : 'green' , 'points' : 5,
        'speed' : 'slow'
    }
    aliens.append(new_alien)
for alien in aliens[:5]:
    print(alien)
print(len(aliens))
#Todos os aliens são iguais, mas o python trata eles todos de maneira diferente
for alien in aliens[0:3]:
    if alien['color'] == 'green':
        alien['color'] = 'yellow'
        alien['speed'] = 'medium'
        alien['points'] = 10
for alien in aliens[0:5]:
    print(alien)

#armazenando uma lista em um valor 
pizza = {
    'borda' : 'crocante' , 'ingredientes': ['cogumelo' , 'requeijão']
}
for borda,ingrediente in pizza.items():
    print(ingrediente)


favorite_languages = {
'jen': ['python', 'ruby'], 'sarah': ['c'], 'edward': ['ruby', 'go'],
'phil': ['python', 'haskell'], }
for person, languages in favorite_languages.items():
    print("\nA linguagem favorita do "+person.title()+" é")
    for language in languages:
        print("\t"+language.title())


print("\n")
for person, languages in favorite_languages.items():
    if len(languages) == 1:
        print("\nA linguagem favorita do "+person.title()+" é")
        for language in languages:
            print("\t"+language.title())
    else:
        print("\nAs linguagens favoritas do "+person.title()+" são")
        for language in languages:
            print("\t"+language.title())

#podemos também armazenar dicionários em outros dicionários como por exemplo:
usuarios = {
    'gmorais':{'first_name':'guilherme' , 'last_name':'morais', 'city':'fortaleza'},
    'hholanda':{'first_name':'henrique','last_name':'holanda','city':'fortaleza'},
}
for username, user_infos in usuarios.items():
    print("username:"+username)
    full_name = user_infos['first_name'] + " "+user_infos['last_name']
    location = user_infos['city']
    print("nome:"+full_name)
    print("localidade:"+location)

#exercícios:
#6.7
pessoa_0 = {}
pessoa_0['first_name'] = 'guilherme'
pessoa_0['last_name'] = 'araujo'
pessoa_0['age'] = 17
pessoa_0['city'] = 'fortaleza'
pessoa_1 = {
    'first_name':'henrique' , 'last_name':'holanda', 'age':19 ,
    'city':'fortaleza'
}
pessoa_2 = {
    'first_name':'danilo','last_name':'alencar','age':20,'city':'recife'
}
pessoas = [pessoa_0,pessoa_1,pessoa_2]
for pessoa in pessoas:
    print(pessoa)

#6.8
malu = {
    'tipo':'cachorro' , 'dono':'carol'
}
cash = {
    'tipo':'cachorro','dono':'matheus'
}
gatinho = {
    'tipo':'gato' , 'dono':'geovana'
}
pets = [gatinho,malu,cash]
for pet in pets:
    print(pet)

#6.9
print("\n")
favorite_numbers = {
    'nicolas' :[25,6] , 'danilo' : [7,8] , 'henrique' : [17,12],
    'guilherme' : [27,3]
}
for nome,numbers in favorite_numbers.items():
    print("Os números favoritos do " + nome.title()
    +" são:")
    for number in numbers:
        print("\t"+str(number))

#6.10
print("\n")
cities = {
    "paris" : {'pais':'frança' , 'população':2.2, 'fact':'torre eifel'} ,
    "berlim" :{'pais':'alemanha','população':3.6, 'fact':'muros de berlim'},
    "rio de janeiro":{'pais':'brasil','população':6.7, 'fact':'cristo redentor'}
}
for cidades, infos in cities.items():
    print("\nCidade: "+cidades.title())
    pais = infos['pais']
    população = infos['população']
    fatos = infos['fact']
    print("Pais: "+pais.title())
    print("População: "+str(população),"milhões de pessoas")
    print("Fato: "+fatos.title())

    