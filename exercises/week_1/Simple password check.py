#exercises : while loop
#Simple password check
while True:
    print('who are you?')
    name =input()
    if name != 'Mob':
        continue
    print("Hello, Mob. What is your password (It's a goat)" )
    passwd = input()
    if passwd == "goatsowrd":
        break
print("Access granted.")