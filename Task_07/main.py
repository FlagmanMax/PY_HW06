# Создайте модуль
# Напишите в нем ф-ю которая получает на вхход дату ddmmYYYY
# Ф-я возвращает истину, если такая дата может существовать если такая дата возможна
# Проверку года на весокосность вынести в отдельную защищенную ф-ю

from Task_07 import check_date

if check_date(input("Введите дату в формате DD.MM.YYYY: ")):
    print("Дата существует")
else:
    print("Дата не существует")


