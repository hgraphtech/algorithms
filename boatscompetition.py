t = int(input())


def countpairs(s):
    
    w = ws.copy()
    
    pairs = 0
    while len(w)>1:

        a = w[0]
        target = s-w[0]
        w.remove(a)
        if target in w:
            pairs += 1
            w.remove(target)
            #print(a,target,w)
            
    return pairs


for t_ in range(t):
    n = int(input())
    ws = [int(i) for i in input().split()]

    s_max = max(ws)*2
    max_pairs = 0

    for s in range(s_max+1):
        p = countpairs(s)
        if p>max_pairs:
            max_pairs=p
        if max_pairs == int(n/2):
            break
       
    print(max_pairs)