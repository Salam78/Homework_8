numbers = input("Введите список цифр через пробел: ").split()

count_5 = numbers.count('5')
count_4 = numbers.count('4')
count_3 = numbers.count('3')
count_2 = numbers.count('2')

average_score = sum(int(num) for num in numbers) / len(numbers)

print(count_5, count_4, count_3, count_2)
print("Средний балл Васи:", average_score)
input("press any key to close window")
