# no-idea

first_line = input().split()
n, m = int(first_line[0]), int(first_line[1])
U = input().split()

set_A = set(input().split())
set_B = set(input().split())
    
happiness = [(element in set_A) - (element in set_B) for element in U]

print(sum(happiness))