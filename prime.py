# to check entered no is prime or not
#=============================
def prime(p):
    count=0
    for i in range(1,n):
        if n%i==0:
            count=count+1
    if count==1:
        print("prime number")
    else :
        print("not a prime number")
n=int(input())     
prime(n)
        
