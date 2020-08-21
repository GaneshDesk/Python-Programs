

def CheckPerfect(n):
    sum1 = 0
    for i in range(1, n):
        if(n % i == 0):
            sum1 = sum1 + i
    return sum1

if __name__=='__main__':
    num = int(input("Enter any number: "))

    ret=CheckPerfect(num)

    if (sum1 == n):
        print("The number is a Perfect number!")
    else:
        print("The number is not a Perfect number!")

