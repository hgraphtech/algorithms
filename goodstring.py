t = int(input())
for t_ in range(t):

    s = input()

    best = 0
    for a in range(10):
        for b in range(10):
            c = 0
            state = 0
            for n in range(len(s)):
                if s[n]==str(a) and state==0:
                    c+=1
                    state=1
                elif s[n]==str(b) and state==1:
                    c+=1
                    state=0
            if a!=b and state==1:
                c-=1
            if c>best:
                best=c
    print(len(s)-best)
        
                