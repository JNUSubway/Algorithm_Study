# 11022 A+B - 8

num = int(input())

for i in range(1, num+1):
    a, b = map(int, input().split())
    sum = a+b
    print("Case #%d: %d + %d = %d" %(i, a, b, sum))