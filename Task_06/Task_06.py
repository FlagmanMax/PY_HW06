# Создайте модуль с функцией внутри
# Функция получает на вход загадку, список с возможными вариантами отгадок и количество попыток на угадывание
# Программа возвращает номер попытки с которой угадали или 0 если попытки исчерпаны
from random import choice


_answers_count = {}

def quest(question, answers, try_count):
    tries = 0
    while tries < try_count:
        tries += 1
        print(question)
        answer = input("Ваш ответ >>> ")
        if answer in answers:
            _answers_count[question] = tries

            print(f"Верно! Угадал за {tries} попыток")
            break
        else:
            print("Ответ не верный!")
    else:
        print("Не угадал(")

    return tries

def more(nums):
    quests = {"Сколько ног у муравья?":['4','5','6'],
              "Какого цвета огнетушитель?":['Красный','Синий'],
              "Сколько лет тебе было в детстве?":[str(i) for i in range(5,19)],
              "Летят 2 крокодила, один зеленый, другой направо. Зачем не холодильник, если я не курю?":['Да','Гладиолус']}

    for i in range(nums):
        q = choice(list(quests.keys()))
        quest(q, quests[q], 3)

def how_many_answers():
    print(*(f'Загадка {key[:10:]} отгадана с {value} попытки'\
          for key, value in _answers_count.items()), sep='\n')