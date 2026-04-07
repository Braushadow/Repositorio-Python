def t_shirt(size='large',text= 'I love python'):
    print(f"\nSize of the T-shirt: {size}")
    print(f"Text of the T-shirt: {text}")

t_shirt()
t_shirt('medium')
t_shirt('small','I love C++')

def describe_city(name, country = 'mexico'):
    print(f"\n{name.title()} is in {country.title()}")

describe_city('Guadalajara')
describe_city('Zapopan')
describe_city('Tonala','Atizapan')
