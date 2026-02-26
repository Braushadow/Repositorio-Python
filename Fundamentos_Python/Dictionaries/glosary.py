programming_words = {
    'if_statement': 'Is a condition that we stablished for something',
    'for_loop' : 'A way to repeat an event',
    'integer' : 'A number without decimal dot',
    'float' : 'A number that includes decimals',
    'format' : 'Is a way to make the code more simple'
    }


for key ,value in programming_words.items():
    print(f"\n{key.title()}: {value}")

rivers = {
    'nile' : 'egypt',
    'amazon' : 'south america',
    'yantze' : 'china',
}

for key,value in rivers.items():
    print(f"\nThe {key.title()} runs through {value.title()}")

for river in rivers.keys():
    print(river)

for country in rivers.values():
    print(country)


favorite_languages = {
    'jen' : 'python',
    'sarah' : 'C',
    'edward' : 'ruby',
    'phil' : 'python',
}

friends = ['phil','sarah']
people = ['braulio', 'jonny', 'homer','bart','lisa','marty','phil','charlie','sarah']

#language = favorite_languages['sarah'].title()
#print(f"Sara's favorite language is {language}\n")

#for name,language in favorite_languages.items():
 #   print(f"{name.title()}'s favorite language is {language.title()}!!\n")

#for name in favorite_languages.keys():
    #print(f"Hi {name.title()}!!")
    #if name in friends:
        #language = favorite_languages[name].title()
        #print(f"\t{name.title()} I see you love {language.title()}!")

#if 'erin' not in favorite_languages.keys():
 #   print("Erin, please take our poll")

#for name in sorted(favorite_languages.keys()):
 #   print(f"{name.title()}, thank you for taking the poll")

print("The following languages have been mentioned:")

for language in set(favorite_languages.values()):
    print(language.title())

for person in people:
    if person not in favorite_languages.keys():
        print(f"{person.title()}, you should take a favorite language")
    elif person in favorite_languages.keys():
        print(f"{person.title()}, thanks for being part of the poll")
