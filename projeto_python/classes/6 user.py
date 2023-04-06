class User():
    def __init__(self, first_name, last_name, age, city):
        self.first_name = first_name
        self.last_name = last_name
        self.age = age
        self.city = city
        self.login_attempts = 0
    def increment_login_attempts(self, attempts):
        self.login_attempts += attempts
    def reset_login_attempts(self):
        self.login_attempts = 0
    def show_login_attempts(self):
        print(str(self.login_attempts))
    def describe_user(self):
        print("Informacoes do usuário \nNome: "+self.first_name.title(), self.last_name.title() +"\nIdade: "+str(self.age)+"\nCidade: "+ self.city.title())
    
user = User('guilherme' ,'araujo', 17, 'fortaleza')
user.describe_user() 
user.increment_login_attempts(20)
user.show_login_attempts()
user.reset_login_attempts()
user.show_login_attempts()
    