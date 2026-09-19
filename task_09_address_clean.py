addresses = [
    " г. Москва, ул. Ленина, д. 10  ",
    "г.Казань,ул.Баумана,д.15",
    " г. Санкт-Петербург, ул. Невский, д. 100  "
]

def clean_address(address):
    """
    Приводит адрес к стандартному виду:
    - убирает пробелы по краям
    - добавляет пробел после 'г.', 'ул.', 'д.'
    - унифицирует запятые (один пробел после запятой)
    - убирает множественные пробелы
    """
  
    address = address.strip()

    address = address.replace("г.", "г. ")
    address = address.replace("ул.", "ул. ")
    address = address.replace("д.", "д. ")

    parts = address.split(",")
    cleaned_parts = [part.strip() for part in parts]
    address = ", ".join(cleaned_parts)

    while "  " in address:
        address = address.replace("  ", " ")

    return address

print("=" * 60)
print("=== СРАВНЕНИЕ ===")
print("=" * 60)

for i, original in enumerate(addresses, 1):
    cleaned = clean_address(original)
    print(f"#{i}")
    print(f"  ДО:     '{original}'")
    print(f"  ПОСЛЕ:  '{cleaned}'")
    print("-" * 60)
