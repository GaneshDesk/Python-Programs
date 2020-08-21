
# program to calculate sum of digit of given number.


def SumFunction(n):
    tot = 0
    while(n > 0):
        dig = n % 10
        tot = tot+dig
        n = n//10

    return tot


if __name__ == '__main__':
    print("Program for sum of digit of given number")

    n = int(input("Enter a number:"))

    ret = SumFunction(n)

    print("The total sum of digits is:", ret)
