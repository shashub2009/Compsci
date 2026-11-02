def seq_search(student, grades, key):
    index = 0
    found = False
    while not found and index < len(students):
        if students[index] == key:
            found = True
        else:
            index += 1
    return grades[index]

students = ['Alissa', 'Ben', 'Charlie', 'Dianna']
grades = ['B', 'D', 'B', 'A']

print(seq_search(students, grades, 'Charlie'))



