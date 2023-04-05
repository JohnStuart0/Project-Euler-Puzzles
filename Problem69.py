mynum=6
maxprod=3
for num in range(5,100001):
    a=[]
    for j in range(2,num+1):
        if num%j==0:
            a.append(j)
            a.append(num//j)
            break
    index=1
    while a[-1]!=1:
        for j in range(a[index-1],a[index]+1):
            if a[index]%j==0:
                if j!=a[index-1]:
                    a.append(a[index]//j)
                    a[index]=j
                    index+=1
                else:
                    a[index]=a[index]//j
                break
    prod=1
    for i in a:
        if i!=1:
            prod*=i/(i-1)
    if prod>maxprod:
        maxprod=prod
        mynum=num
print(mynum,maxprod)