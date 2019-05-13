str1=input()
k=[]
for i in range(0,len(str1)):
    k.append(ord(str1[i]))
k.sort()
for i in k:
    print(chr(i),end='')
