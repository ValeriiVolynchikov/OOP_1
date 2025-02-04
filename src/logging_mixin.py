# -*- coding: utf-8 -*-
from typing import Any


class LoggingMixin:
    """Миксин для логирования создания объектов."""

    def __init__(self, *args: Any, **kwargs: Any) -> None:
        """
        Конструктор миксина.
        :param args: Позиционные аргументы.
        :param kwargs: Именованные аргументы.
        """
        class_name = self.__class__.__name__
        params = ', '.join([f"{k}={v}" for k, v in kwargs.items() if not k.startswith('_')])
        print(f"Создан объект класса {class_name} с параметрами: {params}", flush=True)

        # Проверяем, есть ли родительский класс, который принимает аргументы
        try:
            super().__init__(*args, **kwargs)
        except TypeError:
            # Если родительский класс — object, вызываем без аргументов
            super().__init__()

    def __repr__(self) -> str:
        """
        Формальное строковое представление объекта для отладки.
        Возвращает строку, содержащую имя класса и все переданные параметры.
        """
        class_name = self.__class__.__name__
        params = ', '.join([f"{k}={repr(v)}" for k, v in self.__dict__.items() if not k.startswith('_')])
        return f"{class_name}({params})"
