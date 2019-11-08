def input_fun():
    a = float(input("Введите сторону а "))
    b = float(input("Введите сторону b "))
    c = float(input("Введите сторону c "))
    return [a, b, c]


def exists(a, b, c):
    if a <= 0 or b <= 0 or c <= 0:
        return False
    elif a + b <= c or a + c <= b or b + c <= a:
        return False
    else:
        return True


def view(a, b, c):
    if a == b:
        if b == c:
            return "равносторонний"
        else:
            return "равнобедренный"
    elif a == c or b == c:
        return "равносторонний"
    else:
        return "общего вида"


sides = input_fun()
if exists(*sides):
    print(f"Треугольник {view(*sides)}")
else:
    print("Треугольник не существует")
