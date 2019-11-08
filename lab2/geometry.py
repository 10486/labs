var = int(input("Введите вариант задания\n"))
if var == 3:
    a = float(input("Введите сторону икосаэдра\n"))
    R = a / 4 * (2 * (5 + 5 ** .5)) ** .5
    print(f"Радиус описанной окружности - {round(R,2)}")
elif var == 4:
    import math
    r = float(input("Введие радиус вписанной окружности\n"))
    a = float(input("Введите угол при основании(в градусах)\n"))
    S = (4 * r ** 2) / math.sin(math.pi / 180 * a)
    print(f"Площадь трапеции - {round(S,2)}")
else:
    print("Я не делал этот вариант")