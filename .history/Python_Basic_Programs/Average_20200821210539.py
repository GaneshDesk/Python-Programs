

def Average(a):
    for i in range(0, n):
        elem = int(input("Enter element: "))
        a.append(elem)
        avg = sum(a)/n
    return round(avg, 2)


if __name__ == "__main__":

    n = int(input("Enter the number of elements to be inserted: "))
    num = []

    ret = Average(num)

    print("Average of number is : ", ret)
