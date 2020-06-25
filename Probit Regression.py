a1=[]
n=int(input())
for i in range(0,n):
a,b=input().split()
b=int(b)         
b1=[]
b1.append(a)  
b1.append(b)
a1.insert(i,b1)
print('0 0')
for i in range(1,n):
s1=0                
s2=0                
for j in range(0,i):
    if a1[i][0]==a1[j][0]:
        if a1[j][1]>=4:
            s1+=1
        else:
            s2+=1
print(s1,s2)
