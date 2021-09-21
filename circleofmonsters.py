t = int(input())
for t_ in range(t):
    n = int(input())
    cost = 0
    entry = 100000000000000
    firsta = 0
    lastb = 0

    for n_ in range(n):
        a,b = map(int,input().split())
        if n_==0:
            firsta = a
            lastb = b
        else:
            if a>lastb:
                cost+=a-lastb
                ent = lastb
            else:
                ent = a
            if ent<entry:
                entry=ent
            lastb=b
    
    a = firsta
    if a>lastb:
        cost+=a-lastb
        ent = lastb
    else:
        ent = a
    if ent<entry:
        entry=ent
        
    lastb=b
    
    print(cost+entry)



