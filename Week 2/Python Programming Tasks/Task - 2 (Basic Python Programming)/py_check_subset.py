# py-check-subset

def get_subsets(set1, set2):
    if set1.intersection(set2) == set1:
        return True
    return False
    
n = int(input())
for i in range(n):
    set1_n = int(input())
    set1 = set(map(int, input().split()))
    set2_n = int(input())
    set2 = set(map(int, input().split()))
    
    print(get_subsets(set1, set2))