for i in range(100,1000):
    s=0
    r=i
    while(r>0):
        p=r%10
        s=s+(p) ** 3
        r=r//10  
    if s==i:
        print(i)
