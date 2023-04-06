#4.6
for odd in range(1,20,2):
  print(odd)
#4.7
numeros3=list(value*3 for value in range(1,11))
print(numeros3)
#mais longo:
numbers=[]
for value in range(3,31,3):
  numbers.append(value)
print(numbers)
#4.8
for valor in range(1,11):
  print(valor**3)
#4.9
cubos=list(cubo**3 for cubo in range(1,11))
print(cubos)
print("Esta acima é a lista de cubos de 1 a 10.")