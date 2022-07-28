# py-set-mutations

if __name__ == '__main__':
    N = int(input())
    a = set(map(int, input().split()))
    n = int(input())
    for iteration in range(n):
        com = list(map(str, input().split()))
        n = int(com[1])
        b = set(map(int, input().split()))
        if com[0] == "intersection_update":
            a.intersection_update(b)
        elif com[0] == "update":
            a.update(b)
        elif com[0] == "symmetric_difference_update":
            a.symmetric_difference_update(b)
        elif com[0] == "difference_update":
            a.difference_update(b)

print(sum(a))