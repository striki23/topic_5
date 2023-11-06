numbers = [12, 45, 0.34711, 67, 89, 34, 55.632781, 78.9395]

# находим среднее арифметическое значение списка numbers,
# используя методы sum и len

average = sum(numbers)/len(numbers)

# округляем полученное значение до десятых

result = round(average, 1)

# выводим результат

print(result)