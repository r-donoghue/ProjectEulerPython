#Project Euler Problem 9

def divisors(n):
    for divisor in range(1, int(n**0.5) + 1):
        if n % divisor == 0:
            yield divisor, n // divisor

pn = {}
for r in range(2, 550, 2):
    st = r*r // 2
    for s, t in divisors(st):
        x = (r+s) + (r+t) + (r+s+t)
        pn[x] = (r+s) * (r+t) * (r+s+t)

p = int(input('Pythagorean target sum'))
print ("Result:", pn[p] if p in pn else "Impossible sum.")
