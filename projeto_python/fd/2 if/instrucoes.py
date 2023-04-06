#função if
age = 12
if age <= 18:
  print("menores de idade não são bem vindos.")
  print("volte quando tiver idade!")

#função if-else
age = 18
if age >=18:
  print("seja bem vindo!")
else:
  print("menores de idade são proibidos!")

#função if-elif-else
age = 12
if age < 4: #false
  print("seu custo de entrada é gratuito")
elif age >= 18: #false
  print("seu custo de entrada é 10 dolares")
else: #true
  print("seu custo de entrada é 5 dolares")

#mais simples!
age = 12
if age <4:
  price=0
elif age <18:
  price=5
elif age >=60:
  price = 7
else: 
  price=10
print("\nseu custo de entrade é $" + str(price) +".")

#também é interessante em alguns casos omitir o bloco else, e assim dando mais confiança ao seu código e mais simples de vizualizar 
age = 62
if age <4:
  price=0
elif age <18:
  price=5
elif age < 60:
  price=10
elif age >=60:
  price=5
print("\nSeu custo de entrada é $"+str(price)+".")

#usando várias condições if, no caso varias podem ser true usamos if separadamente
ingredientes = ["cream cheese" , "pepperoni"]
if "cream cheese" in ingredientes:
  print("\nAdicione cream cheese.")
if "pepperoni" in ingredientes:
  print("\nAdicione pepperoni.")
if "mushroom" in ingredientes:
  print("\nAdicione cogumelos.")
  
