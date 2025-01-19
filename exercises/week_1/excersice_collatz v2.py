#excersice collatz Sequance v2 
def collatz(num):
    if num % 2 == 0:
        return num // 2
    else:
        return 3 * num +1

def main():
    try:
        num=int(input("Enter a positive intger"))
        if num <=0:
            print("invaild intger")
            return
        while num != 1:
            num =collatz(num)
            print (num)
    except ValueError:
        print("invaild input")
if __name__ == "__main__":
    main()

