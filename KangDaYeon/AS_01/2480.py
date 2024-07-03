# 2480 주사위 세개

a, b, c = map(int,input().split())

list = [a, b, c]
list.sort()

if list.count(a) == 3:
    sum1 = 10000+(a*1000)
elif list.count(a) == 2:
    sum1 = 1000+(a*100)
elif list.count(b) == 2:
    sum1 = 1000+(b*100)
else:
    sum1 = list[2]*100

print(sum1)