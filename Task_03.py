# улучшаем задачу 2
# запускаем из терминала
# от 1 до 3 аргументов
# генераторное выражение

from guess_num.Task_02 import guess_num
from sys import argv

guess_num(*(int(i) for i in argv[1::]))



