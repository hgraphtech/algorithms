s,n = map(int,input().split())
d = []
for x in range(n):
    x,y = map(int,input().split())
    d.append((x,y))
d_sorted = sorted(d,key=lambda x:x[1], reverse=True)

dragon = 0

while len(d_sorted)>0 and dragon<len(d_sorted):

    if d_sorted[dragon][0]<s:
        s+=d_sorted[dragon][1]
        d_sorted.remove(d_sorted[dragon])
        dragon=0
    else:
        dragon+=1
        
if len(d_sorted)==0:
    print('YES')
else:
    print('NO')
    