def main():
    print("Привет! Добро пожаловать в программу работы с банковскими транзакциями.")
    print("Выберите необходимый пункт меню:")
    print("1. Получить информацию о транзакциях из JSON-файла")
    print("2. Получить информацию о транзакциях из CSV-файла")
    print("3. Получить информацию о транзакциях из XLSX-файла")

    choice = input("Ваш выбор: ")

    if choice == "1":
        print("Для обработки выбран JSON-файл.")
        # Тут будет вызов функции для JSON

        print("Введите статус, по которому необходимо выполнить фильтрацию.")
        print("Доступные для фильтровки статусы: EXECUTED, CANCELED, PENDING")

        while True:
            status = input("Статус: ").upper()
            if status in ["EXECUTED", "CANCELED", "PENDING"]:
                print(f"Операции отфильтрованы по статусу '{status}'")
                break
            else:
                print(f"Статус операции '{status}' недоступен.")

    elif choice == "2":
        print("Для обработки выбран CSV-файл.")
        # Тут будет вызов функции для CSV

        print("Введите статус, по которому необходимо выполнить фильтрацию.")
        print("Доступные для фильтровки статусы: EXECUTED, CANCELED, PENDING")

        while True:
            status = input("Статус: ").upper()
            if status in ["EXECUTED", "CANCELED", "PENDING"]:
                print(f"Операции отфильтрованы по статусу '{status}'")
                break
            else:
                print(f"Статус операции '{status}' недоступен.")

    elif choice == "3":
        print("Для обработки выбран XLSX-файл.")
        # Тут будет вызов функции для XLSX

        print("Введите статус, по которому необходимо выполнить фильтрацию.")
        print("Доступные для фильтровки статусы: EXECUTED, CANCELED, PENDING")

        while True:
            status = input("Статус: ").upper()
            if status in ["EXECUTED", "CANCELED", "PENDING"]:
                print(f"Операции отфильтрованы по статусу '{status}'")
                break
            else:
                print(f"Статус операции '{status}' недоступен.")

    else:
        print("Неверный выбор.")

if __name__ == "__main__":
    main()
