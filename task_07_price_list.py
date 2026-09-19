prices = {
    "Кирпич": 20,
    "Цемент": 450.00,
    "Песок": 800.00,
    "Сталь": 48000.00,
    "Бетон": 5000.00
}

print("=" * 55)
print("ПРАЙС-ЛИСТ МАТЕРИАЛОВ")
print("=" * 55)

print("Начальный прайс-лист:")
for item, price in prices.items():
    print(f"  {item}: {price:.2f} руб")
print("-" * 55)

prices["Плитка"] = 1500.00
prices["Линолеум"] = 890.00
print("Добавлены: Плитка, Линолеум")
print("-" * 55)

item_to_update = "Цемент"
old_price = prices[item_to_update]
prices[item_to_update] = old_price * 1.10

print(f"Цена '{item_to_update}' увеличена на 10%:")
print(f"  {old_price:.2f} руб → {prices[item_to_update]:.2f} руб")
print("-" * 55)

deleted_item = "Песок"
deleted_price = prices.pop(deleted_item)

print(f"Удалён материал: '{deleted_item}' (цена была {deleted_price:.2f} руб)")
print("-" * 55)

total_price = sum(prices.values())   # сумма всех цен
count = len(prices)                  # количество товаров
average_price = total_price / count  # средняя цена

print("Итоговый прайс-лист:")
for item, price in prices.items():
    print(f"  {item}: {price:.2f} руб")

print("-" * 55)
print(f"Количество товаров:    {count}")
print(f"Общая стоимость:       {total_price:.2f} руб")
print(f"Средняя цена:          {average_price:.2f} руб")
print("=" * 55)
