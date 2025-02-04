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
        # Пустой конструктор, который просто вызывает родительский класс
        super().__init__(*args, **kwargs)  # Передаем управление дальше


class DummyTestClass(BaseDummyClass, LoggingMixin):
    """
    Тестовый класс для проверки работы миксина LoggingMixin.
    """
    def __init__(self, name: str, value: int) -> None:
        self.name = name
        self.value = value
        super().__init__(name=name, value=value)  # Передаем параметры в миксин через kwargs
        # Здесь вы можете вызвать LoggingMixin, если нужно
        # LoggingMixin.__init__(self, name=name, value=value)


def test_logging_mixin_creation(capsys: pytest.CaptureFixture) -> None:
    """Тестирует работу миксина для логирования создания объектов."""
    DummyTestClass(name="Test Object", value=42)  # Создание объекта

    out, _ = capsys.readouterr()  # Считываем вывод (на уровне ОС)
    expected_output = "Создан объект класса DummyTestClass с параметрами: name=Test Object, value=42\n"

    # Удаляем лишние пробелы для точного сравнения
    out = out.strip()
    expected_output = expected_output.strip()

    # Проверяем соответствие вывода ожидаемому результату
    assert out == expected_output


def test_logging_mixin_repr() -> None:
    """
    Тестирует метод __repr__ миксина LoggingMixin.
    Проверяет, что метод возвращает корректное строковое представление объекта.
    """
    obj = DummyTestClass(name="Test Object", value=42)  # Создание объекта
    expected_repr = "DummyTestClass(name='Test Object', value=42)"  # Ожидаемое представление

    # Проверяем результат вызова метода __repr__
    assert repr(obj) == expected_repr
