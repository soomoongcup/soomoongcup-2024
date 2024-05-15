FIBO_MAT = [
    [1,1],
    [1,0],
]


def matpow(mat: list[list[int]], exp: int):
    if exp != 1:
        mat = matpow(mat, exp//2)
        mat = matmul(mat, mat)
        if exp % 2 == 1:
            mat = matmul(mat, FIBO_MAT)
    return mat


def matmul(m1: list[list[int]], m2: list[list[int]]):
    return [
        [m1[0][0]*m2[0][0] + m1[0][1]*m2[1][0], m1[0][0]*m2[0][1] + m1[0][1]*m2[1][1]],
        [m1[1][0]*m2[0][0] + m1[1][1]*m2[1][0], m1[1][0]*m2[0][1] + m1[1][1]*m2[1][1]],
    ]


def fib(n: int) -> int:
    if n == 0:
        return 0
    if n == 1:
        return 1
    return matpow(FIBO_MAT, n-1)[0][0]
