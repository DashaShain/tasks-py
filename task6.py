s = input("Введите строку: ")
k = int(input("Введите k: "))
result = ""
i = 0
while i < len(s):
    part = s[i:i + 2 * k]
    first_k = part[:k][::-1]
    rest = part[k:]
    result += first_k + rest
    i += 2 * k
print(result)