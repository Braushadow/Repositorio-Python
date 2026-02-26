person = {
    'first_name': 'Braulio',
    'last_name' : 'Hurtado',
    'age' : 20,
    'city' : 'Guadalajara'
}

person2 = {
    'first_name' : 'Cris',
    'last_name' : 'Avalos',
    'age' : 20,
    'city': 'Guadalajara'
}

person3 = {
    'first_name' : 'Jonny',
    'last_name' : 'Marquez',
    'age' : 21,
    'city' : 'Guadalajara',
}

people = [person,person2,person3]

for person in people:
    print(f"\nName: {person['first_name']}")
    print(f"Last name: {person['last_name']}")
    print(f"Age: {person['age']}")
    print(f"City: {person['city']}")

garfield = {
    'kind' : 'cat',
    'owner_name' : 'John'
}

snoopy = {
    'kind' : 'dog',
    'owner_name' : 'Charlie Brown'
}

jorge = {
    'kind' : 'monkey',
    'owner_name' : 'The man with the yellow coat'
}

pets = [garfield,snoopy,jorge]

for pet in pets:
    print(f"\nKind: {pet['kind']}")
    print(f"Owner's name: {pet['owner_name']}")

favorite_places = {
    'United_states' : 'New york',
    'Mexico' : 'Nayarit',
    'Alemania' : 'Berlin'
}

