n = int(input("Сколько чисел Фибоначчи нужно: "))
a = 0
b = 1
i = 0
while i < n:
    print(a)
    c = a + b
    a = b
    b = c
    i += 1