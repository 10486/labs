import time
import random


def check(array, flag=True):
    for i in range(1, len(array)):
        disc = 1 if flag else -1
        if array[i - 1] * disc > array[i] * disc:
            return False
    return True


def bubble_sort(array):
    ready = False
    length = len(array)
    completed = 0
    while not ready:
        ready = True
        for i in range(1, length - completed):
            if array[i] < array[i-1]:
                array[i], array[i-1] = array[i-1], array[i]
                ready = False
        completed += 1


def insertion_sort(array):
    for i in range(len(array)):
        j = i - 1
        key = array[i]
        while array[j] > key and j >= 0:
            array[j + 1] = array[j]
            j -= 1
            array[j + 1] = key


def shell_sort(array):
    inc = len(array) // 2
    while inc:
        for i, el in enumerate(array):
            while i >= inc and array[i - inc] > el:
                array[i] = array[i - inc]
                i -= inc
            array[i] = el
        inc = 1 if inc == 2 else int(inc * 5.0 / 11)


def partition(nums, low, high):
    # Выбираем средний элемент в качестве опорного
    # Также возможен выбор первого, последнего
    # или произвольного элементов в качестве опорного
    pivot = nums[(low + high) // 2]
    i = low - 1
    j = high + 1
    while True:
        i += 1
        while nums[i] < pivot:
            i += 1

        j -= 1
        while nums[j] > pivot:
            j -= 1

        if i >= j:
            return j

        # Если элемент с индексом i (слева от опорного) больше, чем
        # элемент с индексом j (справа от опорного), меняем их местами
        nums[i], nums[j] = nums[j], nums[i]


def quick_sort(nums):
    # Создадим вспомогательную функцию, которая вызывается рекурсивно
    def _quick_sort(items, low, high):
        if low < high:
            # This is the index after the pivot, where our lists are split
            split_index = partition(items, low, high)
            _quick_sort(items, low, split_index)
            _quick_sort(items, split_index + 1, high)

    _quick_sort(nums, 0, len(nums) - 1)





def sort(array, type):
    if type == 0:
        t = time.perf_counter()
        bubble_sort(array)
    elif type == 1:
        t = time.perf_counter()
        insertion_sort(array)
    elif type == 2:
        t = time.perf_counter()
        shell_sort(array)
    elif type == 3:
        t = time.perf_counter()
        quick_sort(array)
    t = time.perf_counter() - t
    return t


def count_sort(arr):
    counter = {x: 0 for x in range(10)}
    for i in arr:
        counter[i] += 1
    result=[]
    for i in counter:
        result+=[i for k in range(counter[i])]
    return result


# if __name__ == "__main__":
#     sorts = ['Пузырковая', 'Вставками', "Шелла", "Быстрая"]
#     name = len(max(sorts, key=len))
#     print(f"{'Название':<{name}}|{'Отсоритованная':<15}|{'Случайная':<15}|Отсортированная в обратном порядке")
#     arr = [random.randint(-100000, 100000) for x in range(1000)]
#     for i in range(4):
#         time_sorting = []
#         time_sorting.append(sort(sorted(arr.copy()), i))
#         time_sorting.append(sort(arr.copy(), i))
#         time_sorting.append(sort(sorted(arr.copy(), reverse=True), i))
#         print(f"{sorts[i]:<{name}}|{time_sorting[0]:0>15.12f}|{time_sorting[1]:0>15.12f}|{time_sorting[2]:0>15.12f}")






