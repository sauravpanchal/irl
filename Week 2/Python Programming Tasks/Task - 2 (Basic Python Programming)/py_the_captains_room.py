# py-the-captains-room

group_size = int(input())
l = list(map(int, input().split()))
hash_map = dict()
for i in range(len(l)):
    if l[i] in hash_map:
        hash_map[l[i]] += 1
    else:
        hash_map[l[i]] = 1
for key, value in hash_map.items():
    if value == 1:
        print(key)
        break