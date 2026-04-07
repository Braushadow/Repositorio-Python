def formatted_name(name, last_name, middle_name=''):
    if middle_name: 
        full_name = f"{name} {middle_name} {last_name}"
    else:
        full_name = f"{name} {last_name}"
    return full_name.title()


musician = formatted_name('braulio','hurtado')
print(musician)

musician = formatted_name('john', 'lee', 'hooker')
print(musician)