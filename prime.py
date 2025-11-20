n=int(input("enter the number: "))
def prime(n):
    for i in range(2,n):
        if n%i==0:
            return False
        return True

if prime(n):
    print("prime")
else:
    print("not prime")
