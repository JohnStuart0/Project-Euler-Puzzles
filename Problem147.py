n=47
m=43
summ1, summ2, summ3 = 0, 0, 0
for i in range (1,n+1):
    summ1 += i*(n+1-i)
    
for j in range(1, m+1):
    summ2 += j*(m+1-j)

for i in range(4, 2*m+1, 2):
    for j in range(1, i-1):
        for k in range(j+1,i):
            summ3 += min(j,i-k)*(((2*n-i+j)//2)+1)*(((2*m-k)//2)+1)

for i in range(2*m+2, 2*n+1, 2):
    for j in range(1, 2*m):
        for k in range(j+1,2*m+1):
            summ3 += min(j,i-k)*(((2*n-i+j)//2)+1)*(((2*m-k)//2)+1)

for i in range(2*n+2, 2*n+2*m, 2):
    for j in range(i-2*n, 2*m):
        for k in range(j+1,2*m+1):
            summ3 += min(j,i-k)*(((2*n-i+j)//2)+1)*(((2*m-k)//2)+1)
            
            
print(summ1*summ2 +summ3)
