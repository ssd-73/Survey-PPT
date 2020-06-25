import math
n=int(input())
for i in range(0,n):
s=3         
    a,b,l,d,e,f=input().split()   
    l=int(c)    
    d=int(d)   
    e=int(e)   
    f=int(f)   
    l=math.log(l,10)
    if a=='N': 
        v=0
    else:
        v=1
    if b=='N':   
        p=0.5
    else:
        p=1
    if e==0:    
        hr=0.3
    else:
        hr=e/f
    if d==1:    
        s=s+v+p*(hr+l)
    else:
        s=s-v-p*(hr+l)
print(s)   
