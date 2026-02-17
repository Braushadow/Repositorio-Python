'''users = ['braulio','paul','leto','admin','contra']

for user in users:
    if user == 'admin':
        print("Hello admin, would you like to see a status review?")
    else:
        print(f"Helo {user}, thanks for login again")
else:
    print("We need to find some users!!")'''

current_users = ['braulio','jose','juan','alexis','cris']
current_users2 = ['Braulio','BRAULIO','Jose','JOSE','Juan','JUAN','Alexis','ALEXIS','cris','CRIS']
new_users = ['braulio','gina','eli','cris','jonny']

for user in new_users:
    if user in current_users or user in current_users2:
        print("You need to enter a new nickname!!")
    else:
        print(f"The username {user} is available")

numbers = [1,2,3,4,5,6,7,8,9]
for number in numbers:
    if number == 1:
        print(f"{number}st")
    elif number == 2:
        print(f"{number}nd")
    elif number == 3:
        print(f"{number}rd")
    else:
        print(f"{number}th")
