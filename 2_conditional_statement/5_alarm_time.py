time, minute = input().split()

time = int(time)
minute = int(minute)

output_minute = 0
output_time = 0

if 0 <= minute < 45:
    output_minute = 60 - (45 - minute)
    if time != 0:
        output_time = time - 1
    else:
        output_time = 23
elif 45 <= minute < 60:
    output_minute = minute - 45
    output_time = time

print("{} {}".format(output_time, output_minute))