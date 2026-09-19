celsius = 150.0

fahrenheit = celsius * 9 / 5 + 32

if celsius <= 0:
    state = "Лёд ❄️"
elif 1 <= celsius <= 99:
    state = "Жидкость 💧"
else:
    state = "Пар ♨️"


print("=" * 45)
print("КОНВЕРТЕР ТЕМПЕРАТУР")
print("=" * 45)
print(f"Температура в °C:     {celsius}")
print(f"Температура в °F:     {fahrenheit:.2f}")
print(f"Состояние воды:       {state}")
print("=" * 45)
