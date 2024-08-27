def display_life_weeks():
    # پرسیدن سن کاربر
    age = int(input("enter age: "))

    # تعداد کل هفته‌های 80 سال
    total_weeks = 80 * 52

    # تعداد هفته‌هایی که تاکنون گذشته
    passed_weeks = age * 52

    # نمایش هفته‌های عمر
    for i in range(total_weeks):
        if i < passed_weeks:
            print("+", end="")
        else:
            print("-", end="")
    
    print()  # برای خط جدید بعد از نمایش کامل

# فراخوانی تابع
display_life_weeks()
