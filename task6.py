# Задача 6*.
# Реализовать структуру данных «Товары». Она должна представлять собой список кортежей.
# Каждый кортеж хранит информацию об отдельном товаре.
# В кортеже должно быть два элемента:номер товара и словарь с параметрами
# --(характеристиками товара: название, цена, количество, единица измерения).
# Структуру нужно сформировать программно, т.е. запрашивать все данные у пользователя.
# Пример готовой структуры:
# [(1, {“название”: “компьютер”, “цена”: 20000, “количество”: 5, “eд”: “шт.”}),
# (2, {“название”: “принтер”, “цена”: 6000, “количество”: 2, “eд”: “шт.”}),
# (3, {“название”: “сканер”, “цена”: 2000, “количество”: 7, “eд”: “шт.”})]
# Необходимо собрать аналитику о товарах.
# Реализовать словарь, в котором каждый ключ — характеристика товара, например название,
# а значение — список значений-характеристик, например список названий товаров.ПРИМЕР:
# {“название”: [“компьютер”, “принтер”, “сканер”],
# “цена”: [20000, 6000, 2000],
# “количество”: [5, 2, 7],
# “ед”: [“шт.”] # }

q = int(input("Здравствуйте! Сколько продуктов желаете добавить в систему?\n\t Кол-во: "))
chr = "Название", "Цена", "Количество", "Ед.изм"
products, names, prices, Quantity, uoms = [], [], [], [], []
for i in range(q):
    print(f"Введите характеристики для товара # {i + 1} :")
    name, price, quantity, uom = input("\tНазвание : "), input("\tЦена товара : "), input("\tКоличество : "), \
                                 input("\tЕд.изм : ")
    products_up = (i + 1, {chr[0]: name, chr[1]: price, chr[2]: quantity, chr[3]: uom})
    products.append(products_up)
    names.append(products[i][1].get(chr[0]))
    prices.append(products[i][1].get(chr[1]))
    Quantity.append(products[i][1].get(chr[2]))
    uoms.append(products[i][1].get(chr[3]))
analytics ={chr[0]: names, chr[1]: prices, chr[2]: Quantity, chr[3]: uoms}
print(f"Статистика по товарам ниже \n{analytics}")