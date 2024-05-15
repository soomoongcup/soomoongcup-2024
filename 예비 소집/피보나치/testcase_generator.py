__about__ = """
피보나치 수 테스트케이스 생성기

- 소수를 입력으로 사용
- 2^64 를 벗어나지 않도록 값의 범위 조절
"""


from fast_fibo import fib
from pathlib import Path
import oj


def primes(n):
    # Sieve of Eratosthenes
    # https://en.wikipedia.org/wiki/Sieve_of_Eratosthenes
    sieve = [True] * (n+1)
    for p in range(2, n+1):
        if sieve[p]:
            for j in range(2*p, n+1, p):
                sieve[j] = False
            yield p


problem = oj.Problem('fibo')
dir_path = Path(__file__).parent

dir_name = problem.title
zip_name = problem.title+'.zip'

for id, prime in enumerate(primes(1000), start=1):
    x = prime
    y = fib(x)

    if y > oj.SIZE_T_INT64:
        # long long 을 사용해서 풀 수 있는 범위에서만 출제
        break

    tc = oj.TestCase()
    tc.input.from_args(x)
    tc.output.from_args(y)

    problem.add_testcase(tc)

print(f'{len(problem.testcases)} testcases generated.')
problem.extract_as_dir(dir_path / dir_name)
problem.extract_as_zip(dir_path / zip_name)
