def print_rectangle(a, b, file):
    with open(file[1:-1], 'w') as f:
        for i in range(b):
            if i == 0 or i == b - 1:
                f.write(a * "*" + "\n")
            else:
                f.write(f"*{(a-2)*' '}*\n")


def print_square(a, file):
    print_rectangle(a, a, file)
