def rec(n):
    if n == 1:
        return 1
    else:
        return n * rec(n - 1)


def iteration(n):
    res = 1
    while n:
        res *= n
        n -= 1
    return res


k = 100
print(iteration(k))
print(rec(k))
