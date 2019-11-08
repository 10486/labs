var = int(input("Введите вариант задания\n"))
if var == 3:
    x = float(input("Введите х\n"))
    y = (x ** 2 + 1) / (3 * (x ** 2 - 1)) + (x ** 2 - 1) * (1 - x)
    print(f"y = {round(y,2)}")
elif var == 4:
    x = float(input("Введите х\n"))
    y = (x * (x * x ** .5) ** .5) ** .5
    print(f"y = {round(y,2)}")
else:
    print("Я не делал этот вариант")