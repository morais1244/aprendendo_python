class Restaurant():
    def __init__(self, name, cousine):
        self.name = name
        self.cousine = cousine
    def describe_restaurant(self):
        print("O restaurante se chama: " + self.name.title() + 
              ' E a especialidade da cozinha é ' + self.cousine)
    def open_restaurant(self):
        print("O restaurante está aberto!")
            

my_restaurant = Restaurant('la boutique', 'francesa')
my_restaurant.describe_restaurant()
my_restaurant.open_restaurant()