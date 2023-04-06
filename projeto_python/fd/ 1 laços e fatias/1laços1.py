magicos=['joao','paulo','carlos']
for magico in magicos:
  print(magico)
#"for package_list in large_list:"Serve para ditar os componentes da lista, ajuda le-se “para todo mágico na lista de mágicos, exiba o nome do mágico" lembre-se dos dois ponto : 
for magico in magicos:
  print("\n"+magico.title()+", o show está para começar.")
#Podemos adicionar frases após cada exibição!
for magico in magicos:
  print("\nEssa foi uma boa mágica, "+magico.title())
  print(magico.title() + ", muito obrigado pelo show, já estou ansioso pelo próximo!")
