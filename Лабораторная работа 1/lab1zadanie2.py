import random

win = random.randint(0, 100)
luck = False
while luck == False:
    vi = int(input("Введите ваше число" + "\n"))
    if vi == win:
        print("Поздравляю!!!Ты выиграл!")
        luck = True
    else:
        if vi > win:
            print("Ваше чиcло больше загадонного ")
        else:
            print("Ваше число меньше загаданного")
