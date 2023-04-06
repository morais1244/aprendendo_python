#se for conhecido o índice e posição do elemento que você quer tirar da lista basta usar del lista[]
carros=['bmw','renault','ferrari','fiat']
del carros[0]
print("\n",carros,sep="")

# o método pop() serva para qund tiver um item que eu queira remover da lista, mas que posso facilmente acessa-lo depois
popped_carros=carros.pop(1)
print("\n",carros,sep="")
print("\n"+popped_carros)

#O metodo lista.remove() é usado para retirar um elemento com seu valor sabido, retira apenas a primeira ocorrencia que aparecer
motos=['honda','ninja','ducati','ferrari','mercedes']
motos.remove('ninja')
print("\n", motos,sep="")
#também é possível tirar o elemento e armazenar ele numa váriavel
too_expensive='ducati'
motos.remove(too_expensive)
print("\nA", too_expensive, "é muito cara para mim")
print(motos)


