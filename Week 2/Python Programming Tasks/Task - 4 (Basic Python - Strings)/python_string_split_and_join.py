# python-string-split-and-join

def split_and_join(line):
    # write your code here
    l = line.split()
    return "-".join(l)

if __name__ == '__main__':
    line = input()
    result = split_and_join(line)
    print(result)