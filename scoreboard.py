digits = ["1110111", "0010010", "1011101", "1011011", "0111010", "1101011", "1101111", "1010010", "1111111", "1111011"]

n,k = map(int,input().split())

x = {}

for n_ in range(n):
    
    state = input()

    x[n_] = []
    min_dist = 10

    for t in range(9,-1,-1):
        
        target = digits[t]

        reachable = True
        dist = 0
        for i in range(7):
            if state[i]=="1" and target[i]=="0":
                reachable = False
            if state[i]=="0" and target[i]=="1":
                dist += 1
                
        if reachable==True:
            x[n_].append([t,dist])


# try a bf search

j = [0]*n
index = n-1

while index>=0:
    total = sum([x[i][j[i]][1] for i in range(n)])
    if total==k:
        s = [x[i][j[i]][0] for i in range(n)]
        ss = ''
        for z in s:
            ss+=str(z)
        print(ss)
        break
    reset = False
    while j[index]==len(x[index])-1:
        reset = True
        index-=1
        if index==-1:
            print(-1)
            break
    if index==-1:
        break
    j[index]+=1
    if reset == True:
        for z in range(index+1,n):
            j[z]=0
        index = n-1


