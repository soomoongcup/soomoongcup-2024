from pathlib import Path
from typing import List

import random

from oj import Problem
from oj.validators import RangeValidator
from oj.validators import IntCoverageValidator
from oj.validators import TimeComplexityValidator

from solution import solve


DIR_PATH = Path(__file__).parent


PROBLEM_TITLE = 'eskr'

DIR_NAME = PROBLEM_TITLE
ZIP_NAME = PROBLEM_TITLE+'.zip'


random.seed(1)


def create_testcase(p: Problem, TESTCASE_ID: str, N: int, M: int, A: List[int], OUTPUT: int):
    # 문제의 조건에서 제시하는 바를 만족하는지 검사.
    RangeValidator(lo=1, hi=1e5).validate(N)
    RangeValidator(lo=1, hi=1e6).validate(M)
    RangeValidator(lo=1, hi=200).validate_all(A)
    # 테스트케이스를 문제에 추가
    p.testcases[TESTCASE_ID].input.write(f'{N} {M}\n')
    for i in range(N):
        p.testcases[TESTCASE_ID].input.write(f'{A[i]}\n')
    p.testcases[TESTCASE_ID].output.write(f'{OUTPUT}\n')


if __name__ == '__main__':
    p = Problem(PROBLEM_TITLE)

    """테스트케이스 1

    2중 반복문을 이용하여 풀 수 있는 테스트케이스
    O(NM) 으로 Naive 하게 에스컬레이터에 가해지는 하중을 계산한다.
    """
    TESTCASE_ID = '1'
    N = 100
    M = 80
    A = [random.randint(20, 200) for i in range(N)]
    OUTPUT = solve(N, M, A)

    TimeComplexityValidator(seconds=0.5, raise_exception=True).validate(N*M)
    IntCoverageValidator(allow_int32=True).validate(sum(A), OUTPUT)

    create_testcase(p, TESTCASE_ID, N, M, A, OUTPUT)


    """테스트케이스 2

    2중 반복문을 이용하면 시간 초과를 받는 테스트케이스
    큐나 투 포인터를 활용하여 O(N) 으로 해결해야 한다.
    """
    TESTCASE_ID = '2'
    N = 100000
    M = 30000
    A = [random.randint(1, 1000) for i in range(N)]
    OUTPUT = solve(N, M, A)

    assert TimeComplexityValidator(seconds=0.5, raise_exception=False).validate(N*M) == False
    TimeComplexityValidator(seconds=0.5, raise_exception=True).validate(N)
    IntCoverageValidator(allow_int32=True).validate(500*M, OUTPUT)

    create_testcase(p, TESTCASE_ID, N, M, A, OUTPUT)


    print(f'{len(p.testcases)} testcases generated.')
    p.extract_as_dir(DIR_PATH / DIR_NAME)
    p.extract_as_zip(DIR_PATH / ZIP_NAME)


    PROBLEM_SAMPLE_TITLE = 'eskr-sample'

    p_sample = Problem(PROBLEM_SAMPLE_TITLE)

    TESTCASE_ID = '1'
    N, M = 6, 4
    A = [58, 113, 77, 66, 180, 45]
    OUTPUT = solve(N, M, A)
    create_testcase(p_sample, TESTCASE_ID, N, M, A, OUTPUT)

    p_sample.extract_as_dir(DIR_PATH / PROBLEM_SAMPLE_TITLE)
