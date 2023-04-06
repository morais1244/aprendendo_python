class Restaurant():
    def __init__(self, name, cousine):
        self.name = name
        self.cousine = cousine
        self.number_served = 0  
    def set_number_served(self, number_served):
        if number_served >= self.number_served:    
            self.number_served = number_served
        else:
            print("Impossível voltar atrás nos números de clientes atendidos!")
    def increment_number_served(self, number):
        if number > 0:
            self.number_served += number
        else:
            print("Não tem como perder um cliente no momento!")
    def number_served12(self):
        print("O número de clientes atendidos no dia de hoje foram: "+
              str(self.number_served))
    def describe_restaurant(self):
        print("O restaurante se chama: " + self.name.title() + 
              ' E a especialidade da cozinha é ' + self.cousine)
    def open_restaurant(self):
        print("O restaurante está aberto!")

myrestaurant = Restaurant('la boutique', 'francesa')
myrestaurant.increment_number_served(10)
myrestaurant.number_served12()
