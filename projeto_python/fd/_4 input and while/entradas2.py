#enquanto o laço for cita cada elemento por vez, o laço while irá citar algo enquanto ou durante algo for verdadeiro
numero = 1
while numero <= 5:
    print(numero)
    numero +=1
#enquanto numero for menor de 5 ele irá printar e adicionar 1

prompt = "\nMe diga algo e direi de volta: "
prompt += "\nInsira 'quit' se quiser sair."
messagem = " "
while messagem != 'quit':
    messagem = input(prompt)
    if messagem != 'quit':
        print(messagem)
        
#Quando o programa necessita de muitas condições para continuar funcionando, usamos a variável flag
prompt = "\nMe diga algo e direi de volta: "
prompt += "\nInsira 'quit' se quiser sair."
active = True #nossa flag é 'active'
while active:
    messagem = input(prompt)
    if messagem.strip() == 'quit':
        active = False
    else: 
        print(messagem) 

#Para quebrar um laço while de imediato basta usarmos break
cidade= "\nInsira aqui uma cidade que você gostaria de visitar."
cidade += "\nInsira 'quit' se quiser sair do programa. \n"
while True: #só irá parar se receber um 'break'
    messagem = input(cidade)
    if messagem == 'quit':
        break #comando break quebra o laço while
    else: 
        print("Que maravilhoso!Adoraria conhecer "+messagem+" também!")

i = 0
while i < 10:
    i += 1
    if i % 2 == 0:
        continue
    print(i)

#exercicos
#7.4
prompt = "Uma pizza esta sendo feita, acrescente aqui o ingrediente desejado"
prompt += "\nCaso deseje sair, insira 'quit'. \n"
while True:
    ingrediente = input(prompt)
    if ingrediente != 'quit':
        print("\nAdicionando "+ingrediente)
    if ingrediente == 'quit':
        break

#7.5
while True:
    idade = input("Escreva aqui sua idade: ")
    idade = int(idade)
    if idade == 0:
        break
    if idade <3 :
        print("Sua entrada eh gratuita.")
    elif idade <12:
        print('Sua entrada custa 10 dolares.')
    else:
       print('Sua entrada custa 15 dolares.')
    
