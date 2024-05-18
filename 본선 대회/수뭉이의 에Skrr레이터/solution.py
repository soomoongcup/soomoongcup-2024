# 큐를 쓰기위해 필요한 내장 모듈 (혹은 직접 큐를 구현해도 된다)
from typing import List


def solve(N: int, M: int, A: List[int]) -> int:
    """
    사람의 수 N, 에스컬레이터의 길이 M, 사람들의 몸무게 A를 입력받아,
    에스컬레이터가 버텼던 최대 중량을 계산한다.
    """
    max_load = 0
    current_load = 0

    i = 0 # queue front index (새로운 노드가 추가 될 위치)
    j = 0 # queue rear index (다음번에 제거 될 노드의 위치)

    while i < N:
        # 사람이 탑승한다.
        current_load += A[i]
        i += 1

        if (i-j) > M:
            # 사람이 내린다.
            current_load -= A[j]
            j += 1

        # 최대 하중을 갱신한다.
        if max_load < current_load:
            max_load = current_load

    return max_load
