
def SecondLast(inlist):
    
    inlist.sort()
    return inlist[n-2]

if __name__=='__main__':
    a=[]
    n=int(input("Enter number of elements:"))
    SecondLast(n)

    for i in range(1,n+1):
        b=int(input("Enter element:"))
        a.append(b)
        ret=SecondLast(a)
        print("Second LAst element is : ",ret)

