# string-validators

if __name__ == '__main__':
    s = input()
    print(any([s_.isalnum() for s_ in s]))
    print(any([s_.isalpha() for s_ in s]))
    print(any([s_.isdigit() for s_ in s]))
    print(any([s_.islower() for s_ in s]))
    print(any([s_.isupper() for s_ in s]))