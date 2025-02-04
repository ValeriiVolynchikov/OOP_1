# -*- coding: utf-8 -*-
from typing import Any
import pytest
from pytest import CaptureFixture
from src.logging_mixin import LoggingMixin


class BaseDummyClass:
    """
    Базовый класс для тестирования миксина LoggingMixin.
    Этот класс нужен для того, чтобы избежать вызова конструктора object.
    """
    def __init__(self, *args: Any, **kwargs: Any) -> None:
        super().__init__()  # Передаем вызов дальше


class DummyTestClass(BaseDummyClass, LoggingMixin):
    """
    Тестовый класс для проверки работы миксина LoggingMixin.
    """
    def __init__(self, name: str, value: int) -> None:
        self.name = name
        self.value = value
        super().__init__()  # Передаем аргументы LoggingMixin


def test_logging_mixin_creation(capsys: CaptureFixture) -> None:
    """
    Тестирует работу миксина LoggingMixin при создании объекта.
    Проверяет, что сообщение о создании объекта выводится в консоль корректно.
    """
    # Создаем объект тестового класса
    DummyTestClass(name="Test Object", value=42)

    # Считываем вывод в консоль
    out, _ = capsys.readouterr()

    # Ожидаемый вывод
    expected_output = "Создан объект класса DummyTestClass с параметрами: name=Test Object, value=42\n"

    # Удаляем лишние пробелы для точного сравнения
    out = out.strip()  # Убираем символы перевода строки и пробелы в начале/конце строки
    expected_output = expected_output.strip()

    # Проверяем соответствие вывода ожидаемому результату
    assert out == expected_output


def test_logging_mixin_repr() -> None:
    """
    Тестирует метод __repr__ миксина LoggingMixin.
    Проверяет, что метод возвращает корректное строковое представление объекта.
    """
    # Создаем объект тестового класса
    obj = DummyTestClass(name="Test Object", value=42)

    # Ожидаемое строковое представление
    expected_repr = "DummyTestClass(name='Test Object', value=42)"

    # Проверяем результат вызова метода __repr__
    assert repr(obj) == expected_repr
