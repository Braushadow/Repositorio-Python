pizzas = ['peperoni','double cheese', 'hawaian']
for pizza in pizzas: 
    print(f"I like {pizza.title()} pizza!")

print("\nI really love all kind of pizzas!!\n\n")

animals = ['snake','cat','dog']
for animal in animals:
    print(f"A {animal.title()} would be an amazing pet")

print("\nAll animals have colas\n")

friend_pizzas = pizzas[:]

pizzas.append('three beefs')
friend_pizzas.append('vegie pizza')

print("My favorite pizzas are:")
for pizza in pizzas:
    print(pizza)

print("My friend's favorite pizzas are:")
for friend_pizza in friend_pizzas:
    print(friend_pizza)