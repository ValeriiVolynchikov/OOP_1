from abc import ABC, abstractmethod


class EntityWithCount(ABC):
    """Абстрактный класс для сущностей с подсчетом количества."""

    count = 0

    def __init__(self) -> None:
        """Инициализация объекта EntityWithCount."""
        EntityWithCount.count += 1
        # super().__init__()

    @abstractmethod
    def get_total_quantity(self) -> int:
        """Абстрактный метод для получения общего количества."""
        pass
