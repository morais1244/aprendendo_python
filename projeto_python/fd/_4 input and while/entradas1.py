#capacidade de trabalhar com dados de entrada do usuário e controlar o tempo que seus programas executam com input e while
message = input("me diga algo que direi de volta a voce: ")
print(message)

#sempre escreva prompts claros
name = input("\nPor favor, insira seu nome: ")
print("Bem vindo "+name+"!")

#Podemos escrever assim, o += serve para adicionar mais uma linha ao comando que temos 
prompt = "\nPara que possamos identificá-lo"
prompt += "\nQual seu nome? "
name = input(prompt)
print("Hello, "+name.title())

#Para aceitar entradas de números precisamo usar o int depois para podermos usar a idade como um número, caso não tivesse o python entederia idade como uma string
idade = input("\nPor favor, insira sua idade: ")
idade = int(idade)
print(idade>=18)

#aplicando em um programa de verdade, numa montanha russa que autoriza de acordo com tamanho
altura = input("\nMe diga quantos metros você tem de altura: ")
altura = float(altura)
if altura >= 1.5:
    print("Pode entrar e se preparar para a aventura!")
else:
    print("Desculpe, mas você não tem altura suficiente.")

#operador de módulo % que divide um número por outro e dá o resto 4 % 3 = 1, assim podemos dizer se um número é par ou impar
número = input("Diga um número que eu direi se ele é par ou impar: ")
número = int(número)
if número % 2 == 0 :
    print("Esse número é par!")
else:
    print("Esse número é impar!")

#Exercício
#7.1 
carro = input("Me diga o carro que você gostaria de alugar: ")
print("Deixe-me ver se consigo um "+carro.title()+" para você.")

#7.2
mesa = input("Bem vindos! Mesa para quantos? ")
mesa = int(mesa)
if mesa >= 8:
    print("Infelizmente vocês terão que esperar por uma mesa.")
else:
    print("Podem vir, já temos uma esperando por vocês!")

#7.3
dez = input("Me diga um número e eu direi se ele é múltiplo de dez ou não: ")
dez = int(dez)
if dez % 10 == 0:
    print("Esse número é múltiplo de 10!")
else:
    print("Esse número não é múltiplo de 10.")
