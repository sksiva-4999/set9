str12=input()
s=[]
for i in str12:
    s.append(i)
k=set(s)
n1=len(s)
n2=len(k)
if n1-n2==0:
  print("Yes")
else:
  print("No") 
