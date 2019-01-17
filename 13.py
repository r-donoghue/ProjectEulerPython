f = open('test.txt').read().split()
n = 10

total = sum(map(int, f))
print ("Top", n, "digits of sum =", str(total)[:n])
