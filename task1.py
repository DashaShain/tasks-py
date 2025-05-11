phrase = input("Введите фразу: ")
words = phrase.split()
abbr = ""
for word in words:
    if word[0].isalpha():
        abbr += word[0].upper()
print(abbr)