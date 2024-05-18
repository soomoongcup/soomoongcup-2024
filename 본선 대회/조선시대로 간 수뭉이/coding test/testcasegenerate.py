# 조선 시대 책 읽기 테스트 케이스 made by 준환

import random

# 제한 값 설정
MIN_VALUE = 1
MAX_VALUE = 100

# 제한 값 
def value_limit(n):
    return MIN_VALUE <= n <= MAX_VALUE

# 랜덤 시드
random.seed(1)

# ord 값
strs = ""

for i in range(ord('a'), ord('z') + 1):
    strs += chr(i)

for i in range(ord('A'), ord('Z') + 1):
    strs += chr(i)

for i in range(ord('0'), ord('9') + 1):
    strs += chr(i)

# N의 값은 100이하의 자연수
N = [1, 5, 10, 31, 51, 75, 100]

# N의 값이 들어가는 for문
for i in range(len(N)):
    # input 값 제한
    assert value_limit(N[i]) is True
    # input 값 작성
    input_file = open(f"coding test/test_result/{i + 1}.in", "w")
    input_file.write(str(N[i]) + "\n")
    for j in range(N[i]):
        for o in range(N[i]):
            n = random.randint(0, len(strs) - 1)
            input_file.write(strs[n])
        input_file.write("\n")
    input_file.close()

    input_file = open(f"coding test/test_result/{i + 1}.in", "r")
    
    # output 값 가공
    output_file = open(f"coding test/test_result/{i + 1}.out", "w")
    input_line = input_file.readlines()
    input_values = []
    for j in input_line[1:]:
        input_values.append(list(j))
    
    # 줄바꿈 문자 없애기
    real_input_values = []
    for j in input_values:
        real_input_values.append(j[:len(j) - 1])

    # output 값 작성
    for j in range(N[i]):
        for o in range(N[i]):
            output_file.write(f"{real_input_values[o][N[i] - 1 - j]}")
        output_file.write("\n")

    # input, output 파일 닫기
    input_file.close()
    output_file.close()