def int_dot(r):
    y = r
    counter = 0
    for x in range(r):
        if x ** 2 + y ** 2 <= r ** 2:
            counter += y
        else:
            counter += y - 1
    return counter * 4 + 1

