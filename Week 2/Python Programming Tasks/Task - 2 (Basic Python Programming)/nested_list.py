# nested-list

marks = []
scores = []
for _ in range(int(input())):
    name = input()
    score = float(input())
    marks += [[name,score]]
    scores += [score]
second = sorted(list(set(scores)))[1] 

for name, score in sorted(marks):
     if score == second :
            print(name)