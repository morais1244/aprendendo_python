names=['gui','david','joao']
print(names)
print("\n"+names[0])
print("\n"+names[1])
print("\n"+names[2])
#podemos definir qual dos nomes da lista vão aparecer definindo com um k=0,1,2,3,... na sequência
print("\n"+names[-1])
#podemos acessar o último termo da lista sem saber o seu tamanho apenas colocando -1, e adotamos um n=-1,-2,-3 como se fosse vista de trás pra frente
message= names[0].title()+" foi levar sua vó a padaria."
print("\n"+message)

play=['playstation','xbox','pc','nitendo']
messagem="queria jogar um "+play[0].title()
print("\n"+messagem)
