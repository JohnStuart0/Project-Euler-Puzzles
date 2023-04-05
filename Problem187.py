num=100000000
n=num//2
prime = [1 for i in range(n+1)] 
total=0
      
p = 2
while(p * p <= n): 
       
    # If prime[p] is not changed, then it is  
   # a prime 
    if (prime[p] == 1): 
           
        # Update all multiples of p 
        for i in range(p * p, n + 1, p): 
            prime[i] = 0
        
        # Count all doubles with p as largest factor
        #print(p,prime[2:p+1])
        total+=sum(prime[2:p+1])
        
    p += 1
    
while p*p<num:
    if prime[p]==1:
        #print(p,prime[2:p+1])
        total += sum(prime[2:p+1])
    p += 1 
    
while p<n:
    if prime[p]==1:
        #print(p,prime[2:num//p+1])
        total += sum(prime[2:num//p+1])
    p += 1 
print(total)