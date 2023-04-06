#Exercícios página 123

#5.3
alien_color = "green"
if alien_color == "green":
  print("Parabéns, você acabou de ganhar 5 pontos!")
if alien_color == "black":
  print("aaa") #false!

#5.4
alien_color = "red"
if alien_color == "green":
  print("Parabéns, você acabou de ganhar 5 pontos!")
else:
  print("\nParabéns, você acabou de ganhar 10 pontos!")
alien_color = "green"
if alien_color == "green":
  print("\nParabéns, você acabou de ganhar 5 pontos!")
else:
  print("Parabéns, você acabou de ganhar 10 pontos!")

#5.5
alien_color = "yellow"
if alien_color == "green":
  print("Parabéns, você acabou de ganhar 5 pontos!")
elif alien_color == "yellow":
  print("\nParabéns, você acabou de ganhar 15 pontos!")
else:
  print("Parabéns, você acabou de ganhar 10 pontos!")

alien_color = "green"
if alien_color == "green":
  print("\nParabéns, você acabou de ganhar 5 pontos!")
elif alien_color == "yellow":
  print("\nParabéns, você acabou de ganhar 15 pontos!")
else:
  print("\nParabéns, você acabou de ganhar 10 pontos!")

alien_color = "red"
if alien_color == "green":
  print("\nParabéns, você acabou de ganhar 5 pontos!")
elif alien_color == "yellow":
  print("\nParabéns, você acabou de ganhar 15 pontos!")
else:
  print("\nParabéns, você acabou de ganhar 10 pontos!")

#5.6
age = 13
if age < 2:
  print("Você é um bebê")
elif age < 4:
  print("Você é uma criança")
elif age <13:
  print("Você é um(a) garoto(a)")
elif age <20:
  print("\nVocê é um(a) adolescente")
elif age <65:
  print("Você é um adulto")
else:
  print("Você é um idoso")

#5.7
frutas_favoritas= ["banana" , "goiaba"]
if "banana" in frutas_favoritas:
    print("Você realmente gosta de bananas!")
if "goiaba" in frutas_favoritas:
    print("Você realmente gosta de goiabas!")
if "maça" in frutas_favoritas:
    print("Você realmente gosta de maças!")
if "kiwi" in frutas_favoritas:
    print("Você realmente gosta de kiwi!")
if "pêssego" in frutas_favoritas:
    print("Você realmente gosta de pêssego!")
    