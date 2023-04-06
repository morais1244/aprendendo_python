#Para fatiar uma lista, precisamos usar o list[0:3] para especificar de onde e até onde minha fatia vai;
players=['carlos' , 'davi' , 'martin' , 'gui' , 'valen']
print(players[0:3])
print(players[:5])
print(players[2:5])
print(players[1:])
print(players[:2])

#Para utilizar isto no laço, basta específicar na lista de onde até onde vai essa fatia;
print("\nAqui estão os três principais jogadores do meu time:")
for player in players[:3]:
  print(player.title())

#Podemos copiar uma lista apenas definindo uma variavel nova com a lista inteira:
comidas=['cenoura' , 'batata' , 'pizza' , 'hamburguer' , 'batata-frita']
amigos_comidas=comidas[:]
print('\n',amigos_comidas,sep="")
amigos_comidas.insert(0,'lasanha')
print('\n',amigos_comidas,sep="")
comidas.append('coxinha')
print('\n', comidas, sep='')
