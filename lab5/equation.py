def input_fun():
    a = round(float(input("Введите коэффицент А")), 5)
    b = round(float(input("Введите коэффицент B")), 5)
    c = round(float(input("Введите коэффицент C")), 5)
    return [a, b, c]


def discriminant(a, b, c):
    return b ** 2 - 4 * a * c


def root(a, b, c):
    d = discriminant(a, b, c)
    roots = []
    if d >= 0:
        roots.append(round((-b + d) / (2 * a), 5))
        roots.append(round((-b - d) / (2 * a), 5))
    return roots


def output(roots):
    count = len(roots)
    if roots[0] == roots[1]:
        count = 1
    print(f"Колчиество корней: {count}")
    print("{:.5f}".format(min(roots)))
    print("{:.5f}".format(max(roots)))


coef = input_fun()
print("Уравнение X^2*({:.5f})+X*({:.5f})+({:.5f})".format(*coef))
output(root(*coef))


