# Создайте модуль с функцией внутри
# Функция получает на вход загадку, список с возможными вариантами отгадок и количество попыток на угадывание
# Программа возвращает номер попытки с которой угадали или 0 если попытки исчерпаны

def quest(question, answers, try_count):
    tries = 0
    while tries < try_count:
        tries += 1
        print(question)
        answer = input("Ваш ответ >>> ")
        if answer in answers:
            print(f"Верно! Угадал за {tries} попыток")
            break
        else:
            print("Ответ не верный!")
    else:
        print("Не угадал(")

    return tries