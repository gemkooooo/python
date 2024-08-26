first = int(input('Введите первое число: '))
second = int(input('Введите второе число: '))
third = int(input('Введите третье число: '))

if first == second or second == third or first == third:
    print('Результат: 2')
elif first == second == third:
    print('Результат: 3')
elif first != second and second != third:
    print('Результат: 0')
else:
    print('Ошибка')