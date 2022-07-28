# py-introduction-to-sets

def average(array):
    array = list(set(array))
    return (sum(array) / len(array))

if __name__ == '__main__':
    n = int(input())
    arr = list(map(int, input().split()))
    result = average(arr)
    print(result)