fibonacci_count = int(input("Сколько чисел Фибоначчи нужно: "))
first_number = 0
second_number = 1
current_index = 0

while current_index < fibonacci_count:
    print(first_number)  

    next_number = first_number + second_number  # Вычисляем следующее число
    first_number = second_number               # Сдвигаем числа вперёд
    second_number = next_number

    current_index += 1