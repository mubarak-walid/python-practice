#exercise:if
#fun with if statement
print('What is your name?')
name = input()
print('How old are you?')
age= int(input())
if name == 'Hero':
    print('Welcome back boss')
    if age <21:
        print("So young. Did you go back in time?")
    elif age == 21 :
        print("You are full with energy")
    elif age > 2000:
        print("I have been wating for a long time")
    elif age == 100:
        print("You are little to old for me")
    else:
        print("it's not funny")
else:
    print("Get away of here")