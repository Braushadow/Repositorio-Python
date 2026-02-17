available_toppings = ['mushrooms','oives','green peppers',
                     'pepperoni','pineaple','extra cheese']

requested_toppings = ['mushrooms','french fries','extra cheese']

requestion = input(str("What do you want in your pizza?:"))
requested_toppings.append(requestion)

for requested_topping in requested_toppings:
    if requested_topping in available_toppings:
            print(f"Adding {requested_topping}.")
    else:
        print(f"Sorry, we are out of {requested_topping}")
    
print("\nFinished making your pizza!!")

