grades = input("Введите оценки, разделенные пробелами: ")
grades_list = grades.split()

updated_grades = ' '.join(['3' if grade == '2' else grade for grade in grades_list])

print(updated_grades)
input("press any key to close window")
