#include <cstdio>
#include <iostream>
using namespace std;

int main(){

    int t; scanf("%d", &t);

    for (int tc=0;tc<t;tc++) {

        int n; scanf("%d", &n);
        long long firsta, firstb; scanf("%lld %lld", &firsta, &firstb);
        long long lastb = firstb;
        long long cost = 0; long long entry = firsta;

        for (int i=1;i<n;i++) {

            long long a, b; scanf("%lld %lld", &a, &b);

            if (lastb >= a) {
                if (a<entry) {
                    entry = a;
                }
            }

            if (lastb < a) {
                cost += a - lastb;
                if (lastb<entry) {
                    entry = lastb;
                }
            }

            lastb = b;

        }

        long long a = firsta; long long b = firstb;

        if (lastb >= a) {
            if (a<entry) {
                entry = a;
            }
        }

        if (lastb < a) {
            cost += a - lastb;
            if (lastb<entry) {
                entry = lastb;
            }
        }

        cout << cost+entry << "\n";

    }

    return 0;
}



