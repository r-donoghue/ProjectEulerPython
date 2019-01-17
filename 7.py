import math
count = 0
x = 1
while count != 10001:
    x += 1
    factors = 0
    sq = round(x**.5)
    for i in range(1,int(sq)+1):
        divides = False
        if (x % i == 0):
            factors += 1
    if factors < 2:
        count += 1
        factors = 0
    factors = 0
    
print(x)
