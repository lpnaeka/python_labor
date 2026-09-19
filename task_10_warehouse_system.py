warehouse = {
    "Кирпич":   {"quantity": 5000, "price": 12.50,    "min_quantity": 1000},
    "Цемент":   {"quantity": 120,  "price": 450.00,   "min_quantity": 50},
    "Песок":    {"quantity": 8,    "price": 800.00,   "min_quantity": 10},
    "Сталь":    {"quantity": 30,   "price": 48000.00, "min_quantity": 20},
    "Бетон":    {"quantity": 45,   "price": 4200.00,  "min_quantity": 15}
}

print("=" * 78)
print("СИСТЕМА УЧЁТА СКЛАДА")
print("=" * 78)

print(f"{'Материал':<12} | {'Кол-во':>8} | {'Цена':>10} | {'Мин.':>8} | {'Стоимость':>12}")
print("-" * 78)

total_value = 0
critical_items = []
most_expensive_item = None
most_expensive_value = 0

for name, data in warehouse.items():
    quantity = data["quantity"]
    price = data["price"]
    min_qty = data["min_quantity"]

    value = quantity * price
    total_value += value

    is_critical = quantity < min_qty

    if value > most_expensive_value:
        most_expensive_value = value
        most_expensive_item = name

    if is_critical:
        critical_items.append(f"{name}: {quantity} < {min_qty}")

    mark = "КРИТИЧ!" if is_critical else ""
    print(f"{name:<12} | {quantity:>8} | {price:>10.2f} | {min_qty:>8} | {value:>12.2f}{mark}")

print("-" * 78)
print(f"ОБЩАЯ СТОИМОСТЬ:      {total_value:>12.2f} руб")

print("-" * 78)
print(f"Самый дорогой:        {most_expensive_item} ({most_expensive_value:.2f} руб)")

if critical_items:
    print("-" * 78)
    print(f" КРИТИЧЕСКИЕ ОСТАТКИ ({len(critical_items)}):")
    for item in critical_items:
        print(f"  - {item}")
else:
    print(" Все остатки в норме")

print("-" * 78)
print("=== ВЫДАЧА МАТЕРИАЛА ===")

material_to_withdraw = "Цемент"
amount_to_withdraw = 25

if material_to_withdraw in warehouse:
    current_qty = warehouse[material_to_withdraw]["quantity"]

    if current_qty >= amount_to_withdraw:
        new_qty = current_qty - amount_to_withdraw
        warehouse[material_to_withdraw]["quantity"] = new_qty
        print(f" Выдано {amount_to_withdraw} единиц '{material_to_withdraw}'")
        print(f" Остаток: {current_qty} → {new_qty}")
    else:
        print(f" Недостаточно '{material_to_withdraw}'! Нужно: {amount_to_withdraw}, есть: {current_qty}")
else:
    print(f" Материал '{material_to_withdraw}' не найден")

print("=" * 78)
