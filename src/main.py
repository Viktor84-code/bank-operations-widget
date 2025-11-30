from patterns import process_bank_search, process_bank_operations
from processing import load_operations, filter_by_state, sort_by_date

def main():
    print("Привет! Добро пожаловать в программу работы с банковскими транзакциями.")
    print("Выберите необходимый пункт меню:")
    print("1. Получить информацию о транзакциях из JSON-файла")
    print("2. Получить информацию о транзакциях из CSV-файла")
    print("3. Получить информацию о транзакциях из XLSX-файла")

    choice = input("Ваш выбор: ")

    if choice == "1":
        print("Для обработки выбран JSON-файл.")
        # Загружаем данные
        operations = load_operations("data/operations.json")
        print(f"Загружено операций: {len(operations)}")
        print("Введите статус, по которому необходимо выполнить фильтрацию.")
        print("Доступные для фильтровки статусы: EXECUTED, CANCELED, PENDING")

        while True:
            status = input("Статус: ").strip().upper()
            if status in ["EXECUTED", "CANCELED", "PENDING"]:
                print(f"Операции отфильтрованы по статусу '{status}'")
                # РЕАЛЬНАЯ ФИЛЬТРАЦИЯ
                filtered_operations = filter_by_state(operations, status)
                print(f"После фильтрации осталось: {len(filtered_operations)} операций")
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

        # Сортировка по дате
    sort_choice = input("Отсортировать операции по дате? Да/Нет: ").lower()
    if sort_choice == "да":
        sort_order = input("Отсортировать по возрастанию или по убыванию? ").lower()
        if sort_order == "по возрастанию":
            print("Сортировка по возрастанию даты")
            filtered_operations = sort_by_date(filtered_operations, reverse=False)
        elif sort_order == "по убыванию":
            print("Сортировка по убыванию даты")
            filtered_operations = sort_by_date(filtered_operations, reverse=True)
        else:
            print("Неверный выбор сортировки")
    else:
        print("Сортировка по дате не применяется")

    # Рублевые транзакции
    currency_choice = input("Выводить только рублевые транзакции? Да/Нет: ").lower()
    if currency_choice == "да":
        print("Вывод только рублевых транзакций")
        # Тут будет реальная фильтрация
    else:
        print("Вывод всех транзакций независимо от валюты")

    # Фильтрация по слову в описании
    search_choice = input("Отфильтровать список транзакций по определенному слову в описании? Да/Нет: ").lower()

    if search_choice == "да":
        search_word = input("Введите слово для поиска в описании: ")
        print(f"Фильтрация по слову '{search_word}'")
        # Тут будет вызов нашей функции process_bank_search
    else:
        print("Фильтрация по описанию не применяется")


if __name__ == "__main__":
    main()
