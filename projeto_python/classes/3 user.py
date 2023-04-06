class User():
    def __init__(self, first_name, last_name, age, city):
        self.first_name = first_name
        self.last_name = last_name
        self.age = age
        self.city = city
    def describe_user(self):
        print("Informacoes do usuário \nNome: "+self.first_name.title(), self.last_name.title() +"\nIdade: "+str(self.age)+"\nCidade: "+ self.city.title())
    
user = User('guilherme' ,'araujo', 17, 'fortaleza')
user.describe_user() 

