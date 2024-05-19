from typing import Dict, List, Iterable, Iterator, Tuple
import sys


sys.setrecursionlimit(int(1e9))


def solve(N: int, A: List[int], M: int, Q: Iterable[int]):
    cache: Dict[Tuple[int, int], bool] = {}

    def is_palindrome(S: int, E: int) -> bool:
        if S >= E:
            return True
        if (S, E) not in cache:
            cache[S,E] = A[S] == A[E] and is_palindrome(S+1, E-1)
        return cache[S,E]

    output = []
    for s, e in Q:
        output.append('YES' if is_palindrome(s-1, e-1) else 'NO')
    return output


def get_queries(M: int) -> Iterator[Tuple[int, int]]:
    for i in range(M):
        S, E = map(int, input().split())
        yield S, E



if __name__ == '__main__':
    input = sys.stdin.readline

    N = int(input())
    A = list(map(int, input().split()))
    M = int(input())
    Q = get_queries(M)
    OUTPUT = solve(N, A, M, Q)
    sys.stdout.write('\n'.join(OUTPUT)+'\n')


# if __name__ == '__main__':
#     import glob
#     import os

#     for file in glob.glob(os.path.dirname(__file__)+'/**/*.in'):
#         input = open(file, 'r').readline

#         N = int(input())
#         A = list(map(int, input().split()))
#         M = int(input())
#         Q = get_queries(M)
#         OUTPUT = solve(N, A, M, Q)
#         sys.stdout.write('\n'.join(OUTPUT)+'\n')
