def factors(n):
    return [x for x in range(1, n+1) if n % x == 0]
n=0
increment=1
found = False
x = []
while (len(x) < 500):
    n+=increment
    increment+=1
    x = factors(n)
