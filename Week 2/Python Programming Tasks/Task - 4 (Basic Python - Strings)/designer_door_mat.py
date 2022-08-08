# designer-door-mat

# Enter your code here. Read input from STDIN. Print output to STDOUT
N, M = map(int,input().split())
pattern = [('.|.'*(2*i + 1)).center(M, '-') for i in range(N//2)]
print('\n'.join(pattern + ['WELCOME'.center(M, '-')] + pattern[::-1]))