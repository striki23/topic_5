fruits = dict([
    ('яблоко', 50),
    ('банан', 30),
    ('груша', 40),
    ('апельсин', 35),
    ('мандарин', 60)
])

print("Список фруктов и их цены:")
print(fruits)

user_input = input('Выберите фрукт из списка: ')

price = fruits[user_input]
print('Цена апельсин - ', price)
