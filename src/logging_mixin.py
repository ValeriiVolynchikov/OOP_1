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
        super().__init__(*args, **kwargs)  # Вызываем конструктор родительского класса
        class_name = self.__class__.__name__
        params = []
        for key in self.__dict__:
            value = getattr(self, key)  # Получаем значение атрибута
            # Проверяем, является ли атрибут защищенным
            if key.startswith('_') and not key.startswith('__'):
                params.append(f"{key[1:]}={value}")  # Убираем один уровень подчеркивания
            else:
                params.append(f"{key}={value}")

        print(f"Создан объект класса {class_name} с параметрами: {', '.join(params)}", flush=True)

    def __repr__(self) -> str:
        """
        Формальное строковое представление объекта для отладки.
        Возвращает строку, содержащую имя класса и все переданные параметры.
        """
        class_name = self.__class__.__name__
        params = ', '.join([f"{k}={repr(v)}" for k, v in self.__dict__.items()])
        return f"{class_name}({params})"
