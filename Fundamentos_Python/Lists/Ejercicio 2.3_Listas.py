guest_list = ['leonardo di caprio', 'bruce wayne', 'peter parker']

message1 = f"Feliz navidad para ti {guest_list[0].title()}, ven a cenar"
message2 = f"Conozca sus limites señor {guest_list[1].title()} y no se termine la cena"
message3 = f"{guest_list[2].title()} es spiderman y esta invitado a la cena"

print(message1)
print(message2)
print(message3)

print(f"\nEl invitado {guest_list[2].title()} no podra asistir a la cena\n")

guest_list.remove('peter parker')
print(guest_list)
guest_list.append('logan')

message1 = f"Feliz navidad para ti {guest_list[0].title()}, ven a cenar"
message2 = f"Conozca sus limites señor {guest_list[1].title()} y no se termine la cena"
message3 = f"{guest_list[2].title()} esta invitado a la cena"

print(message1)
print(message2)
print(message3)

print("Se ha encontrado una mesa mas grande por lo que invitaremos mas personas\n")
guest_list.insert(0,'steve rogers')
guest_list.insert(2,'matt murdock')
guest_list.append('elon musk')

print(f"Numero de invitados que estaran en la cena: {len(guest_list)}")
message1 = f"Feliz navidad para ti {guest_list[0].title()}, ven a cenar"
message2 = f"Conozca sus limites señor {guest_list[1].title()} y no se termine la cena"
message3 = f"{guest_list[2].title()} esta invitado a la cena"
message4 = f"Bienvenido a la cena {guest_list[3].title()}"
message5 = f"Te esperamos en la cena de esta noche {guest_list[4].title()}"

print(message1)
print(message2)
print(message3)
print(message4)
print(message5)

print("Lo sentimos, solo podemos invitar a dos personas a la cena !!!\n")

no_invited1 = guest_list.pop(0)
no_invited2 = guest_list.pop(1)
no_invited3 = guest_list.pop(2)
no_invited4 = guest_list.pop(2)

print(f"Lo sentimos {no_invited1.title()}, pero no estas invitado")
print(f"Lo sentimos {no_invited2.title()}, pero no estas invitado")
print(f"Lo sentimos {no_invited3.title()}, pero no estas invitado")
print(f"Lo sentimos {no_invited4.title()}, pero no estas invitado\n\n")

print(f"Tu sigues invitado a la cena {guest_list[0].title()}")
print(f"Tu sigues invitado a la cena {guest_list[1].title()}")

del guest_list[0]
del guest_list[0]

print(guest_list)