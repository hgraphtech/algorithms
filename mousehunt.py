n = int(input())
c = [int(x) for x in input().split()]
c.insert(0,0)
a = [int(x) for x in input().split()]
a.insert(0,0)

done = [0]*(n+1)
sol = 0
c_i = 0

for i in range(1,n+1):
    c_i+=2
    cost=0
    
    if done[i]!=0:
        continue
    
    while done[i]==0:
        done[i]=c_i
        i=a[i]
        
    if done[i]==c_i:
        # found a new cycle
        cost = c[i]
        while done[i]==c_i:
            done[i]+=1
            i=a[i]
            if c[i]<cost:
                cost=c[i]
        
    sol+=cost
    
print(sol)

