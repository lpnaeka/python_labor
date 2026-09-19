price_per_item = 700.0
quantity = 4

total_before_discount = price_per_item * quantity
if total_before_discount < 1000:
    discount_percent = 0
elif 1000 <= total_before_discount <= 5000:
    discount_percent = 5
else:
    discount_percent = 10

discount_amount = total_before_discount * (discount_percent / 100)
total_after_discount = total_before_discount - discount_amount

print("=" * 50)
print("КАЛЬКУЛЯТОР СКИДКИ")
print("=" * 50)
print(f"Цена за единицу:       {price_per_item:.2f} руб")
print(f"Количество:            {quantity} шт")
print("-" * 50)
print(f"Сумма без скидки:      {total_before_discount:.2f} руб")
print(f"Процент скидки:        {discount_percent}%")
print(f"Сумма скидки:          {discount_amount:.2f} руб")
print("-" * 50)
print(f"ИТОГО К ОПЛАТЕ:        {total_after_discount:.2f} руб")
print("=" * 50)
