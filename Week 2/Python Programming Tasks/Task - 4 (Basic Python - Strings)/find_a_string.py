# find-a-string

def count_substring(string, sub_string):
    count = 0
    for idx in range(0, len(string)):
        # print(string[idx:len(sub_string)+idx])
        if string[idx:len(sub_string)+idx] == sub_string:
            count += 1
    return count
if __name__ == '__main__':
    string = input().strip()
    sub_string = input().strip()
    
    count = count_substring(string, sub_string)
    print(count)