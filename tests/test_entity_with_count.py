import pytest

from src.concrete_entity import ConcreteEntity
from src.entity_with_count import EntityWithCount  # Импортируйте ваш абстрактный класс


def test_abstract_class_cannot_be_instantiated() -> None:
    """
    Проверяет, что нельзя создать экземпляр абстрактного класса EntityWithCount.
    """
    with pytest.raises(TypeError) as exc_info:
        _ = EntityWithCount()   # type: ignore

    # Проверяем, что сообщение об ошибке содержит упоминание об абстрактном методе
    assert "Can't instantiate abstract class EntityWithCount" in str(exc_info.value)
    assert "abstract method 'get_total_quantity'" in str(exc_info.value)


def test_concrete_entity_initialization() -> None:
    """
    Проверяет, что можно создать экземпляр конкретного класса, реализующего абстрактные методы.
    """
    entity = ConcreteEntity()
    assert entity.get_total_quantity() == 0  # Проверка реализации метода
