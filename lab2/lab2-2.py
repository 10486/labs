# Целые числа и числа с плавающей точкой являются одними из самых распространенных в языке Python

number = 9

print(type(number))   # Вывод типа переменной number

float_number = float(number)

# Создайте ещё несколько переменных разных типов и осуществите вывод их типов
str_number = str(number)
arr_number = [number]
dict_number = {0: number}
print(type(str_number))
print(type(arr_number))
print(type(dict_number))
print(type(type))
print(type(print))
print(int(float_number))



# Существует множество функций, позволяющих изменять тип переменных.
# Изучите такие функции как int(), float(), str() и последовательно примените их к переменным, созданным ранее.