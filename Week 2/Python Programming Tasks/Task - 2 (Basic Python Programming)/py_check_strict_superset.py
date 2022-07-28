# py-check-strict-superset

U = set(map(int, input().split()))
size = int(input())
list_sets = []
for i in range(size):
    inp = set(map(int, input().split()))
    list_sets.append(inp)

def get_super(list_sets):
    for sets in list_sets:
        if len(U.intersection(sets)) == 0 or len(U.intersection(sets)) < len(sets):
            return "False"
    return "True"
    
print(get_super(list_sets))