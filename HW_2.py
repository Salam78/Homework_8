numbers = []
sum_of_numbers = 0

while True:
    num = int(input("Введите число: "))
    numbers.append(num)
    sum_of_numbers += num

    if sum_of_numbers == 0:
        break

sum_of_squares = sum([x**2 for x in numbers])

print("Сумма квадратов введенных чисел:", sum_of_squares)
input("press any key to close window")
