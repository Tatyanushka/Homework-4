#2- Задайте последовательность чисел. Напишите 
# программу, которая выведет список неповторяющихся 
# элементов исходной последовательности. Посмотрели, 
# что такое множество? Вот здесь его не используйте.


lst_number = [3, 6, 9, 3, 8, 9]
unique_lst = []

for i in range(len(lst_number)):
    f = True
    for j in range(len(lst_number)):
        if lst_number[i] == lst_number[j] and i != j:
            f = False
            break
    if f == True:
        unique_lst.append(lst_number[i])
print(unique_lst)

