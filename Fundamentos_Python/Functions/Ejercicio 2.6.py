def city_country(city_name, country_name):
    message = f"{city_name}, {country_name}"
    return message.title()

citycountry = city_country('lima','Peru')
print(citycountry)

citycountry = city_country('san lucas','mexico')
print(citycountry)

citycountry = city_country('tokyo','japon')
print(citycountry)


def make_album(name, title, number_song=None):
    album = {'artist_name' : name, 'album_title' : title}
    if number_song:
        album['songs'] = number_song
    return album

while True:
    print("\nPara salir, ingrese la letra x")
    nombre = input("Ingrese el nombre de su artista:")
    if(nombre == 'x'):
        break
    titulo_album = input("Ingrese el titulo del album:")
    if(titulo_album == 'x'):
        break
    album = make_album(nombre, titulo_album)
    print(album)