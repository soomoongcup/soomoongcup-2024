from pathlib import Path
from typing import List

from oj import Problem
from oj import validators
from oj import constants

from solution import solve


DIR_PATH = Path(__file__).parent


PROBLEM_TITLE = 'k-base-book-pages'

DIR_NAME = PROBLEM_TITLE
ZIP_NAME = PROBLEM_TITLE+'.zip'


n_validator = validators.RangeValidator(lo=1, hi=int(1e9))
k_validator = validators.RangeValidator(lo=2, hi=16)


def validate_default_limitations(T: int, N: List[int], K: List[int], OUTPUT: List[str]) -> bool:
    assert len(N) == T
    assert len(K) == T
    assert len(OUTPUT) == T
    assert n_validator.validate_all(N)
    assert k_validator.validate_all(K)
    return True


def create_testcase(problem: Problem, testcase_id: str, T: int, N: List[int], K: List[int]):
    problem.testcases[testcase_id].input.write(f'{T}\n') # 첫 째줄에 테스트케이스의 개수 T가 주어진다.
    for i in range(T):
        problem.testcases[testcase_id].input.write(f'{N[i]} {K[i]}\n') # 각 테스트케이스 마다 하나의 줄에 N과 K가 공백을 기준으로 주어진다.
        problem.testcases[testcase_id].output.write(f'{solve(N[i], K[i])}\n') # 각 테스트케이스의 정답을 한 줄에 하나 씩 순서대로 출력한다.


if __name__ == '__main__':
    p = Problem(PROBLEM_TITLE)

    """
    테스트케이스 1

    int 만 사용해도 풀 수 있는 테스트케이스.
    모든 숫자를 하나하나 전부 세어도 풀 수 있는 문제.

    10진수만 다룬다.

    O(N \log_K N)
    """
    TESTCASE_ID = '1'
    N = [1, 7, 10, 11, 19, 333, 500, 957, 999, 1000, 98765, 111111, 1234567, 9999999, 152939251, 543212345, 1000000000]
    K = [10] * len(N)
    T = len(N)
    OUTPUT = [solve(n, k) for n, k in zip(N, K)]

    validate_default_limitations(T, N, K, OUTPUT)

    assert validators.int32_validator.validate_all(N)
    assert validators.int32_validator.validate_all(K)
    for i in range(T):
        output = list(map(int, OUTPUT[i].split()))
        assert len(output) == K[i]
        assert validators.int32_validator.validate_all(output)

    create_testcase(p, TESTCASE_ID, T, N, K)



    """
    테스트케이스 2

    int 만 사용해도 풀 수 있는 테스트케이스.
    모든 숫자를 하나하나 전부 세어도 풀 수 있는 문제.

    2~16진수를 모두 다룬다.

    O(N \log_K N)
    * \sum N = 약 5천만 이하
    """
    TESTCASE_ID = '2'
    N = [1, 7, 10, 11, 19, 333, 500, 957, 999, 1000, 98765, 111111, 1234567, 4599999] * 15
    K = []
    for base in range(2, 17):
        K.extend([base] * (len(N)//15))
    T = len(N)
    OUTPUT = [solve(n, k) for n, k in zip(N, K)]

    validate_default_limitations(T, N, K, OUTPUT)

    assert validators.RangeValidator(hi=int(5e8)).validate_one(sum(N)), f'{sum(N)} should be less than {int(5e8)}'
    assert validators.int32_validator.validate_all(N)
    assert validators.int32_validator.validate_all(K)
    for i in range(T):
        output = list(map(int, OUTPUT[i].split()))
        assert len(output) == K[i]
        assert validators.int32_validator.validate_all(output)

    create_testcase(p, TESTCASE_ID, T, N, K)



    """
    테스트케이스 3

    long long 은 사용해야 풀 수 있는 테스트케이스.
    모든 숫자를 하나하나 전부 세어서는 풀 수 없는 문제.
    자릿 수만 세어서 풀 수 있도록 하는 방법을 떠올리지 않으면 시간 초과를 받는다.

    2~16진수를 모두 다룬다.

    O(K \log_K N)
    """
    TESTCASE_ID = '3'
    N = [1, 7, 10, 11, 19, 333, 500, 957, 999, 1000, 98765, 111111, 1234567, 9999999, 152939251, 987656789, 1000000000] * 15
    K = []
    for base in range(2, 17):
        K.extend([base] * (len(N)//15))
    T = len(N)
    OUTPUT = [solve(n, k) for n, k in zip(N, K)]

    validate_default_limitations(T, N, K, OUTPUT)

    assert validators.int64_validator.validate_all(N)
    assert validators.int64_validator.validate_all(K)
    all_outputs = []
    for i in range(T):
        output = list(map(int, OUTPUT[i].split()))
        assert len(output) == K[i]
        assert validators.int64_validator.validate_all(output)
        all_outputs.extend(output)
    assert validators.RangeValidator(lo=constants.UINT32_MAX_VALUE).validate_any(all_outputs), f"{max(all_outputs)} is less than {constants.UINT32_MAX_VALUE}"

    create_testcase(p, TESTCASE_ID, T, N, K)


    print(f'{len(p.testcases)} testcases generated.')
    p.extract_as_dir(DIR_PATH / DIR_NAME)
    # p.extract_as_zip(DIR_PATH / ZIP_NAME)
