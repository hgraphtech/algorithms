
#include <cstdio>
#include <vector>
#include <algorithm>

int main(){

    long n; scanf("%ld", &n);
    std::vector<long> c(n + 1, 0); for(long p = 1; p <= n; p++){scanf("%ld", &c[p]);}
    std::vector<long> a(n + 1, 0); for(long p = 1; p <= n; p++){scanf("%ld", &a[p]);}
    
    std::vector<long> done(n + 1, 0);
    long sol(0);
    long ci(0);
    long cost(0);
   

    for(long i = 1; i <= n; i++){
        if(done[i]!=0){continue;}

        ci+=2;
        cost=0;

        while(done[i]==0){
            done[i]=ci;
            i=a[i];
        }

        if (done[i]==ci){
            cost=c[i];
            while (done[i]==ci){
                done[i]+=1;
                i=a[i];
                if (c[i]<cost){
                    cost=c[i];
                }
            }
        }

        sol+=cost;
    }

    printf("%ld\n", sol);

    return 0;
}