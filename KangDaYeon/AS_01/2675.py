num = int(input())



for i in range(num):
    a, b = input().split()
    a = int(a)
    b = str(b)
    for i in range(0, len(b), 1):
        print(b[i]*a, end ='')
    print()