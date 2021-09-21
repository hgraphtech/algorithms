t = int(input())

for t_ in range(t):
    n = int(input())
    
    s = int((n-1)/2)
    total = 0
    for x in range(1,s+1):
        total += x*(8*x)    
    
    print(total)



