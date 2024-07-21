grades = [[5, 3, 3, 5, 4], [2, 2, 2, 3], [4, 5, 5, 2], [4, 4, 3], [5, 5, 5, 4, 5]] # Список оценок
students = {'Johnny', 'Bilbo', 'Steve', 'Khendrik', 'Aaron'} # Множество имен учеников

sorted_students = sorted(students) # Сортируем имена учеников в алфавитном порядке
print(sorted_students)

average_grades = {}  # Создаем пустой словарь для хранения средних оценок

for i, student in enumerate(sorted_students): # Вычисляем средние оценки и заполняем словарь

    student_grades = grades[i] # Получаем список оценок для текущего ученика
    average_grade = sum(student_grades) / len(student_grades)# Вычисляем среднюю оценку
    average_grades[student] = average_grade # Добавляем в словарь

print(average_grades)