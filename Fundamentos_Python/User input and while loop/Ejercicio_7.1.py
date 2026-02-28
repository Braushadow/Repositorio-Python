requested_car = input("What kind of car are you looking for? ")
print(f"\nLet me see if I can find you a {requested_car}")

people = int(input("\nHow many people are in your dinner group? "))

if people >= 8:
    print("I'm so sorry, but you'll need to wait for a table")

else:
    print("Your table is ready")

multiple_of_ten = int(input("\nPlease give me a number: "))

if multiple_of_ten % 10 == 0:
    print("\nYour number is multiple of ten")
else:
    print("Your number is NOT multiple of ten")