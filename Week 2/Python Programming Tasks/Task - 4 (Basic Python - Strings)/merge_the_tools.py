# merge-the-tools

def merge_the_tools(string, k):
    # your code goes here
    # error
    # for i in range(0,len(string), size):
    #     l.append("".join(set(string[i:size+i])))
    # for i in l:
    #     print(i)
    for i in range(0, len(string), k):
        final = ""
        for element in string[i:k+i]:
            if element not in final:
                final += element
        print(final)        
        

if __name__ == '__main__':
    string, k = input(), int(input())
    merge_the_tools(string, k)