# 11021 A+B - 7

num = int(input())

for i in range(1, num+1):
    a,b = map(int, input().split())
    sum = a+b
    print("Case #%d: %d" %(i, sum))
        
