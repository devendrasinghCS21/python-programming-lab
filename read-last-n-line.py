f=open(r"cpp.c\obj\Debug\hello.txt","r")
n=int(input())
t=f.readlines()[-n:]
print(*t,sep="\n")
f.close()
