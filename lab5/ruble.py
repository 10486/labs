cop = int(input())
rub = cop // 100
cop %= 100
cop_name = ''
rub_name = ''

if (4 < cop < 21) or (cop % 10 > 4) or cop % 10 == 0:
    cop_name = 'копеек'
elif cop % 10 == 1:
    cop_name = 'копейка'
else:
    cop_name = 'копейки'

if (4 < rub % 100 < 21) or (rub % 10 > 4) or rub % 10 == 0:
    rub_name = 'рублей'
elif rub % 10 == 1:
    cop_name = 'рубль'
else:
    rub_name = 'рубля'

print(f'{rub if rub else ""} {rub_name if rub else ""}\n{cop if cop else ""} {cop_name if cop else ""}')