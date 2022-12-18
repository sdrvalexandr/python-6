import math

def ex1():
    i = 0
    list = []

    while i != 1:
        numbers = input('Введите число: ')
        if numbers.isnumeric():
            list.append(int(numbers))
            print(list)
        elif numbers == ' ':
            i = 1
        else:
            print('некорректный ввод, попробуйте еще раз')
    print(list)
    print('НОД для ',list,' будет :',math.gcd(*list, list[0]))

def ex2():
    k = 0
    string = ''
    while k != 1:
        string = input('Введите строку: ')
        string.islower()
        count = 1
        for i in range(len(string)):
            if string[i] != 'о' and string[i] != 'р':
                print('некорректный ввод, попробуйте еще раз')
                break
            else:
                # print('значения вверны')
                count += 1
                if count == len(string):
                    k = 1
    print('STRING: ',string)
    char = 'р'
    count = 0
    maxCount = 0
    for i in range(len(string)):
        if char == string[i]:
            count += 1
        else:
            if count > maxCount:
                maxCount = count
            count = 0
    print('max count', maxCount)

print('В модуле math есть функция math.gcd(a, b), возвращающая наибольший общий делитель (НОД) двух чисел. Вычислите и напечатайте наибольший общий делитель для списка натуральных чисел. Ввод чисел продолжается до ввода пустой строки.')
print(ex1())
print('Дана строка текста, состоящая из букв русского алфавита "О" и "Р". Буква "О" – соответствует выпадению Орла, а буква "Р" – соответствует выпадению Решки. Напишите программу, которая подсчитывает наибольшее количество подряд выпавших Решек.\nФормат входных данных:\nНа вход программе подается строка текста, состоящая из букв русского алфавита "О" и "Р".\nФормат выходных данных:\nПрограмма должна вывести наибольшее количество подряд выпавших Решек.\nПримечание. Если выпавших Решек нет, то необходимо вывести число 0.')
print(ex2())