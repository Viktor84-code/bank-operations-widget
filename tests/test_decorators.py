import pytest
import os
from src.decorators.decorators import log


def test_log_decorator_to_console(capsys):
    """Тест логирования в консоль"""

    @log()
    def add(a, b):
        return a + b

    result = add(1, 2)

    # Перехватываем вывод в консоль
    captured = capsys.readouterr()
    assert "add ok" in captured.out
    assert result == 3


def test_log_decorator_to_file():
    """Тест логирования в файл"""
    test_filename = "test_log.txt"

    @log(filename=test_filename)
    def multiply(x, y):
        return x * y

    # Удаляем файл если он существует
    if os.path.exists(test_filename):
        os.remove(test_filename)

    result = multiply(3, 4)

    # Проверяем что файл создан и содержит лог
    with open(test_filename, "r", encoding="utf-8") as f:
        content = f.read()
        assert "multiply ok" in content
    assert result == 12

    # Чистим за собой
    os.remove(test_filename)


def test_log_decorator_error(capsys):
    """Тест логирования ошибки"""

    @log()
    def divide(a, b):
        return a / b

    try:
        divide(1, 0)
    except ZeroDivisionError:
        pass

    # Проверяем лог ошибки
    captured = capsys.readouterr()
    assert "divide error" in captured.out
    assert "ZeroDivisionError" in captured.out
