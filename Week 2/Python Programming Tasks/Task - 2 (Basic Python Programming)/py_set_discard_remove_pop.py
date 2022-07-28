# py-set-discard-remove-pop

n = int(input())
s = set(map(int, input().split()))
N = int(input())

for iteration in range(N):
    op = input().split()
    if op[0] == "pop":
        s.pop()
    elif op[0] == "remove":
        s.remove(int(op[1]))
    elif op[0] == "discard":
        s.discard(int(op[1]))
# print(list(s)[0]) # results runtime error
print(sum(s))