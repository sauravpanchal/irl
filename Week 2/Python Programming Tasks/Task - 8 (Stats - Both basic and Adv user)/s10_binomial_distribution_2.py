# s10-binomial-distribution-2

def fact(n):
    if n == 0:
        return 1
    return n * fact(n - 1)

def bi_dist(x, n, p, q):
    val = (fact(n) / (fact(x) * fact(n - x))) * (p ** x) * ((q) ** (n - x))
    return val
    
inp = input().split()
q, total = float(inp[0])/100, int(inp[1])

x = 2

summation = 0
for i in range(x+1):
    summation += bi_dist(i, total, q, 1 - q)
print(round(summation, 3))

summation = 0
for i in range(x, total+1):
    summation += bi_dist(i, total, q, 1 - q)
print(round(summation, 3))