# 2525 오븐 시계

hour, min = map(int, input().split())
time = int(input())

final_min = time + min
final_hour = 0

if final_min < 60:
    print(hour, final_min)

if final_min >= 60:
    final_hour = hour + int(final_min /60)
    final_min = final_min % 60
    if final_hour >= 24:
        final_hour = final_hour - 24
        print(final_hour, final_min)
    else:
        print(final_hour, final_min)

