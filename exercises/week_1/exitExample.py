#exitExample
import sys
while True:
    print("type exit to stop the progam")
    res = input()
    if res == 'exit':
        sys.exit()
    print("you typed " + res + ".")
