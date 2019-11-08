def rec(n, x):
    if n == 0:
        return 1
    elif n == 1:
        return x
    else:
        n = n - 1
        return (2 * n + 1) / (n + 1) * x * rec(n, x) - n / (n + 1) * rec(n - 1, x)


def iteration(n, x):
    old_res = 1
    cur_res = x
    if n == 0:
        return old_res
    elif n == 1:
        return cur_res
    k = 1
    while n > k:
        cur_res, old_res = (2 * k + 1) / (k + 1) * x * cur_res - k / (k + 1) * old_res, cur_res
        k += 1
    return cur_res


print(rec(4, 2))
print(iteration(4, 2))
