time, minute = map(int, input().split())
running_time = int(input())

time = time + running_time // 60
minute = minute + running_time % 60

if minute >= 60:
    time += 1
    minute -= 60

if time >= 24:
    time -= 24

print("{} {}".format(time, minute))