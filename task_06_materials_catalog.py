materials = ["Кирпич", "Цемент", "Песок", "Сталь", "Бетон"]

print("=" * 50)
print("КАТАЛОГ МАТЕРИАЛОВ")
print("=" * 50)
print(f"Начальный список:     {materials}")
print("-" * 50)
print("Элементы списка:")
print(f"  Первый элемент:     {materials[0]}")
print(f"  Последний элемент:  {materials[-1]}")
print(f"  Средние элементы:   {materials[1:4]}")
print("-" * 50)

materials.append("Стекло")  
materials.append("Дерево")
print(f"После добавления:     {materials}")
print("-" * 50)

deleted_item = materials.pop(1)
print(f"Удалён элемент:       {deleted_item}")
print("-" * 50)

print(f"Итоговый список:      {materials}")
print(f"Количество элементов: {len(materials)}")
print("=" * 50)
