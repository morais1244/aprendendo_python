#percorrendo dicionários com laços:
user_0 = {
    'username' : 'efermi' , 'first' : 'enrico' ,
    'last' : 'fermi' , 
}
for key, value in user_0.items():
    print("\nKey: "+key)
    print("Value: "+value)
#inclui o nome do dicionário, seguido do método items(), que devolve uma lista de pares chave-valor. O laço for então armazena cada uma desses pares nas duas variáveis especificadas. como key, value que foi no caso.

favorite_languages = {
'jen': 'python', 'sarah': 'c', 'edward': 'ruby', 'phil': 'python', }
for name, language in favorite_languages.items():
    print("\nNome: "+name.title())
    print("Linguagem: "+ language.title())

#Podemos usar o método keys() quando apenas nos interessa as chaves, mas produzirá a mesma saída de caso usássemos sem nenhum método.
friends = ['phil' , 'sarah']
for name in favorite_languages.keys():
    if name in friends:
        print("Hi" , name.title() +
        ", I see your favorite language is "+
        favorite_languages[name].title()+"!" )
    else:
        print(name.title())
#também podemos usar keys() para verificar se algo está no dicionário ou não
if 'erin' not in favorite_languages.keys():
    print("Olá Erin, vi que não respondeu a enquete ainda, se possível responder!")
#Caso queiramos que seja estabelicida uma ordem no nosso laço, basta usarmos:
print("\nAs pessoas que responderam a enquete são:")
for name in sorted(favorite_languages.keys()):
    print(name.title())

#agora percorrendo o laço nos valores usamos values()
print("\nAs linguagens mencionadas são:")
for language in favorite_languages.values():
    print(language.title())
#Isso é adequado para um número pequeno de valores, já que acontece a repetição, mas caso queiramos sem repetição usamos set(....)
print("\nAs linguagens apresentadas na enquete são:")
for language in set(favorite_languages.values()):
    print(language.title())

#Exercícios
#6.5
rios={}
rios['amarelo'] = 'china'
rios['nilo'] = 'egito'
rios['amazonas'] = 'brasil'
print("\n")
for rio, pais in rios.items():
    print("O rio "+rio.title()+" percorre o "+pais.title()+".")
print("\n")
for rio in rios.keys():
    print(rio.title())
print("\n")
for pais in rios.values():
    print(pais.title())

#6.6
print("\n")
pessoas = ['edward' , 'sarah' , 'david' , 'adão']
for pessoa in pessoas:
    if pessoa in favorite_languages.keys():
        print("Obrigado por responder "+pessoa.title())
    else:
        print("Por favor, responda a enquete "+pessoa.title())


