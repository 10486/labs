import calculator
calc = calculator.Calculator()  # создать новый экземпляр класса Calculator, определенный в модуле calculator

calc.add(2)
print(calc.get_current())

# Импортируйте модуль my_module и используйте функцию hello_world.

...  # Импортируйте my_module здесь
import my_module

...  # Вызовите функцию hello_world из модуля my_module
my_module.hello_world("321313")
# ----------------------------------------------------#


""" 
Python поставляется с библиотекой стандартных модулей. 
Запомните, что вы можете использовать Ctrl + Space после точки (.), чтобы изучить доступные методы модуля. 
"""

import datetime

current_date = datetime.date.today()
print(current_date)  # Выведите текущую дату, используя встроенный модуль datetime


# ----------------------------------------------------#


""" 
Специальная форма оператора импорта импортирует имена из модуля непосредственно в таблицу символов импортирующего модуля. 
Таким образом, вы можете использовать функции напрямую без префикса module_name. 
"""

from calculator import Calculator

calc = Calculator()  # теперь мы можем использовать класс Calculator без префикса calculator.
calc.add(2)
print(calc.get_current())

# Импортируйте функцию hello_world из модуля my_module.Сравните с предыдущим примером.
from my_module import hello_world
hello_world("23121")  # Функция hello_world должна вызываться без указания модуля