#tuplas são listas imutáveis e basta usarmos parenteses no local de colchetes para definirmos
dimension = (200, 50)
print(dimension[0])
print(dimension[1])
for dimesion1 in dimension:
  print(dimesion1)
#eu posso sobrescrever os dados por cima de outro, ou seja
dimesion = (400, 100)
print(dimesion)

#EXERCÍCIO
cardapio = ('ovo benedict' , 'file migno' , 'tartar' , 'chocolate')
print('\nEsses são os itens do cardápio, certifiquem-se de provarem todos:')
for cardapio1 in cardapio:
  print(cardapio1)
cardapio = ('ovo benedict' , 'file migno' , 'picadinho' , 'creme')
print('\nHouve uma alteração no cardápio e o novo é esse:')
for cardapio1 in cardapio:
  print(cardapio1)
  