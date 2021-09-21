# dynamic programming

t = int(input())
for t_ in range(t):

    n = int(input())
    a = [int(x) for x in input().split()]

    if len(a)<=3:
        print(a[0])
    else:
        x,y,z,w = 10,10,a[0],a[0]+a[1]
        for i in range(2,n):
            x,y,z,w = z, min(x,z)+a[i], min(y,w), y+a[i]
        print(min(x,y,z,w))

        
