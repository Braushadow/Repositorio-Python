class Restaurant:
    def __init__(self,restaurant_name, cuisine_type):
        self.restaurant_name = restaurant_name
        self.cuisine_type = cuisine_type
        self.number_served = 0

    def describe_restaurant(self):
        print(f"The name of the restaurant is {self.restaurant_name.title()}")
        print(f"The cuisine type is: {self.cuisine_type.title()}")

    def open_restaurant(self):
        print(f"\nThe restaurant {self.restaurant_name.title()} is now open")

    def set_numer_served(self, number_served):
        self.number_served = number_served

    def increment_user_served(self, number_served):
        self.number_served += number_served


restaurant = Restaurant('El pollo pepe', 'mexican')
print(f"The restaurant name is {restaurant.restaurant_name.title()}")
print(f"The cuisine type of the restaurant is {restaurant.cuisine_type}")
print(f"The number of costumers served is {restaurant.number_served}")
restaurant.open_restaurant()
restaurant.set_numer_served(20)
print(f"The number of costumers served is {restaurant.number_served}")
restaurant.increment_user_served(14)
print(f"The number of costumers served is now {restaurant.number_served}")

restaurant2 = Restaurant('Little caesars', 'italian')
print(f"The restaurant name is {restaurant2.restaurant_name.title()}")
print(f"The cuisine type of the restaurant is {restaurant2.cuisine_type}")
restaurant2.open_restaurant()

restaurant3 = Restaurant('Qin', 'china food')
print(f"The restaurant name is {restaurant3.restaurant_name.title()}")
print(f"The cuisine type of the restaurant is {restaurant3.cuisine_type}")
restaurant3.open_restaurant()

class User:
    def __init__(self, first_name, last_name, age, career, login_attempts = 0):
        self.first_name = first_name
        self.last_name = last_name
        self.age = age
        self.career = career
        self.login_attempts = login_attempts
    
    def describe_user(self):
        print(f"\nName: {self.first_name.title()}")
        print(f"Last name: {self.last_name.title()}")
        print(f"Age: {self.age}")
        print(f"Career: {self.career.title()}")
        print(f"Number of login attempts: {self.login_attempts}")

    def greet_user(self):
        print(f"Have a great day!!")

    def increment_login_attempts(self):
        self.login_attempts +=1

    def reset_login_attempts(self):
        self.login_attempts = 0


user1 = User('braulio', 'hurtado', 20, 'Computer engineer', 0)
user1.increment_login_attempts()
user1.increment_login_attempts()
user1.increment_login_attempts()
user1.increment_login_attempts()
user1.increment_login_attempts()

user1.describe_user()
user1.greet_user()

user1.reset_login_attempts()
user1.describe_user()

class IceCreamStand(Restaurant):
    def __init__(self, restaurant_name, cuisine_type):
        super().__init__(restaurant_name, cuisine_type)
        self.flavors = ['lemon', 'strawberry', 'cookies', 'vanilla']

    def display_flavors(self):
        print("Available flavors\n")
        for flavor in self.flavors:
            print(f"-{flavor}")

restaurant4 = IceCreamStand("La michoacana", "Desserts")
restaurant4.display_flavors()


class Privileges:
    def __init__(self):
        self.privileges = ['can add post', 'can delete post', 'can ban user']

    def show_privileges(self):
            print("Administrator options")
            for privilege in self.privileges:
                print(f"-{privilege}")


class Admin(User):
    def __init__(self, first_name, last_name, age, career, login_attempts = 0):
        super().__init__(first_name, last_name, age, career, login_attempts)
        self.privileges = Privileges()


admin = Admin('Jonny', 'Marquez', 20, 'Computer science')
admin.describe_user()
admin.privileges.show_privileges()

