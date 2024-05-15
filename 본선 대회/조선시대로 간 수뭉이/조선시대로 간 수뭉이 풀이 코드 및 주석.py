# 1부터 10까지 받을 것임
# 배열 입력 받기
n = int(input())

# 받을 배열 생성
arr = []

# 배열에 입력 받기
for i in range(n):
    str = input()
    arr.append(list(str))

# 배열 돌리기
for i in range(n):
    for j in range(n):
        print(arr[j][n - 1 - i], end="")
    print() # 줄바꿈