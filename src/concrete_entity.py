from src.entity_with_count import EntityWithCount


class ConcreteEntity(EntityWithCount):
    """Пример конкретного класса, реализующего абстрактные методы."""

    def get_total_quantity(self) -> int:
        return 0  # Реализация абстрактного метода
