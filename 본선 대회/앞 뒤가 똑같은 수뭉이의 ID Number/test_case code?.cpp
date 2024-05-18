#include <cstdio>
#include <stdio.h>
#include <iostream>

#define _CRT_SECURE_NO_WARNINGSS
#define REP(i, a, n) for(auto i = a; i <= n ; i++)
#define rep(i, a, n) for(auto i = a; i < n; i++)

using namespace std;

int board[2003];
int dp[2003][2003];
int n, m;

int main()
{
	freopen("input.txt", "r", stdin);
	freopen("output.txt", "w", stdout);

	cin >> n;
	REP(i, 1, n) cin >> board[i];

	REP(i, 1, n) dp[i][i] = 1;

	REP(j, 1, n) {
		REP(i, 1, n) {
			if (i >= j) break;
			if (board[i] == board[j] && dp[i + 1][j - 1] == 1) dp[i][j] = 1;
			if (board[i] == board[j] && j - i == 1) dp[i][j] = 1; // 차이가 1일 때 조심해야 함
		}
	}

	cin >> m;

	rep(i, 0, m) {
		int s, e;
		cin >> s >> e;
		if (dp[s][e]) cout << "YES" << endl;
		else cout << "NO" << endl;

	}

	fclose(stdin);
	fclose(stdout);
}
