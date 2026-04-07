
def describe_pet(pet_name, animal_type ='dog'):
    print(f"\nI have a {animal_type} !!")
    print(f"My {animal_type}'s name is {pet_name.title()}")

describe_pet(animal_type='Horse', pet_name='Juan')
describe_pet('turtle','sheldon')
describe_pet('dog','snoopy')
describe_pet('joe','rabbit')