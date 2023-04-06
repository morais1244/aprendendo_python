#Instruções if adicionará condições 
cars = ['bmw' , 'toyota' , 'audi' , 'ferrari']
for car in cars:
  if car == 'bmw': 
    print(car.upper())
  else:
    print(car.title())
#Por exemplo, nesta acima, caso o carro for bwm todas as letras serão maiusculas, caso contrário terá apenas a primeira letra maiuscula.


#Teste condicional
car='bmw'
car=='bmw'
#o terminal vai responder true or false, nesta caso true.
#esse == se chama operador de igualdade, serve para verificar se aquilo é verdadeiro ou falso.
#caso queira verificar apenas para letras minúsculas ou maúsculas basta.
car='Audi'
car.lower() == 'audi'
#Usando diferente:
request_topping = 'mushroom'
if request_topping != 'anchova':
  print('Não faça isso')
if request_topping != 'mushroom':
  print('aaaaa')
#Podemos notar que apenas 'não faça isso' foi escrito, tendo em vista que a variável definida é diferente de anchova, mas para o caso abaixo,como é igual ela não mostra.


resposta = '17'
if resposta != '42':
  print('Essa não é a resposta correta, porfavor tente novamente.')
#Também é possível incluir comparações matemáticas como.
age = 18
if age >= 18:
  print('maior de idade')
else:
  print('menor de idade')
#Além de serem úteis para verificar como.
age = 18
age == 18
age >= 10
age <= 20
#Caso eu queira verificar mais de uma por vez usamos: usando 'and'
age_1 = 18
age_0 = 10
age_1 >= 18 and age_0 <= 12
#true
age_1 >= 50 and age_0 >=20
#false

#usando 'or'
age_1 = 18
age_0 = 20
age_1 >=18 or age_0 <=19
#true

#verificando se algo está numa lista
sabores = ['mussarela' , 'calabresa' , 'peperoni' , 'napolitana']
'mussarela' in sabores
#true
'4queijos' in sabores
#false

#verificando se algo não está em uma lista, usamos not para aplicar essa condição:
users = ['carlos' , 'david' , 'barbara']
user = 'marie'
if user not in users:
  print('\n\nVocê não está cadastrado no nosso site, faça isso aqui!')


#Expressão booleana é como se chama os testes de condição!


#EXERCICIO
car = 'subaru'
print(car == 'subaru')

sabores=['mussarela']
print('mussarela' in sabores) #true

sabor='calabresa'
if sabor not in sabores:
  print("aaaa")
idade= 18
if idade >= 16:
  print("batata")
print(sabor not in sabores) #true
print(idade>=18) #true