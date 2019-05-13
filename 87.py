import math
i,j=map(int,input().split())
l=[]
j=math.gcd(i,j)
l.append(k)
for p in range(0,len(l)):
  if(p==len(l)-1):
    print(l[p],end="")
  else:
    print(l[p],end=" ")
