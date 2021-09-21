t = int(input())
for t_ in range(t):
    n,k = map(int,input().split())
    x = int(k/n)
    r = k - n*x

    if r==0:
        print(0)
        k = 0
        for n_ in range(n):

            if k+x<=n:
                row = '0'*k+'1'*x+'0'*(n-k-x)
            if k+x>n:
                row = '1'*(k+x-n)+'0'*(n-x)+'1'*(n-k)
            print(row)
            k+=x
            if k>n:
                k-=n

    else:
        print(2)
        x+=1
        k = 0
        for n_ in range(n):

            if k+x<=n:
                row = '0'*k+'1'*x+'0'*(n-k-x)
            if k+x>n:
                row = '1'*(k+x-n)+'0'*(n-x)+'1'*(n-k)
            print(row)
            k+=x
            if k>n:
                k-=n
            r-=1
            if r==0:
                x-=1


