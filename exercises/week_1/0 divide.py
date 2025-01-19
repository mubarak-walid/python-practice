# exercise: try and except  
#0 divide
def spam(divideby):
    try:
        return 42 / divideby
    except ZeroDivisionError:
        print('Error: Invalid argument.')
    
print(spam(1))
print(spam(5))
print(spam(0))
print(spam(42))
