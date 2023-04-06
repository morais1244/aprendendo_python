listax=['henrique','alisson','danilo']
messagem_1= listax[0].title()+" para de ser estranho."
messagem_2= listax[1].title()+" bora jogar lol depois daqui!"
messagem_3=listax[2].title()+" voce fala demais mas eu gosto de tu."
print("\n"+messagem_1)
print("\n"+messagem_2)
print("\n"+messagem_3)
nao_pode= listax[2]
listax.remove(nao_pode)
print("\n",listax,sep="")
messagem_n= nao_pode.title()+" não pode participar pois tem o aniversário de sua mãe no mesmo dia"
print(messagem_n)
listax.append('joao')
print("\n",listax,sep="")
listax.append('carlos')
listax.insert(0,'paulo')
print("\n",listax,sep="")
listax.insert(2,'gordo')
print("\n",listax,sep="")
messagem_mesa="Adicionei "+listax[-1]+","+listax[0]+" e "+listax[2]+" a lista pois encontramos uma mesa maior"
print("\n"+messagem_mesa)
messagem_mesamenor="Caros convidados, sinto-lhes informar que infelizmente a mesa maior não chegará a tempo e eu sinto muito mas terei que retirar alguns colegar!"
print("\n"+messagem_mesamenor)
print(listax)
print(listax[2])
pessoas_retiradas= listax.pop(1), listax.pop(0), listax.pop(3),listax.pop(-1)
print("\n",listax,sep="")
print("\n",pessoas_retiradas,sep="")
messagem_tira="me desculpe "+pessoas_retiradas[0]
print(messagem_tira)
del listax[0]
del listax[0]
print("\n",listax,sep="")




