supplier_1 = ["Кирпич", "Цемент", "Песок", "Сталь"]
supplier_2 = ["Цемент", "Песок", "Бетон", "Гравий"]
supplier_3 = ["Кирпич", "Песок", "Бетон", "Древесина"]
print("=" * 60)
print("АНАЛИЗ ЗАКАЗОВ ПОДРЯДЧИКОВ")
print("=" * 60)
print("Подрядчик #1:", supplier_1)
print("Подрядчик #2:", supplier_2)
print("Подрядчик #3:", supplier_3)
print("-" * 60)

set_1 = set(supplier_1)
set_2 = set(supplier_2)
set_3 = set(supplier_3)

all_unique = set_1 | set_2 | set_3
print(f"Все уникальные материалы:  {sorted(all_unique)}")

common_all = set_1 & set_2 & set_3
print(f"Общие для всех трёх:       {sorted(common_all)}")

only_first = set_1 - set_2 - set_3
print(f"Только у подрядчика #1:    {sorted(only_first)}")

at_least_two = (set_1 & set_2) | (set_1 & set_3) | (set_2 & set_3)
exactly_two = at_least_two - common_all
print(f"Ровно у двух подрядчиков:  {sorted(exactly_two)}")
print("=" * 60)
