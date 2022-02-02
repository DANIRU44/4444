#последний раз прикасался к этому коду 17.06.2019; моя самая первая программа(не считая hello world)
import numpy as np
import math
import time
import os
print("выбирите уровень сложности 1, 2 или 3")
f = int(input("уровень сложности:"))
if f == 1:
    print("введите число от одного до десяти, у вас 7 попыток")
    math.floor(np.random.uniform(1,10))
    for i in range(7):
        a = int(input("введите число:"))
        if a == math.floor(np.random.uniform(1,10)):
            print("поздравляем,вы угадали число " + str(a))
            break
        else:
            print("вы не угадали число")
    print("игра окончена, нажмите любую кнопку чтобы выйти:")
    input()
elif f == 2:
    print("введите число от одного до десяти, у вас 5 попыток")
    math.floor(np.random.uniform(1,10))
    for i in range(5):
        a = int(input("введите число:"))
        if a == math.floor(np.random.uniform(1,10)):
            print("поздравляем,вы угадали число " + str(a))
            break
        else:
            print("вы не угадали число")
    print("игра окончена, нажмите любую кнопку чтобы выйти:")
    input()
elif f == 3:
    print("введите число от одного до десяти, у вас 3 попытки")
    math.floor(np.random.uniform(1,10))
    for i in range(3):
        a = int(input("введите число:"))
        if a == math.floor(np.random.uniform(1,10)):
            print("поздравляем,вы угадали число " + str(a))
            break
        else:
            print("вы не угадали число")
    print("игра окончена, нажмите любую кнопку чтобы выйти:")
    input()
elif f == 1748395:
    print(".......................")
    time.sleep(2)
    print("зря ты это сделал")
    time.sleep(3)
    print("не хочешь играть по правилам...ну ладно")
    time.sleep(3)
    print("я тоже кое-что могу")
    time.sleep(3)
    print("я удалю все данные с этого копьютера")
    print(5)
    time.sleep(2)
    print(4)
    time.sleep(2)
    print(3)
    time.sleep(2)
    print(2)
    time.sleep(2)
    print(1)
    time.sleep(3)
    print("хотя знаешь ты можешь отиграться")
    time.sleep(3)
    print("чтобы ты понял, что всё серьёзно, компьютер уже заражён и выйдя из программы")
    time.sleep(2)
    print("ты автоматически запустишь вирус")
    time.sleep(3)
    print("но если сможешь отъиграться то я просто самоуничтожусь")
    time.sleep(3)
    j = os.environ["USERNAME"]
    print("начнём " + str(j))
    time.sleep(2)
    print("угадайте случайно заданное число от 1 до 10, у вас 1 попытка ")
    input("введите число: ")
    time.sleep(2)
    print("поздравляем вы угадали число!")
    time.sleep(3)
    print("мы ещё встретимся...")
    time.sleep(4)
else:
    print("ошибка")



















