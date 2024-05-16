#include <bits/stdc++.h>
#define endl "\n"
#define FAST_IO ios_base::sync_with_stdio(false); cin.tie(0), cout.tie(0)

using namespace std;

int board[2003];
int dp[2003][2003];
int n, m;

int main() {
	FAST_IO;

	cin >> n;
	for (int i = 1; i <= n; i++) cin >> board[i];

	for (int i = 1; i <= n; i++) dp[i][i] = 1; // 범위가 같을 땐 무조건 회문이다.

	for (int j = 1; j <= n; j++) {
		for (int i = 1; i <= n; i++) {
			if (i >= j) break; // i==j는 볼 필요 없고 i > j이면  이 범위는 정수 범위가 아니다
			if (board[i] == board[j] && dp[i + 1][j - 1] == 1) dp[i][j] = 1;
			// 끝 수가 같고 이전 애들 회문이라면 나도 회문이다
			if (j - i == 1 && board[i] == board[j]) dp[i][j] = 1; // 차이가 1일 때 조심
			// 내 이전이 존재하지 않고 범위 크기가 2일 때 조심해야한다.(한번 더 검사 필요)
		}
	}

	cin >> m;

	for (int i = 0; i < m; i++) {
		int s, e;
		cin >> s >> e;
		if(dp[s][e]) cout << "YES" << endl;
		else cout << "NO" << endl;
	}
	
	
}