a = int(input())
b = int(input())

b0 = int(b/100)
b1 = int((b%100)/10) #십의 자리수
b2 = (b%100)%10 #일의 자리수


print(a*b2)
print(a*b1)
print(a*b0)
print(a*b)