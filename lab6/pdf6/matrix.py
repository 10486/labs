def write(matrix, name, f):
    f.write(f"Матрица {name}:\n")
    for i in matrix:
        for j in i:
            f.write(f"{j} ")
        f.write("\n")
