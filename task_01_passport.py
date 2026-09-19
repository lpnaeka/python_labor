
student_name = "Липина Екатерина Игоревна"
group_number = "3140801/52501"
project_name = 'ЖК "GreenЛандия"'
floors = 22
height = 69.0
is_residential = True
construction_year = 2015

print("=" * 50)
print("ПАСПОРТ СТРОИТЕЛЬНОГО ОБЪЕКТА")
print("=" * 50)

print(f"Студент:          {student_name}")
print(f"Группа:           {group_number}")
print("-" * 50)
print(f"Название объекта: {project_name}")
print(f"Этажей:           {floors}")
print(f"Высота здания:    {height} м")
print(f"Год постройки:    {construction_year}")

if is_residential:
    object_type = "Жилой"
else:
    object_type = "Нежилой"

print(f"Тип объекта:      {object_type}")

print("=" * 50)

# Где находится этот объект:
# Объект находится по адресу: Ленинградская область, г. Мурино,
# ул. Шувалова, д. 5. Это реальный жилой комплекс.
#
# Почему я выбрала именно его:
# Я выбрала ЖК "GreenЛандия", потому что я живу в этом доме.
# Мне было интересно составить «цифровой паспорт» этого места.
