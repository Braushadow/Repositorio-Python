messages = ['A leap of faith',
            'Great power comes with great responsability',
            'Why do we fall?']
sended_messages = []

def print_messages(messages,sended_messages):
    while messages:
        current_message = messages.pop()
        print(f"Message: {current_message}")
        sended_messages.append(current_message)

def show_sended_messages(sended_messages):
    print("\nThe following messages were sended")
    for message in sended_messages:
        print(message)

print_messages(messages[:],sended_messages)
show_sended_messages(sended_messages)

print(messages)
print(sended_messages)