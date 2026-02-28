sandwich_orders = ['pastrani','clasic','american','pastrani','beacon','salami','pastrani']
finished_sandwiches = []

print("The deli has run out of pastrani")
while 'pastrani' in sandwich_orders:
        sandwich_orders.remove('pastrani')

while sandwich_orders:
    current_sandwich = sandwich_orders.pop()

    print(f"I made your {current_sandwich} sandwich")
    finished_sandwiches.append(current_sandwich)

print("Finished sandwiches are:\n")
for sandwich in finished_sandwiches:
    print(sandwich)

responses = {}
polling_active = True

while polling_active == True:
     name = input("What is your name? ")
     response = input("If you could visit one place on the world, where would it be? ")

     responses[name] = response

     repeat = input("Would you like to let another person respond (yes/no)")
     if repeat == 'no':
          polling_active = False

print("---Polling results---")
for name,response in responses.items():
     print(f"{name.title()} would like to visit {response}")
     