rowIndex = int(input("Введите индекс строки: "))
row = [1]

i = 0
while i < rowIndex:
    new_row = [1]
    j = 1
    while j < len(row):
        new_row.append(row[j - 1] + row[j])
        j += 1
    new_row.append(1)
    row = new_row
    i += 1

print(row)