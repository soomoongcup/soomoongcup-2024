# 미스터 추 (9pts)

출제자: 김남주

## 문제

<p style="margin-left: 0px;">수뭉이는 k개의 추를 가지고 있다.</p><p>수뭉이는 양팔저울을 한 번만 이용해 원하는 무게를 만들고 싶어 한다.</p><p>만약, 추가 3개이고 무게가 각각 (1, 2, 6)이면, 총 무게는 9이고, 양팔 저울을 한 번만 이용해 1부터 9사이 모든 정수에 대응하는 무게를 다음과 같이 구할 수 있다. 여기서 M은 구할 수 있는 무게이다.</p><table><thead><tr><th style="text-align: center;">M</th><th style="text-align: center;">1</th><th style="text-align: center;">2</th><th style="text-align: center;">3</th><th style="text-align: center;">4</th><th style="text-align: center;">5</th><th style="text-align: center;">6</th><th style="text-align: center;">7</th><th style="text-align: center;">8</th><th style="text-align: center;">9</th></tr></thead><tbody><tr><td style="text-align: center;"></td><td style="text-align: center;">1</td><td style="text-align: center;">2</td><td style="text-align: center;">1+2</td><td style="text-align: center;">6-2</td><td style="text-align: center;">6-1</td><td style="text-align: center;">6</td><td style="text-align: center;">6+1</td><td style="text-align: center;">6+2</td><td style="text-align: center;">6+2+1</td></tr></tbody></table><p>다른 예시로 추의 무게가 (1, 5, 7)이면 총 무게는 13이 된다. 양팔 저울을 한 번만 사용해 구할 수 있는 무게는 (1, 2, 3, 4, 5, 6, 7, 8, 11, 12, 13)이다. 이때 1부터 총 무게 사이의 수 중 9와 10에 대응하는 무게는 구할 수 없다.</p><p>k (3 ≤ k ≤ 13)개 추 무게 $g_1, g_2, ... , g_k$가 주어질 때, 1부터 ($g_i$의 총 합)에 있는 정수 중, 양팔 저울을 한번만 이용해 측정 불가능한 경우의 수를 구해보자</p><p><img alt="KakaoTalk_20240520_004812112.jpg" src="http://test.timelimitexceeded.kr/public/upload/af1623be2c.jpg" width="400.9875183105469" height="272.55959992622303" /></p>

## 입력

<p style="margin-left: 0px;">입력 첫 줄에 추의 개수를 의미하는 정수 $k$이 주어진다. 다음 줄 각 추의 무게를 나타내는 k개의 정수 $g_i$가 공백으로 구분된다.<br /></p><table><thead><tr><th style="text-align: left;">기본 테스트케이스 4개 (각 1pts)</th><th style="text-align: left;">특수 테스트케이스 1개 (5pts)</th></tr></thead><tbody><tr><td>$k (3 ≤ k ≤ 13)$<br /></td><td>$k = 13$</td></tr><tr><td>$1 ≤g_i≤ 200,000$</td><td>$g_i = 200,000$</td></tr></tbody></table>

## 출력

<p><span style="color: rgb(51, 51, 51);">1부터 총 무게 사이에 있는 정수 중, 양팔 저울을 한번만 이용해 측정할 수 없는 경우의 수를 출력한다.</span><br /></p><div class="simditor-table"></div>


## 예제 입력 1

```
3
1 5 7
```

## 예제 출력 1

```
2
```