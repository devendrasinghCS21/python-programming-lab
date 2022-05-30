# cook your dish here
t=int(input())
while(t):
    N,X,P=map(int,input().split())
    if X*3-(N-X)>=P:
        print("PASS")
    else:
        print("FAIL")
    t=t-1
