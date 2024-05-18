from pathlib import Path
from typing import List

import math

from oj import Problem
from oj.validators import RangeValidator
from oj.validators import IntCoverageValidator
from oj.validators import TimeComplexityValidator

from solution import solve


DIR_PATH = Path(__file__).parent


PROBLEM_TITLE = 'kbook'

DIR_NAME = PROBLEM_TITLE
ZIP_NAME = PROBLEM_TITLE+'.zip'


def validate_default_limitations(T: int, N: List[int], K: List[int], OUTPUT: List[str]) -> bool:
    # 문제에서 명시하는 기본 제약 조건들을 만족하는지 검사.
    assert len(N) == T
    assert len(K) == T
    assert len(OUTPUT) == T
    for i in range(T):
        assert len(OUTPUT[i].split()) == K[i]
    RangeValidator(lo=1, hi=1e9, raise_exception=True).validate_all(N)
    RangeValidator(lo=2, hi=16, raise_exception=True).validate_all(K)
    return True


def create_testcase(problem: Problem, testcase_id: str, T: int, N: List[int], K: List[int]):
    problem.testcases[testcase_id].input.write(f'{T}\n') # 첫 째줄에 테스트케이스의 개수 T가 주어진다.
    for i in range(T):
        problem.testcases[testcase_id].input.write(f'{N[i]} {K[i]}\n') # 각 테스트케이스 마다 하나의 줄에 N과 K가 공백을 기준으로 주어진다.
        problem.testcases[testcase_id].output.write(f'{solve(N[i], K[i])}\n') # 각 테스트케이스의 정답을 한 줄에 하나 씩 순서대로 출력한다.


if __name__ == '__main__':
    p = Problem(PROBLEM_TITLE)

    """
    테스트케이스 1 (배점 20점)

    int 만 사용해도 풀 수 있는 테스트케이스.
    모든 숫자를 하나하나 전부 세어도 풀 수 있는 문제.

    10진수만 다룬다.

    O(N \log_K N)
    * \sum N = 약 5천만 이하
    """
    testcase_id = '1'
    shared_inputs = [1, 7, 10, 11, 19, 333, 500, 957, 999, 1000, 98765, 111111, 1234567, 4992751]
    bases = [10]

    N = shared_inputs * len(bases)
    K = []
    for base in bases:
        K.extend([base] * len(shared_inputs))
    T = len(N)
    OUTPUT = [solve(n, k) for n, k in zip(N, K)]

    validate_default_limitations(T, N, K, OUTPUT)

    TimeComplexityValidator(seconds=1, raise_exception=True).validate(sum(N) * math.log10(sum(N)))
    IntCoverageValidator(allow_int32=True, raise_exception=True).validate_all(N)
    IntCoverageValidator(allow_int32=True, raise_exception=True).validate_all(K)
    for i in range(T):
        output = list(map(int, OUTPUT[i].split()))
        IntCoverageValidator(allow_int32=True, raise_exception=True).validate_all(output)

    create_testcase(p, testcase_id, T, N, K)



    """
    테스트케이스 2 (배점 30점)

    int 만 사용해도 풀 수 있는 테스트케이스.
    모든 숫자를 하나하나 전부 세어도 풀 수 있는 문제.

    2~16진수를 모두 다룬다.

    O(N \log_K N)
    * \sum N = 약 5천만 이하
    """
    testcase_id = '2'
    shared_inputs = [1, 7, 10, 11, 19, 333, 500, 957, 999, 1000, 98765]
    bases = [*range(2, 17)]

    N = shared_inputs * len(bases)
    K = []
    for base in bases:
        K.extend([base] * len(shared_inputs))
    T = len(N)
    OUTPUT = [solve(n, k) for n, k in zip(N, K)]

    validate_default_limitations(T, N, K, OUTPUT)

    TimeComplexityValidator(seconds=1, raise_exception=True).validate(sum(N) * math.log(sum(N), min(K)))
    IntCoverageValidator(allow_int32=True, raise_exception=True).validate_all(N)
    IntCoverageValidator(allow_int32=True, raise_exception=True).validate_all(K)
    for i in range(T):
        output = list(map(int, OUTPUT[i].split()))
        IntCoverageValidator(allow_int32=True, raise_exception=True).validate_all(output)

    create_testcase(p, testcase_id, T, N, K)



    """
    테스트케이스 3 (배점 50점)

    long long 은 사용해야 풀 수 있는 테스트케이스.
    모든 숫자를 하나하나 전부 세어서는 풀 수 없는 문제.
    자릿 수만 세어서 풀 수 있도록 하는 방법을 떠올리지 않으면 시간 초과를 받는다.

    2~16진수를 모두 다룬다.

    O(K \log_K N)
    """
    testcase_id = '3'
    shared_inputs = [1, 7, 10, 11, 19, 333, 500, 957, 999, 1000, 98765, 111111, 1234567, 9999999, 152939251, 543212345, 987656789, 1000000000]
    bases = [*range(2, 17)]

    N = shared_inputs * len(bases)
    K = []
    for base in bases:
        K.extend([base] * len(shared_inputs))
    T = len(N)
    OUTPUT = [solve(n, k) for n, k in zip(N, K)]

    validate_default_limitations(T, N, K, OUTPUT)

    TimeComplexityValidator(seconds=1, raise_exception=True).validate(sum(K) * math.log(sum(N), min(K)))
    IntCoverageValidator(allow_int64=True, raise_exception=True).validate_all(N)
    IntCoverageValidator(allow_int64=True, raise_exception=True).validate_all(K)
    all_outputs = []
    for i in range(T):
        output = list(map(int, OUTPUT[i].split()))
        IntCoverageValidator(allow_int64=True, raise_exception=True).validate_all(output)
        all_outputs.extend(output)
    # int32를 벗어난 범위의 int64는 적어도 하나 이상 있어야 함.
    IntCoverageValidator(allow_int64=True, allow_int32=False, raise_exception=True).validate_any(all_outputs)

    create_testcase(p, testcase_id, T, N, K)


    print(f'{len(p.testcases)} testcases generated.')
    p.extract_as_dir(DIR_PATH / DIR_NAME)
    p.extract_as_zip(DIR_PATH / ZIP_NAME)
