t = int(input())

for t_ in range(t):

    n,k = map(int,input().split())
    s = input()

    gaps = [len(x) for x in s.split('W') if len(x)>0]
    runs = [len(x) for x in s.split('L') if len(x)>0]

    # trim ends
    ends = 0
    if s[0]=='L':
        ends+=gaps[0]
        del gaps[0]
    if s[-1]=='L' and len(gaps)>0:
        ends+=gaps[-1]
        del gaps[-1]

    gaps.sort()


    i=0
    while k>0 and i<len(gaps):
        if gaps[i]<=k:
            k-=gaps[i]
            gaps[i] = 0
            i+=1
        else:
            gaps[i]-=k
            k=0
        
    new_gaps = [g for g in gaps if g>0]

            
    if k>0 and ends>0:
        if ends>=k:
            ends-=k
        else:
            ends=0

    score = (n-sum(new_gaps)-ends)*2 - (len(new_gaps)+1)
    score = max(score,0)
    print(score)

