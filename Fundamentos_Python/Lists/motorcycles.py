#Definicion de la lista de motocicletas
motorcycles = []

motorcycles.append ('honda')
motorcycles.append('suzuki')
motorcycles.append('ducati')
motorcycles.insert(3, 'yamaha')

print(motorcycles)

#Metodo del
del motorcycles[0]
print(motorcycles)
motorcycles.append('honda')
print(motorcycles)

#Metodo pop
first_owned = motorcycles.pop(0)
print(motorcycles)
print(f"La primera motocicleta que compramos fue de la marca {first_owned.title()}")

print(motorcycles)
too_expensive = 'ducati'
motorcycles.remove(too_expensive)
print(motorcycles)
print(f"\n A {too_expensive.title()} is to expensive for me")

