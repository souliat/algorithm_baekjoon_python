a = int(input()) # a는 정수형으로 형변환
b = input() # b는 문자열로 그대로 둠

multiply_1 = a * int(b[2])
multiply_10 = a * int(b[1])
multiply_100 = a * int(b[0])

print(multiply_1)
print(multiply_10)
print(multiply_100)
print(a * int(b))