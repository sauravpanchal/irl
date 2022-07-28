# find-second-maximum-number-in-a-list

sizes = int(input())
arr = list(map(int, input().split()))[:sizes]
largest = max(arr)
while max(arr) == largest :
    arr.remove(max(arr))
print(max(arr))