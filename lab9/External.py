from textwrap import wrap
# Максимальное количество цифр в числе(Включая знак)
MAX_DIGITS = 11


def external_sort(filename, num_files, max_memory):
    while not chek(filename):
        with open(filename, 'r') as f:
            files = []
            for i in range(num_files):
                files.append(open(f"tmp{i}.txt", 'w'))
            n = 0
            while True:
                data = f.read(max_memory * MAX_DIGITS)
                data = ''.join(map(to_str, sorted(list(map(int, wrap(data, 11))))))
                files[n % num_files].write(data)
                n += 1
                if len(data) < max_memory * MAX_DIGITS:
                    break
        for file in files:
            file.close()
        with open(filename, 'w') as f:
            tmp = [x for x in range(num_files)]
            files = []
            for i in range(num_files):
                files.append(open(f"tmp{i}.txt", 'r'))
                tmp[i] = int(files[i].read(MAX_DIGITS))
            while True:
                for i, num in enumerate(tmp):
                    if num == min(tmp):
                        f.write(to_str(num))
                        try:
                            d = files[i].read(MAX_DIGITS)
                            tmp[i] = int(d)
                        except ValueError:
                            tmp[i] = 10 ** MAX_DIGITS
                    if min(tmp) == 10 ** MAX_DIGITS:
                        break
                if min(tmp) == 10 ** MAX_DIGITS:
                    break
            for file in files:
                file.close()


def chek(filename):
    with open(filename, 'r') as f:
        prev = int(f.read(MAX_DIGITS))
        while True:
            try:
                current = int(f.read(MAX_DIGITS))
            except ValueError:
                return True
            if current < prev:
                return False


def to_str(num):
    return f"{'+' if num >= 0 else '-'}{abs(num):0>10}"


# import random
# with open('test.list', 'w') as f:
#     f.write(''.join(map(to_str, [random.randint(-(10 ** 10) + 1, (10 ** 10) - 1) for x in range(10000)])))
external_sort('test.list', 10, 1000)

