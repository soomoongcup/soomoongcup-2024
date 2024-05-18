# Author: Hepheir <hepheir@gmail.com>

from pathlib import Path
import random

from oj import Problem
from oj.validators import RangeValidator
from oj.validators import TimeComplexityValidator


PROBLEM_TITLE = 'chosun-book'

DIR_PATH = Path(__file__).parent
DIR_NAME = PROBLEM_TITLE

ALPHABET_UPPER = ''.join([chr(i) for i in range(ord('A'), ord('Z')+1)])
ALPHABET_LOWER = ''.join([chr(i) for i in range(ord('a'), ord('z')+1)])
NUMERIC = ''.join([chr(i) for i in range(ord('0'), ord('9')+1)])

CHAR_POOL = ALPHABET_UPPER + ALPHABET_LOWER + NUMERIC


random.seed(1)

p = Problem(PROBLEM_TITLE)
n_validator = RangeValidator(lo=1, hi=100)


N = [1, 4, 10, 15, 16, 50, 81, 100]

TimeComplexityValidator(seconds=1, raise_exception=True).validate(max(N) ** 2)

assert n_validator.validate_all(N)

for i in range(len(N)):
    TESTCASE_ID = str(i+1)
    # 테스트케이스에서 사용할 데이터 생성
    grid = [[None] * N[i] for n in range(N[i])]
    for y in range(N[i]):
        for x in range(N[i]):
            c_idx = random.randint(0, len(CHAR_POOL)-1)
            grid[y][x] = CHAR_POOL[c_idx]

    # 입력 파일 작성
    p.testcases[TESTCASE_ID].input.write(f'{N[i]}\n')
    for y in range(N[i]):
        for x in range(N[i]):
            p.testcases[TESTCASE_ID].input.write(grid[y][x])
        p.testcases[TESTCASE_ID].input.write('\n')

    # 출력 파일 작성
    for y in range(N[i]):
        for x in range(N[i]):
            p.testcases[TESTCASE_ID].output.write(grid[x][N[i]-1-y])
        p.testcases[TESTCASE_ID].output.write('\n')

print(f'{len(p.testcases)} testcases generated.')
p.extract_as_dir(DIR_PATH / DIR_NAME)
