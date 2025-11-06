import datetime


def log(filename=None):
    def decorator(func):
        def wrapper(*args, **kwargs):
            # Логируем начало выполнения
            start_time = datetime.datetime.now()

            try:
                # Вызываем исходную функцию
                result = func(*args, **kwargs)

                # Логируем успешное выполнение
                log_message = f"{func.__name__} ok at {start_time}\n"

            except Exception as e:
                # Логируем ошибку
                log_message = f"{func.__name__} error: {type(e).__name__}. Inputs: {args}, {kwargs}\n"
                raise
            finally:
                # Записываем лог в файл или консоль
                if filename:
                    with open(filename, "a", encoding="utf-8") as f:
                        f.write(log_message)
                else:
                    print(log_message, end="")

            return result

        return wrapper

    return decorator
