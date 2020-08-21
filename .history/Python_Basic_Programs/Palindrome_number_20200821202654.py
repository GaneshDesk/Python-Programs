
# Program to Check if a Number is a Palindrome or Not

def CheckPalindrome(n):

    temp=n
    rev=0
    while(n>0):
        dig=n%10
        rev=rev*10+dig
        n=n//10
    if(temp==rev):
        print("The number is a palindrome!")
    else:
        print("The number isn't a palindrome!")

if __name__=='__main__':
    print("Check if a Number is a Palindrome or Not")
    n=int(input("Enter number:"))
