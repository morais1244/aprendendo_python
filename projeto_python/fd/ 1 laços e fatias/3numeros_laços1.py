#A função range(1,n) mostrará os números de 1 até n-1 em sequência!
for valor in range(1,5):
  print(valor)
#Criar uma lista com os números de 1 a 50:
numbers=list(range(1,50))
print(numbers)
#Podemos também criar uma PA, mostrando o número a ser somado logo após o n-1 número da lista.
for valor1 in range(1,20,3):
  print(valor1)
#Também podemos criar uma grande lista como uma função como:
quadrados=[]
for value in range(1,11):
  quadrado=value**2
  quadrados.append(quadrado)
print(quadrados)
del quadrados
quadrados=[]
for value in range(1,11):
  quadrados.append(value**3)
print(quadrados)
#Aplicações simples dentro das listas.
digitos=list(range(1,11))
print(min(digitos))
print(max(digitos))
print(sum(digitos))
#List comprehensions mistura o "for" e uma função tudo na mesma linha e fica muito bonito!!!
digitos=list(value**2 for value in range(1,11))
print(digitos)
