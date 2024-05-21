#include <stdio.h>

#define MAX_K 16

typedef unsigned long long u_int64_t;

u_int64_t counter[MAX_K];
u_int64_t N, K;


void count(u_int64_t n) {
    while (n)
    {
        counter[n % K]++;
        n /= K;
    }
}

int main()
{

    int T;
    scanf("%d ", &T);
    for (int t = 0; t < T; t++) {
        scanf("%d %d ", &N, &K);

        // counter 초기화
        for (int i = 0; i < K; i++) counter[i] = 0;

        // 각 숫자 세기
        for (int n = 1; n <= N; n++) {
            count(n);
        }

        for (int i = 0; i < K; i++) {
            printf("%d", counter[i]);

            // 마지막 줄을 제외하고만 공백 출력
            if (i < K-1) printf(" ");
        }
        printf("\n");
    }
    return 0;
}