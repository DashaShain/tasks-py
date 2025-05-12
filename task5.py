row_index = int(input("Введите индекс строки: "))
current_row = [1]
current_level = 0

while current_level < row_index:
    next_row = [1]
    element_index = 1

    while element_index < len(current_row):
        sum_of_adjacent = current_row[element_index - 1] + current_row[element_index]
        next_row.append(sum_of_adjacent)
        element_index += 1
    
    next_row.append(1)
    current_row = next_row
    current_level += 1
print(current_row)