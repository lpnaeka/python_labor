
length = 6.5
width = 4.2
height = 3.0
PAINT_PRICE_PER_SQM = 125.0

floor_area = length * width
perimeter = 2 * (length + width)
wall_area = perimeter * height
volume = length * width * height
paint_cost = wall_area * PAINT_PRICE_PER_SQM

print("=" * 50)
print("РАСЧЕТ ПАРАМЕТРОВ ПОМЕЩЕНИЯ")
print("=" * 50)

print(f"Длина помещения:      {length} м")
print(f"Ширина помещения:     {width} м")
print(f"Высота помещения:     {height} м")
print("-" * 50)
print(f"Площадь пола:         {floor_area:.2f} м²")
print(f"Площадь стен:         {wall_area:.2f} м²")
print(f"Объем помещения:      {volume:.2f} м³")
print("-" * 50)
print(f"Стоимость покраски:   {paint_cost:.2f} руб")
print("=" * 50)
