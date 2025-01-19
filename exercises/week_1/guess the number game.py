# exercise 
#guess the number game
import random

number = random.randint(1,25)
print ("Welcome adventure to guess the number")
print("I'm thinking of a number between 1 to 25")
for playernumber in range(1,7): #Loop for 6 times 
    print("Take a guess")
    playernumber=int(input())
    if playernumber > number:
        print ("It is too high")
    elif playernumber < number:
        print ("it is too low")
    else:
        break #This is the right guess
if playernumber == number:
    print('Good job! You guessed my number in ' + str(playernumber) + ' guesses!')
else:
    print('Nope. The number I was thinking of was ' + str(number))