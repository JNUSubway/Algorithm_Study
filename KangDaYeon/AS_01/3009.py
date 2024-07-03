x_num = []
y_num = []


for i in range(3):
    x, y = list(map(int, input().split()))
    x_num.append(x)
    y_num.append(y)


x_num = sorted(x_num)
y_num = sorted(y_num)

if x_num.count(x_num[0]) == 1:
    x = x_num[0]
    if y_num.count(y_num[0]) == 1:
        y = y_num[0]

    elif y_num.count(y_num[0]) == 2:
        y = y_num[2]
    print(x, y)

elif x_num.count(x_num[0]) == 2:
    x = x_num[2]
    if y_num.count(y_num[0]) == 1:
        y = y_num[0]
        
    elif y_num.count(y_num[0]) == 2:
        y = y_num[2]
    print(x, y)

    
    # elif x_num.count([0]) == 1:
    #     x1 = x_num[0]
    # if y_num.count([0]) == 2:
    #     y1 = y_num[2]
    # elif x_num.count([0]) == 1:
    #     y1 = y_num[0]

  



# a, b = map(int, input().split())
# c, d = map(int, input().split())
# e, f = map(int, input().split())

# num1 = 0
# num2 = 0

# if a == c:
#     num1 = e
#     if b == d:
#         num2 = f
#         print(num1, num2)
#     elif b == f:
#         num2 = d
#         print(num1, num2)
#     elif d == f:
#         num2 = b
#         print(num1, num2)


# elif a == e:
#     num1 = c
#     if b == d:
#         num2 = f
#         print(num1, num2)
#     elif b == f:
#         num2 = d
#         print(num1, num2)
#     elif d == f:
#         num2 = b
#         print(num1, num2)

# elif c == e:
#     num1 = a
#     if b == d:
#         num2 = f
#         print(num1, num2)
#     elif b == f:
#         num2 = d
#         print(num1, num2)
#     elif d == f:
#         num2 = b
#         print(num1, num2)



    