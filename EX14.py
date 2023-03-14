import math
num = int(input())
p = 0
while p < math.log2(num):
    print(pow(2, p), end=' ')
    p += 1