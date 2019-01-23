# Шахов Кирилл 
# ИВТ 3 курс
# реализация Лабораторной работы 1, Лабораторной работы 2 и Самостоятельной работы. 

class RangeException(Exception):
  def __init__(self,text):
        RangeException.txt = text
"""
Создаем два списка с данными чисел и тип перевеода
"""
numbers = ['ноль','один','два','три','четыре','пять','шесть','семь','восемь','девять']
types = ['bin', 'oct', 'hex']

a =  input("Введите один из типов hex, oct, bin:")

"""
Создаем функцию для задачи
"""
def getStringNumber(x, num_type):
  if num_type in types and num_type != "" and x in range(0,10):
    if (num_type == 'hex'):
      return hex(x)
    elif (num_type == 'oct'):
      return oct(x)
    elif (num_type == 'bin'):
      return bin(x)
    else:
      return 'Ok'
  
  if x in range(0,10):
    return numbers[x] 
  else:
    return "Неверное значение"

"""
Исключение RangeException на неверный тип вводимого числа(например, строка)
"""
try:
  num =  int(input("Введите число от 0 до 9:"))
  if ((num<0) | (num>9)):
      raise RangeException('Введено неверное значение числа, не соответсвует интервалу/типу RangeException') # если не те цифры
  else:
      print(getStringNumber(num, a)) 
      with open('FileP.txt', 'a') as f:
        f.write('Numbers:'"\n" + str(num) + 'Type:' + str(a)+"\n") 
except RangeException:
  print(RangeException.txt)
except ValueError:
  print("Введено неверное значение числа, не соответсвует интервалу/типу ValueError")

"""
Тестирование assert
"""
def test():
  assert getStringNumber(9, 'oct') == '0o11'
  assert getStringNumber('qw', 'oct') == 'Неверное значение'
  assert getStringNumber(5, 'qwer') == 'пять'

test()
