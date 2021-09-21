t = int(input())
for t_ in range(t):
        
    s = input()
    keys = 'abcdefghijklmnopqrstuvwxyz'
    k = ''

    for x in s:
        ok = False
        if k=='':
            k+=x
            i=0
            ok = True
        else:
            if x not in k:
                if i==0:
                    k=x+k
                    i=0
                    ok = True
                elif i==len(k)-1:
                    k=k+x
                    i+=1
                    ok = True
            else:
                if i>0:
                    if k[i-1]==x:
                        i-=1
                        ok = True
                if i<len(k)-1:
                    if k[i+1]==x:
                        i+=1
                        ok = True
        if ok == False:
            print('NO')
            break
            
    if ok == True:
        for x in keys:
            if x not in k:
                k+=x
        print('YES')
        print(k)
        
