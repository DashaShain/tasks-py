num = input("Введите число: ")
counts = [0] * 10
for ch in num:
    digit = int(ch)
    counts[digit] += 1

for i in range(10):
    print(i, ":", counts[i])