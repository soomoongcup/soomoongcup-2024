from collections import deque
from pathlib import Path
from typing import List

import math

from oj import Problem
from oj.validators import RangeValidator
from oj.validators import IntCoverageValidator
from oj.validators import TimeComplexityValidator

from solution import solve


DIR_PATH = Path(__file__).parent


PROBLEM_TITLE = 'idnum'

DIR_NAME = PROBLEM_TITLE
ZIP_NAME = PROBLEM_TITLE+'.zip'


def validate_default_limitations(N: int, A:List[int], M: int, Q: List[int], OUTPUT: List[str]) -> bool:
    # 문제에서 명시하는 기본 제약 조건들을 만족하는지 검사.
    assert len(A) == N
    assert len(Q) == M
    assert len(OUTPUT) == M
    for i in range(M):
        S, E = Q[i]
        assert 1 <= S
        assert S <= E
        assert E <= N
        assert OUTPUT[i] == 'YES' or OUTPUT[i] == 'NO'
    RangeValidator(lo=1, hi=2e3, raise_exception=True).validate(N)
    RangeValidator(lo=1, hi=1e5, raise_exception=True).validate_all(A)
    RangeValidator(lo=2, hi=1e6, raise_exception=True).validate(M)


def create_testcase(problem: Problem, testcase_id: str, N: int, A:List[int], M: int, Q: List[int], OUTPUT: List[str]):
    problem.testcases[testcase_id].input.write(f'{N}\n')
    problem.testcases[testcase_id].input.write(' '.join(map(str, A))+'\n')
    problem.testcases[testcase_id].input.write(f'{M}\n')
    for i in range(M):
        S, E = Q[i]
        problem.testcases[testcase_id].input.write(f'{S} {E}\n')
        problem.testcases[testcase_id].output.write(OUTPUT[i]+'\n')


def create_worst_non_palindrome(N: int) -> List[int]:
    A = [int(1e5)] * N
    # 펠린드롬이 아니게 만들어버리기ㅋ
    mid = N//2
    A[mid] = 2
    A[mid+1] = 3
    return A


if __name__ == '__main__':
    p = Problem(PROBLEM_TITLE)

    TESTCASE_ID = '1'
    N = 2000
    A = create_worst_non_palindrome(N)
    M = int(1e6)
    Q = [[1, 2000] for i in range(M)]
    OUTPUT = solve(N, A, M, Q)

    validate_default_limitations(N, A, M, Q, OUTPUT)

    create_testcase(p, TESTCASE_ID, N, A, M, Q, OUTPUT)


    print(f'{len(p.testcases)} testcases generated.')
    p.extract_as_dir(DIR_PATH / DIR_NAME)
    p.extract_as_zip(DIR_PATH / ZIP_NAME)
