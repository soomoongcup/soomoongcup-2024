"""최백준님의 BOJ 1019 - 책 페이지 풀이를
K-진법에서 사용할 수 있도록 일반화 한 버전.

https://www.slideshare.net/Baekjoon/baekjoon-online-judge-1019?qid=9aa7818e-779e-499a-9c13-d2a5ac2ef8af&v=&b=&from_search=1
[최백준님의 BOJ 1019 - 책 페이지 풀이]
"""


import collections


def solve(N: int, K: int) -> int:
    digit_counter = collections.Counter()

    def count_digits(x: int, base: int, exp: int):
        # X 숫자를 base 진법으로 표기 시, 각 숫자가 등장한 횟수를 카운터에 더해준다.
        while x:
            digit_counter[x % base] += pow(base, exp)
            x //= base

    def solve_util(lo: int, hi: int, base:int, exp: int = 0):
        """lo 이상 hi 이하의 base 진법 수에서 base진법의 각 숫자가 등장한 횟수를 센다."""
        # lo의 base진법 1의 자리 수가 0이 될 때까지 1씩 증가시키며
        # count_digits() 함수를 통해 각 숫자마다 자리 수들을 본다.
        while lo % base and lo <= hi:
            count_digits(lo, base, exp)
            lo += 1
        # 이번엔 hi의 마지막 자리를 base의 가장 마지막 숫자로 맞춰준다.
        while (hi+1) % base and lo <= hi:
            count_digits(hi, base, exp)
            hi -= 1

        if lo > hi:
            # 모든 숫자를 다 보았다.
            return

        # lo와 hi 사이에는 각 숫자가 (hi-lo+1)base^exp 개 존재한다.
        lo //= base
        hi //= base

        diff = (hi - lo + 1)
        for i in range(base):
            digit_counter[i] += diff * pow(base, exp)

        # 다음 자릿 수를 보자
        solve_util(lo, hi, base, exp+1)

    solve_util(1, N, K)
    return ' '.join([str(digit_counter[i]) for i in range(K)])


if __name__ == '__main__':
    N, K = map(int, input().split())
    print(solve(N, K))
