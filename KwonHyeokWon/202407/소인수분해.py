# 문제
# 정수 N이 주어졌을 때, 소인수분해하는 프로그램을 작성하시오.

# 입력
# 첫째 줄에 정수 N (1 ≤ N ≤ 10,000,000)이 주어진다.

# 출력
# N의 소인수분해 결과를 한 줄에 하나씩 오름차순으로 출력한다. N이 1인 경우 아무것도 출력하지 않는다.

import sys

def finput():
    return sys.stdin.readline().rstrip()

num = int(finput())
array = list()
div = 2
while True:
    if div > num:
        break
    elif num % div == 0:
        array.append(div)
        num = num // div
        div = 2
    else:
        div += 1

for i in array:
    print(i)
