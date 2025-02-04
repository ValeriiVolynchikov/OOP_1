import pytest
from src.entity_with_count import EntityWithCount


class MockEntity(EntityWithCount):
    """Тестовый класс для проверки EntityWithCount."""

    def __init__(self, quantity: int) -> None:
        """
        Инициализация тестового объекта.
        :param quantity: Количество.
        """
        super().__init__()
        self.quantity = quantity

    def get_total_quantity(self) -> int:
        """Реализация абстрактного метода."""
        return self.quantity


# Тесты для класса EntityWithCount
def test_entity_count() -> None:
    """Тест для проверки счетчика объектов."""
    # Сбрасываем счетчик перед началом теста
    EntityWithCount.count = 0

    # Создаем несколько объектов
    entity1 = MockEntity(10)
    entity2 = MockEntity(20)
    entity3 = MockEntity(30)

    # Проверяем, что счетчик увеличился на 3
    assert EntityWithCount.count == 3
    assert entity1.get_total_quantity() == 10
    assert entity2.get_total_quantity() == 20
    assert entity3.get_total_quantity() == 30


def test_get_total_quantity() -> None:
    """Тест для проверки метода get_total_quantity."""
    entity = MockEntity(50)

    # Проверяем, что метод возвращает правильное количество
    assert entity.get_total_quantity() == 50

#
# def test_abstract_class_cannot_be_instantiated() -> None:
#     """
#     Проверяет, что нельзя создать экземпляр абстрактного класса EntityWithCount.
#     """
#     with pytest.raises(TypeError) as exc_info:
#         # Попытка создать экземпляр абстрактного класса должна вызывать ошибку
#         EntityWithCount()
#
#     # Проверяем, что сообщение об ошибке содержит упоминание об абстрактном методе
#     assert "Can't instantiate abstract class EntityWithCount" in str(exc_info.value)
#     assert "abstract method 'get_total_quantity'" in str(exc_info.value)
