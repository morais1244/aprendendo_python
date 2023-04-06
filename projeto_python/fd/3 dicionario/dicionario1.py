#Dicionario armazenam informações sobre u mesmo tipo de coisa, ou seja, armazena duas informações ou mais que possam ser combinadas:
alien_0 = {'color' : 'green' , 'points' : 5}
print(alien_0['color'])
print(alien_0['points'])

#coleção de pares chave-valor. pode usar a chave para acessar o valor associado a ela, chave pode ser uma string uma lista ou até mesmo outro dicionário
new_points = alien_0['points']
print("Parabéns, você acaba de conseguir",str(new_points)+"pontos.")

#para adicionarmos novos pares basta:
alien_0['x_position'] = 0
alien_0['y_position'] = 25
print(alien_0)

#As vezes é mais conveniente começar com um dicionário vazio
alien_0 = {}
alien_0['color'] = 'green'
alien_0['points'] = 5
print(alien_0)

#para modificarmos um valor, basta adotarmos um novo valor
print("A cor do alien é",alien_0['color']+".")
alien_0['color'] = 'yellow'
print("A cor do alien agora é" , alien_0['color']+".")

#Exemplo mais divertido/complexo
alien_0 = {}
alien_0['x_position'] = 0
alien_0['y_position'] = 25
alien_0['speed'] = 'medium'
print("\nOriginal x-position: " + str(alien_0['x_position']))
#move o alienígena para a direita
#determina a distância que o alienígena deve se deslocar de acordo com sua velocidade atual
if alien_0['speed'] == 'slow':
    x_increment = 1
elif alien_0['speed'] == 'medium':
    x_increment = 2
elif alien_0['speed'] == 'fast':
    x_increment = 3
alien_0['x_position'] = alien_0['x_position'] + x_increment
print("\nThe new x-position is: "+str(alien_0['x_position']))

#para remover pares chave-valor usamos a instrução del 
alien_0 = {'color':'green' , 'points':5}
print(alien_0)
del alien_0['points']
print(alien_0)

#um dicionário pode também ser utilizado para armazenar resultados de uma enquete por exemplo:
favorite_languages = {
    'jen':'python' , 'sarah':'c' , 'edward':'ruby' , 'phil':'python',
}
print(favorite_languages)
print("Sarah's favorite language is " +
 favorite_languages['sarah'].title() +
    ".")

#Exercicios
#6.1
pessoa = {}
pessoa['first_name'] = 'guilherme'
pessoa['last_name'] = 'araujo'
pessoa['age'] = 17
pessoa['city'] = 'fortaleza'
print(pessoa)
print( "Nome:"+
    pessoa['first_name'].title(),
    pessoa['last_name'].title()+
    "; Idade:"+
    str(pessoa['age'])+
    "; Cidade:"+pessoa['city'].title()
    +".")

#6.2
favorite_numbers = {
    'nicolas' : 25 , 'danilo' : 7 , 'henrique' : 17,
    'guilherme' : 27
}
print("\nO número favorito do Henrique é",str(favorite_numbers['henrique'])+".")

