


a=[]
for i in range(0,n):
    elem=int(input("Enter element: "))
    a.append(elem)
    avg=sum(a)/n
print("Average of elements in the list",round(avg,2))


if __name__ == "__main__":

    n=int(input("Enter the number of elements to be inserted: "))

    ret = NumReverse(n)