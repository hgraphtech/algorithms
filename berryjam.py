t = int(input())
for t_ in range(t):
        
    n = int(input())
    at = input()
    a = [int(x) for x in at.split()]

    count = a.count(2)-a.count(1)

    if count==0:
        print(0)
        
    if count<0:
        # more 1s than 2s
        # trying to find 1s
        
        target = -count
        
        lc = 0
        blc = 0
        ll = []
        rc = 0
        brc = 0
        rl = []
        i = 0 
        lim = n
        found = False
        while i<lim:
            i+=1
            if a[n-i]==1:
                lc += 1
            else:
                lc -= 1
            if lc>blc:
                blc=lc
                ll.append(i)
            if a[n-1+i]==1:
                rc += 1
            else:
                rc -= 1
            if rc>brc:
                brc=rc
                rl.append(i)
            if blc+brc>=target:
                found = True
                # set lim to only go as far as needed

        best = 1000000
        if len(ll)>target-1:
            dist = ll[target-1]
        if dist<best:
            best=dist
        if len(rl)>target-1:
            dist = rl[target-1]
        if dist<best:
            best=dist
        for i in range(target):
            if len(ll)>i and len(rl)>target-i-2 and target-i-2>=0:
                dist = ll[i] + rl[target-i-2]
        if dist<best:
            best=dist
            
        print(best)
    
    if count>0:
        # more 2s than 1s
        # trying to find 2s
        
        target = count
        
        lc = 0
        blc = 0
        ll = []
        rc = 0
        brc = 0
        rl = []
        i = 0 
        lim = n
        found = False
        while i<lim:
            i+=1
            if a[n-i]==2:
                lc += 1
            else:
                lc -= 1
            if lc>blc:
                blc=lc
                ll.append(i)
            if a[n-1+i]==2:
                rc += 1
            else:
                rc -= 1
            if rc>brc:
                brc=rc
                rl.append(i)
            if blc+brc>=target:
                found = True
                # set lim to only go as far as needed

        best = 1000000
        if len(ll)>target-1:
            dist = ll[target-1]
        if dist<best:
            best=dist
        if len(rl)>target-1:
            dist = rl[target-1]
        if dist<best:
            best=dist
        for i in range(target):
            if len(ll)>i and len(rl)>target-i-2 and target-i-2>=0:
                dist = ll[i] + rl[target-i-2]
        if dist<best:
            best=dist
            
        print(best)
            
        