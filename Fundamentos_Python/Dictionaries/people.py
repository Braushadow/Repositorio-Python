person = {
    'first_name': 'Braulio',
    'last_name' : 'Hurtado',
    'age' : 20,
    'city' : 'Guadalajara'
}

print(f"Name: {person['first_name']}")
print(f"Last name: {person['last_name']}")
print(f"Age: {person['age']}")
print(f"City: {person['city']}")

favorite_numbers = {
    'Cris' : 8,
    'Jonny' : 7,
    'Miguelin' : 10,
    'Braulio' : 12,
    'Ana' : 22
}

print(f"Favorite number of Braulio: {favorite_numbers['Braulio']}")
print(f"Favorite number of Cris: {favorite_numbers['Cris']}")
print(f"Favorite number of Jonny: {favorite_numbers['Jonny']}")
print(f"Favorite number of Ana: {favorite_numbers['Ana']}")
print(f"Favorite number of Miguelin: {favorite_numbers['Miguelin']}")

programming_words = {
    'if_statement': 'Is a condition that we stablished for something',
    'for_loop' : 'A way to repeat an event',
    'integer' : 'A number without decimal dot',
    'float' : 'A number that includes decimals',
    'format' : 'Is a way to make the code more simple'
    }


for key ,value in programming_words.items():
    print(f"\n{key.title()}: {value}")