class Dog():
    def __init__(self , name , age):
#__init__() é um método, identico a funcoes, sempre que criamos uma nova instancia precisamos usar esse metodo especial do python precisamos usar o parametro self antes sempre 
        self.name = name
        self.age = age
#qualquer variavel com o prefixo self está disponível para todos os métodos
#variaveis acessiveis atraves de instancias sao chamadas de atributos
    def sit(self):
        print(self.name.title()+" está sentando")
    def roll_over(self):
        print(self.name.title()+" está rolando")


my_dog = Dog('willie' , 6)
print("My dog " + my_dog.name.title() + " have " + str(my_dog.age) + 
        ' years old')
#para acessarmos os atributos basta usarmos o ponto, my_dog.age or my_dog.name , para chamarmos os metodos, fazemos as mesmas coisas
my_dog.sit()
my_dog.roll_over()
