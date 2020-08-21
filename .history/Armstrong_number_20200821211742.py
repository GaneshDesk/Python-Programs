

def CheskArmstrong(n):
    a = list(map(int, str(n)))
    b = list(map(lambda x: x**3, a))
    if(sum(b) == n):
        return 1
    else:
        return 0


if __name__ == '__main__':
    n = int(input("Enter any number: "))

    ret = CheskArmstrong(n)
    if(ret == 1):
        print("The number is an armstrong number. ")
    else:
        print("The number isn't an arsmtrong number. ")
