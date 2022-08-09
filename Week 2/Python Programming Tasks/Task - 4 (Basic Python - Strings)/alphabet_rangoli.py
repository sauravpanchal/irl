# alphabet-rangoli

def print_rangoli(size):
    st = 'abcdefghijklmnopqrstuvwxyz'[0:size]
    for i in range(size-1, -size, -1):
        x = abs(i)
        mid = st[size:x:-1]+st[x:size]
        print ("--"*x+ '-'.join(mid)+"--"*x)
if __name__ == '__main__':
    n = int(input())
    print_rangoli(n)