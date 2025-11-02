expression = input("Введите арифметическое выражение: ")

if '+' in expression:
    num1, num2 = expression.split('+')
    result = float(num1) + float(num2)
elif '-' in expression:
    num1, num2 = expression.split('-')
    result = float(num1) - float(num2)
elif '*' in expression:
    num1, num2 = expression.split('*')
    result = float(num1) * float(num2)
elif '/' in expression:
    num1, num2 = expression.split('/')

    if float(num2) == 0:
        print("Ошибка: деление на ноль!")
        exit()
    result = float(num1) / float(num2)
else:
    print("Ошибка: неверный формат выражения")
    exit()

print(f"Результат: {result}")
