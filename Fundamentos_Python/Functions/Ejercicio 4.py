def make_sandwich(*items):
    print("Making a sandwich with the next items:")
    for item in items:
        print(f"-{item}")

make_sandwich('Jam','cheese','tomato', 'onions')

def build_profile(first, last, **user_info):
    user_info['first_name']= first
    user_info['last_name']= last
    return user_info

user_profile = build_profile('Braulio', 'Hurtado',
                             field = 'computer science',
                             location = 'CUCEI',
                             console = 'Xbox series S')

print(user_profile)


def cars(manufacturer, model_name ,**features):
    features['manufacturer'] = manufacturer
    features['model_name'] = model_name
    return features

car_info = cars('Honda', 'Civic',
                kilometers_ph = 500,
                cilinders = 6)

print(car_info)