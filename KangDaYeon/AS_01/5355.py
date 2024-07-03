# 5355 화성 수학

num = int(input())

for i in range(num):
    list1 = list(map(str, input().split()))
    sum = 0
    for i in range(len(list1)):
        if i == 0:
            sum += float(list1[i])
        else:
            if list1[i] == "@":
                sum = sum * 3
            elif list1[i] == "%":
                sum = sum + 5
            elif list1[i] == "#":
                sum = sum - 7

    print("%0.2f" %sum)
