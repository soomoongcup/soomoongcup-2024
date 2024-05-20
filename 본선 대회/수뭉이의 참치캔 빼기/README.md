# 수뭉이의 참치캔 빼기(6pts)

출제자: 김남주

## 문제

<p style="margin-left: 0px;">수뭉이의 앞에 참치캔 $N$개가 $K$개의 더미로 아무렇게 쌓여있다.$N$개의 참치캔은 각각 $1$부터 $N$까지 번호가 매겨져 있다.</p><p><img src="http://test.timelimitexceeded.kr/public/upload/fea3cd1818.png" alt="Untitled" width="400" height="207.0000126342781" /></p><p>수뭉이는 참치캔을 정리하고자 번호의 역순으로 나열하려고 한다.</p><p>수뭉이는 각 더미에서 맨 위의 참치캔만 꺼낼 수 있고 번호의 역순으로 나열하기 위해서는 $N, N-1, N-2, ... , 2, 1$번 참치캔 순으로 꺼내야 한다.</p><p>참치캔을 번호의 역순으로 나열할 수 있는 프로그램을 만들어 보자.</p>

## 입력

<p style="margin-left: 0px;">첫째 줄에 참치캔의 개수 $N$ , 참치캔 더미의 수 $K$가 주어진다</p><p>둘째 줄부터 $2$ X $K$줄에 걸쳐서 각 더미의 참치캔 정보가 주어진다.<br />$i$번째 더미를 의미하는 첫 줄에는 더미에 쌓인 참치캔 수 $M_i$가 주어지고, 두 번째 줄에는 $M_i$ 개의 정수가 공백으로 구분되어 있다.</p><p>정수는 참치캔 번호이며, 위에 있는 참치캔 번호부터 주어진다.</p><h2>제한</h2><ul><li>1 ≤ $K$ ≤ $N$ ≤ 100,000</li><li>1 ≤ $M_i$</li><li>모든 $M_i$ 합은 $N$이다.</li><li>참치캔의 번호는 $1$부터 $N$까지의 정수가 한 번씩 등장한다</li></ul><table><thead><tr><th style="text-align: left;">2pts</th><th style="text-align: left;">4pts</th></tr></thead><tbody><tr><td>1 ≤ N ≤ 10</td><td>1 ≤ N ≤ 100,000</td></tr></tbody></table>

## 출력

<p><span style="color: rgb(51, 51, 51);">1부터N까지 순서의 역순으로 참치캔을 꺼낼 수 있다면</span><span style="color: rgb(235, 87, 87);">SUCCESS</span><span style="color: rgb(51, 51, 51);">를, 그렇지 않다면</span><span style="color: rgb(235, 87, 87);">FAIL</span><span style="color: rgb(51, 51, 51);">을 출력한다.</span><br /></p>


## 예제 입력 1

```
5 2
3
5 3 1
2
4 2
```

## 예제 출력 1

```
SUCCESS
```


## 예제 입력 2

```
4 2
2
2 3
2
4 1
```

## 예제 출력 2

```
FAIL
```