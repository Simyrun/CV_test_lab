# После запуска предлагает пользователю ввести текст, содержащий любые слова,
# слоги, числа или их комбинации, разделенные пробелом
# Считывает строку с текстом, и разбивает его на элементы списка, считая
# пробел символом разделителя
# Печатает этот же список элементов (через пробел), однако с удаленными
# дубликатами
line = input("Please write line with spaсe :  ").split(' ')
unique_list =[]
for i in line:
    if i not in unique_list:
        unique_list.append(i)
print(*unique_list)