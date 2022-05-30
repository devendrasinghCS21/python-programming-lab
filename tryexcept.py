lst=[2,'34',None,'hello',True,12,0]
out=[]
for i in lst:
    try:
        r=1/int(i)
    except :
        out.append(None)
