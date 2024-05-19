#include <iostream>

using namespace std;

int main()
{
    cin.tie(0);
    cout.tie(0);
    ios_base::sync_with_stdio(false);

    int N, M;
    int A[100001];
    int i;

    cin >> N >> M;
    for (i = 0; i < N; i++)
        cin >> A[i];

    int j = 0;
    int k;
    int max_weight = 0;
    long current_weight;
    for (i = 0; i < N;) {
        i++;
        if ((i-j) > M)
            j++;

        current_weight = 0;
        for (k = j; k < i; k++)
            current_weight += A[k];

        if (max_weight < current_weight)
            max_weight = current_weight;
    }
    cout << max_weight;
    return 0;
}