# 2476 주사위 게임

per = int(input())
sum1 = 0
price = []

for i in range(per):
    a, b, c = map(int, input().split())
    num = [a, b, c]
    
    if num.count(a) == 3:
        sum1 = 10000+(a*1000)
        price.append(sum1)

    elif num.count(a) == 2:
        sum1 = 1000+(a*100)
        price.append(sum1)

    elif num.count(b) == 2:
        sum1 = 1000+(b*100)
        price.append(sum1)

    else:
        max1 = max(num)
        sum1 = max1*100
        price.append(sum1)


print(max(price))   
    
    