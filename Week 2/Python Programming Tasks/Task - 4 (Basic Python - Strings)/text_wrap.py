# text-wrap

import textwrap

def wrap(string, max_width):
    l = list()
    for st in range(0, len(string), max_width):
        l.append(string[st:max_width+st])
    return "\n".join(l)

if __name__ == '__main__':
    string, max_width = input(), int(input())
    result = wrap(string, max_width)
    print(result)