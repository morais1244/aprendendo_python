#4.10
nomes=['carlos' , 'gui' , 'pedro' , 'joao' , 'paulo' , 'davi' , 'jorge']
print("Os três primeiros nomes da lista são:")
print(nomes[:3])
print("\nOs três últimos nomes da lista são:")
print(nomes[4:])
pizzas=['calabresa' , '4queijos' , 'mussarela']
amigos_pizzas=pizzas[:]
print(pizzas)
print(amigos_pizzas)
pizzas.append('pepperoni')
amigos_pizzas.append('portuguesa')
print(pizzas)
print(amigos_pizzas)
print("\nMinhas pizzas favoritas são:")
for pizza in pizzas:
  print(pizza.title())
print("\nA pizza favorita dos meus amigos são:")
for amigos_pizza in amigos_pizzas:
  print(amigos_pizza.title())
