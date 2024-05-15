__about__ = """
피보나치 수 테스트케이스 생성기

- 소수를 입력으로 사용
- 2^64 를 벗어나지 않도록 값의 범위 조절
"""


from fast_fibo import fib
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

for id, prime in enumerate(primes(200), start=1):
    tc = oj.TestCase(
        id=str(id),
        input=str(prime),
        output=str(fib(prime))
    )

    if int(tc.output) > oj.LONG_LONG_SIZE:
        break

    problem.add_testcase(tc)

print(f'{len(problem.testcases)} testcases generated.')
problem.extract_as_zip()
