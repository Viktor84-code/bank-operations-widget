import datetime


def log(filename=None):
    """
    Декоратор для логирования выполнения функций.

    Args:
        filename (str, optional): Имя файла для записи логов.
                                Если не указано, логи выводятся в консоль.

    Returns:
        function: Декоратор с логированием.

    Example:
        >>> @log()
        ... def add(a, b):
        ...     return a + b
        ...
        >>> @log(filename="operations.log")
        ... def multiply(x, y):
        ...     return x * y
    """

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
