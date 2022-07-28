# symmetric-difference

M = int(input())
M_set = set(map(int, input().split()))
N = int(input())
N_set = set(map(int, input().split()))
ans = list(map(str, sorted(list(M_set.symmetric_difference(N_set)))))
print("\n".join(ans))