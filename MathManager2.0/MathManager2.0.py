import os

while True:
    os.system("cls")
    print("Выберете цвет:")
    print("1 - Синий")
    print("2 - Зелёный")
    print("3 - Голубой")
    print("4 - Красный")
    print("5 - Фиолетовый")
    print("6 - Жёлтый")
    print("7 - Белый, как сейчас")
    print("8 - Тускло-белый")
    print("9 - Светло-синий")
    print("10 - BIOS")
    print("0 - Выход")

    choice = input()
    if choice == "0":
        break

    if choice == "1":
        os.system("color 1")
    elif choice == "2":
        os.system("color 2")
    elif choice == "3":
        os.system("color 3")
    elif choice == "4":
        os.system("color 4")
    elif choice == "5":
        os.system("color 5")
    elif choice == "6":
        os.system("color 6")
    elif choice == "7":
        os.system("color 7")
    elif choice == "8":
        os.system("color 8")
    elif choice == "9":
        os.system("color 9")
    elif choice == "10":
        os.system("color 17")

    os.system("cls")
    print("""
      __  __       _   _     __  __                                   
     |  \/  |     | | | |   |  \/  |                                  
     | \  / | __ _| |_| |__ | \  / | __ _ _ __   __ _  __ _  ___ _ __ 
     | |\/| |/ _` | __| '_ \| |\/| |/ _` | '_ \ / _` |/ _` |/ _ \ '__|
     | |  | | (_| | |_| | | | |  | | (_| | | | | (_| | (_| |  __/ |   
     |_|  |_|\__,_|\__|_| |_|_|  |_|\__,_|_| |_|\__,_|\__, |\___|_|   
                                                       __/ |          
                                                      |___/           """)

    print("1 - Число Пи")
    print("2 - Деление")
    print("3 - Умножение")
    print("4 - Сложение")
    print("5 - Вычитание")
    print("0 - Выход")

    choice = input()
    if choice == "0":
        break

    if choice == "1":
        print("Первые 16 цифр числа Пи - 3.141592653589793")
    elif choice == "2":
        print("Введите первое число:")
        a = int(input())
        print("Введите второе число:")
        b = int(input())
        print("Частное - ", a / b)
        input()
    elif choice == "3":
        print("Введите первое число:")
        a = int(input())
        print("Введите второе число:")
        b = int(input())
        print("Произведение - ", a * b)
        input()
    elif choice == "4":
        print("Введите первое число:")
        a = int(input())
        print("Введите второе число:")
        b = int(input())
        print("Сумма - ", a + b)
        input()
    elif choice == "5":
        print("Введите первое число:")
        a = int(input())
        print("Введите второе число:")
        b = int(input())
        print("Разность - ", a - b)
        input()
