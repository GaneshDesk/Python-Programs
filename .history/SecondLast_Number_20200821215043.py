
def SecondLast(n):
    
    
    
    print("Second largest element is:",a[n-2])


if __name__=='__main__':
    a=[]
    n=int(input("Enter number of elements:"))
    SecondLast(n)

    for i in range(1,n+1):
        b=int(input("Enter element:"))
        a.append(b)
        a.sort()
