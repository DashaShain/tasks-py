input_string = input("Введите строку: ")
segment_size = int(input("Введите k: "))
transformed_string = ""
current_position = 0

while current_position < len(input_string):
    current_block = input_string[current_position:current_position + 2 * segment_size]
    reversed_part = current_block[:segment_size][::-1]

    unchanged_part = current_block[segment_size:]
    transformed_string += reversed_part + unchanged_part
    current_position += 2 * segment_size

print(transformed_string)