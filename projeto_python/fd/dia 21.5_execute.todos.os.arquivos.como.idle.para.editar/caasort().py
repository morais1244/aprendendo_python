#Como organizar minha lista? A organização pode ser feita com a função sort() que deixa toda a lista em ordem alfabetica
nomes=['armando','joao','beto','carlos','daniel']
nomes.sort()
print(nomes)
#para organizar na ordem inversa basta usar sort(reverse=True)
nomes.sort(reverse=True)
print("\n",nomes,sep="")
#Para alterar a lista apenas temporariamente, podemos usar o sorted(lista) oque apenas usa a lista em ordem alfabetica mas não altera sua composição permanentemente
nomes=['armando','joao','beto','carlos','daniel']
print("\n",sorted(nomes),sep="")
#Para alterar a ordem da lista para sua inversa basta usar .reverse()
print("\n",nomes,sep="")
nomes.reverse()
print("\n",nomes,sep="")
#muito util, para descobrir a quantidade de elementos naquela lista basta usarmos len(....) ou print(len(nomes))
print("\nO número de nomes na lista de chamada é",len(nomes))


