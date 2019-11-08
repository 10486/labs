# Во входном файле имеется строка символов, которая заканчивается
# точкой. Напишите рекурсивную программу, которая определяет количество
# цифр в заданной последовательности.


def counter(string):
    numbers = [str(x) for x in range(10)] + ['A', 'B', 'C', 'D', 'E', 'F']
    if len(string) == 1:
        return int(string in numbers)
    else:
        if string[0] in numbers:
            return counter(string[1:]) + 1
        return counter(string[1:])


with open('input.txt', 'r') as f:
    print(counter(f.read()))
