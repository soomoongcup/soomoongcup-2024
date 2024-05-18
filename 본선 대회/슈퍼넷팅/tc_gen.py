from pathlib import Path
from typing import List

from oj import Problem
from oj.validators import TimeComplexityValidator

from solution import solve


DIR_PATH = Path(__file__).parent


PROBLEM_TITLE = 'net'

DIR_NAME = PROBLEM_TITLE
ZIP_NAME = PROBLEM_TITLE+'.zip'


def read_google_testcase(file_in: str, file_ans: str):
    # 구글 데이터셋에서 입출력을 가져옴.
    with open(file_in, 'r') as fin, open(file_ans, 'r') as fout:
        T = int(fin.readline())
        N = [None] * T
        ADDRESS: List[List[str]] = [[] for _ in range(T)]
        OUTPUT: List[List[str]] = [[] for _ in range(T)]

        for t in range(T):
            N[t] = int(fin.readline())

            for i in range(N[t]):
                ADDRESS[t].append(fin.readline().strip())

            while fout.readable():
                cookie = fout.tell()
                if not (addr := fout.readline().strip()):
                    break
                elif addr == f'Case #{t+1}:':
                    # 테스트케이스의 시작
                    continue
                elif addr == f'Case #{t+2}:':
                    # 다음 테스트케이스의 시작을 마주치면 커서를 원복.
                    fout.seek(cookie)
                    break
                OUTPUT[t].append(addr)

        return T, N, ADDRESS, OUTPUT


if __name__ == '__main__':
    p = Problem(PROBLEM_TITLE)

    DATA_PATH_DICT = {
        '0': DIR_PATH / 'data' / 'sample',
        '1': DIR_PATH / 'data' / 'secret' / 'subtask1',
        '2': DIR_PATH / 'data' / 'secret' / 'subtask2',
    }

    for TESTCASE_ID in '12':
        DATA_PATH = DATA_PATH_DICT[TESTCASE_ID]

        #구글 데이터셋의 논리적인 구성은 맞다고 전제함.
        T, N, ADDRESS, OUTPUT = read_google_testcase(DATA_PATH/'1.in', DATA_PATH/'1.ans')

        if TESTCASE_ID == '1':
            # 1번 태케가 부실하므로 예제 입력도 이 곳에 병합시킴.
            # 부실한 부분: Prefix가 동일한 두 서브넷을 하나로 합치는 경우가 주어지지 않는다.
            DATA_PATH = DATA_PATH_DICT['0']
            T0, N0, ADDRESS0, OUTPUT0 = read_google_testcase(DATA_PATH/'1.in', DATA_PATH/'1.ans')
            T += T0
            N.extend(N0)
            ADDRESS.extend(ADDRESS0)
            OUTPUT.extend(OUTPUT0)

        p.testcases[TESTCASE_ID].input.write(f'{T}\n')
        for t in range(T):
            # 본인이 문제를 제대로 이해하고 있는게 맞는지 검증하기 위해,
            # 본인의 풀이와 구글의 답안이 일치하는지 검사.
            my_output = solve(ADDRESS[t])
            for i in range(len(OUTPUT[t])):
                assert OUTPUT[t][i] == my_output[i]
            assert len(OUTPUT[t]) == len(my_output)

            # 항상 서브넷의 개수가 더 적거나 같아야 한다.
            assert len(ADDRESS[t]) >= len(OUTPUT[t])

            # 테스트케이스 출력 작성
            p.testcases[TESTCASE_ID].input.write(f'{N[t]}\n')

            for i in range(N[t]):
                p.testcases[TESTCASE_ID].input.write(f'{ADDRESS[t][i]}\n')

            p.testcases[TESTCASE_ID].output.write(f'Case #{t+1}\n')
            for i in range(len(OUTPUT[t])):
                p.testcases[TESTCASE_ID].output.write(f'{OUTPUT[t][i]}\n')

        """
        Trie 자료구조를 사용하면 사용할 연산은 다음과 같다.
        1. Trie에 N개의 주소 추가 -> T = N x 32 x 2
            이진 트리에서 leaf노드를 찾아 내려감. -> T = 32 (비트 당 하나 씩의 노드 분기.)
            Leaf 노드 추가 후, 부모로 거슬러 올라오면서 (필요시) 서브넷 병합 -> T = 32
        2. 서브넷 조회
            pre-order dfs 방식의 완전 탐색
            서브넷의 루트일 경우 smart degeneration case로 최적화 가능
            즉, output 주소의 개수 만큼 노드를 방문한다고 생각.
            그런데 어차피 output 주소의 개수 상한은 N임.
        -> O(N log N) ... 은 아니고 그냥 O(N)

        수행 시간은 대충 이런 느낌 아닐까...
        T(N) = 32x2xN + 32xN = ... 대략 100 N
        """

        IPV4_BIT_LEN = 32
        TimeComplexityValidator(seconds=1, raise_exception=True).validate(100*sum(N))

        # TC#2는 O(N^2) 에는 안 풀렸으면 좋겠다.
        if TESTCASE_ID == '2':
            assert TimeComplexityValidator(seconds=1, raise_exception=False).validate(sum(N)**2) == False

    print(f'{len(p.testcases)} testcases generated.')
    p.extract_as_dir(DIR_PATH / DIR_NAME)
    p.extract_as_zip(DIR_PATH / ZIP_NAME)
