day_number = int(input("Введите номер дня недели (1-7): "))
days_of_week = {
    1: "Понедельник",
    2: "Вторник",
    3: "Среда",
    4: "Четверг",
    5: "Пятница",
    6: "Суббота",
    7: "Воскресенье"
}

if 1 <= day_number <= 7:
    day_name = days_of_week[day_number]

    if day_number <= 5:
        status = "Рабочий день"
        schedule = "9:00 - начало смены"
    else:
        status = "Выходной"
        schedule = "Отдых"

    print("=" * 45)
    print("РАБОЧИЙ ГРАФИК")
    print("=" * 45)
    print(f"День недели:          {day_name}")
    print(f"Статус:               {status}")
    print(f"Режим:                {schedule}")
    print("=" * 45)

else:
    print("=" * 45)
    print("Ошибка: введите число от 1 до 7!")
    print("=" * 45)
