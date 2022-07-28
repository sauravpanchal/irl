# py-set-symmetric-difference-operation

n1 = int(input())
n1_s = list(map(int, input().split()))
n2 = int(input())
n2_s = list(map(int, input().split()))
print(len(set(n1_s).symmetric_difference(set(n2_s))))