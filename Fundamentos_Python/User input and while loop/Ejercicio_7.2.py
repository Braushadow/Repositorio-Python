prompt = "\nIngrese el topping que desea agregar a su pizza: "
prompt += "\nCuando haya terminado, ingrese la palabra 'quit'"

toppings = []
topping = ''

while topping != 'quit':
    topping = input(prompt)
    if topping != 'quit':
        toppings.append(topping)
        print(f"\nAnadiendo {topping} a su pizza")
    else:
        print("Ingredientes que tiene su pizza\n")
        for topping in toppings:
            print(f"-{topping}")



prompt = "\nIngrese su edad: "
prompt += "\nTeclee 'salir' para terminar:"
while True:
    edad = input(prompt)
    if edad == 'salir':
        break
    else:
        age = int(edad)
        if age < 3:
            print("Tu boleto es gratuito")
        elif age >=3 and age <=12:
            print("Tu boleto cuesta $10")
        elif age >= 12:
            print("Tu boleto cuesta $15")