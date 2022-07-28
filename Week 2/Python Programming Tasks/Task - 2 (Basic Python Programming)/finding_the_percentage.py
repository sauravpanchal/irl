# finding-the-percentage

if __name__ == '__main__':
    n = int(input())
    student_marks = {}
    for _ in range(n):
        name, *line = input().split()
        scores = list(map(float, line))
        student_marks[name] = scores
    query_name = input()
    student_values = student_marks[query_name]
    avg = format((sum(student_values) / len(student_values)), '.2f')
    print(avg)