#include <bits/stdc++.h>
using namespace std;

int k, sum, cnt;
int board[14];
vector<bool> visited (13 * 200'000 + 5);

void func(int idx, int weight) {

	if (idx == k) {
		if (weight > 0) {
			visited[weight] = true;
		}
		return;
	}

	func(idx + 1, weight); // 놓지 X
	func(idx + 1, weight + board[idx]); // 같은쪽에 놓은 경우
	func(idx + 1, weight - board[idx]); // 반대편에 놓은 경우
}


int main() {
	FAST_IO;

	cin >> k;
	for (int i = 0; i < k; i++) {
		cin >> board[i];
		sum += board[i];
	}

	func(0, 0); // index, weight

	for(int i = 1; i <= sum; i++) { 
		if (!visited[i]) cnt++;
	}
	cout << cnt;


}
