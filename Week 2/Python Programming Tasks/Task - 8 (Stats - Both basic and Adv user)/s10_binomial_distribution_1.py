# s10-binomial-distribution-1

def fact(n):
    if n == 0:
        return 1
    return n * fact(n - 1)

def bi_dist(x, n, p, q):
    val = (fact(n) / (fact(x) * fact(n - x))) * (p ** x) * ((q) ** (n - x))
    return val
    
inp = input().split()
# inp = "1.09 1"
p, q = float(inp[0]), float(inp[1])

summation = 0
success = p / (p + q)
fail = 1 - success
total = 6
atleast = 3
for i in range(atleast, total+1):
    summation += bi_dist(i, total, success, fail)

print(round(summation, 3))