f=open("hello.txt","r")
print(max(f.read().split(),key=len)
f.close()
