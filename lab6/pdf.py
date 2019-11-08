var = int(input("Номер Задания "))
if var == 1:
    import rectangle as rc
    with open("input1.txt") as f:
        data = f.read().split("\n")
        size = data[0].split(" ")
        if len(size) > 1:
            rc.print_rectangle(int(size[0]), int(size[1]), data[1])
        else:
            rc.print_square(int(size[0]), data[1])

##############################################################
elif var == 2:
    import os
    direct = os.listdir(os.getcwd())
    counter = 0
    exists = False
    # бесполезный кусок кода
    for i in direct:
        if i[-4:].lower() == ".txt":
            counter += 1
            #можно было заменить if os.path.exists()
            if i.lower() == "input2.txt":
                exists = True
    # начался нужный код
    if exists:
        with open("input2.txt") as f:
            data = f.read().split(" ")[0]
        summ = 0 #Счетчик суммы чисел
        mult = 1 #Счетчик произведения чисел
        for k in data:
            summ += int(k)
            mult *= int(k) if int(k) != 0 else 1
        count = len(data)
        print(f"Число: {data}\nКоличество цифр: {count}\nСумма цифр: {summ}\nПроизведение цифр: {mult}")
    else:
        print("Файл с входными данными не обнаружен")
################################################################


elif var == 3:
    import os
    if os.path.exists("input3.txt"):
        with open("input3.txt") as f:
            data = int(f.read())
        # список из всех числе от 1 до N
        out = [x for x in range(2, data)]
        counter = 0
        k = out[counter]
        #Приравниваем к нулю все чила которые делятся на k
        while k <= data ** .5:
            out = list(map(lambda x: 0 if x % k == 0 and x // k != 1 else x, out))
            k += 1
        #Выводим оставшиеся
        with open("output3.txt", "w") as f:
            for i in out:
                if i != 0:
                    f.write(str(i) + " ")
    else:
        print("Файл с входными данными не обнаружен")
####################################################

if var == 4:
    import time
    start = time.perf_counter()
    import datetime
    import circle
    with open("input4.txt") as f:
        r = int(f.read().split("\n")[0])
    out = circle.int_dot(r)
    with open("output4.txt", "w") as f:
        f.write(str(datetime.datetime.now().strftime("%Y-%m-%d %H:%M\n")))
        f.write(str(out)+"\n")
        end = time.perf_counter() - start
        print(str(end))
        f.write(str(end))


#############################################################


if var == 5:
    import numpy as np
    import random
    import matrix
    with open("input5.txt") as f:
        data = f.read().split("\n")
        k = data[1].split("=")[-1][1:]
        n, m = data[0].split(" ")
        k, n, m = int(k), int(n), int(m)
    A = np.array([[random.randint(0, 10) for _ in range(m)] for i in range(n)], int)
    B = np.array([[random.randint(0, 10) for _ in range(k)] for i in range(m)], int)
    C = np.dot(A, B)
    with open("output5.txt", "w") as f:
        matrix.write(A, "A", f)
        matrix.write(B, "B", f)
        matrix.write(C, "C", f)




