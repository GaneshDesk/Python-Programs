

def NumReverse(n):

    rev = 0
    while(n > 0):
        dig = n % 10
        rev = rev*10+dig
        n = n//10
    print("The reverse of the number:", rev)


if __name__ == "__main__":

    n = int(input("Enter number: "))

    ret = NumReverse(n)

    print("The reverse of the number:", rev)
