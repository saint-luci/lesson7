grades = [[5, 3, 3, 5, 4], [2, 2, 2, 3], [4, 5, 5, 2], [4, 4, 3], [5, 5, 5, 4, 5]]
students = {'Johny', 'Bilbo', 'Steve', 'Khendrik', 'Aaron'}

students = list(students)
students.sort()

median_grade = {}

for i in range(len(students)):
    median_grade[students[i]] = sum(grades[i])/len(grades[i])

print(median_grade)
