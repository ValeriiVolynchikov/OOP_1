class Product:
    """ Класс для представления продукта."""
    def __init__(self, name: str, description: str, price: float, quantity: int) -> None:
        """
        Инициализация объекта Product.

        :param name: Название продукта.
        :param description: Описание продукта.
        :param price: Цена продукта.
        :param quantity: Количество продукта в наличии.
        :raises ValueError: Если цена или количество отрицательные.
        """

        if price < 0:
            raise ValueError("Цена товара не может быть отрицательной")
        if quantity < 0:
            raise ValueError("Количество товара не может быть отрицательным")

        self.name = name
        self.description = description
        self.__price = price  # Приватный атрибут цены
        self.quantity = quantity

    @property
    def price(self) -> float:
        """Геттер для атрибута 'цена'."""
        return self.__price

    @price.setter
    def price(self, new_price: float) -> None:
        """Сеттер для атрибута 'цена'."""
        if new_price <= 0:
            print("Цена не должна быть нулевая или отрицательная")
            return
        self.__price = new_price

    @classmethod
    def new_product(cls, product_data: dict) -> 'Product':
        """
        Класс-метод для создания нового продукта из словаря.

        :param product_data: Словарь с данными о продукте.
        :return: Объект класса Product.
        """
        return cls(
            name=product_data["name"],
            description=product_data["description"],
            price=product_data["price"],
            quantity=product_data["quantity"],
        )

    def __str__(self) -> str:
        """Строковое представление объекта Product."""
        return f"{self.name}, {self.price} руб. Остаток: {self.quantity} шт."

    def __add__(self, other: 'Product') -> float:
        """Магический метод сложения двух продуктов."""
        if not isinstance(other, Product):
            raise TypeError("Можно складывать только объекты класса Product.")
        if type(self) is not type(other):
            raise TypeError("Можно складывать только объекты одного класса.")
        return (self.price * self.quantity) + (other.price * other.quantity)


class Smartphone(Product):
    """Класс для представления смартфона."""
    def __init__(self, name: str, description: str, price: float, quantity: int, efficiency: float, model: str,
                 memory: int, color: str) -> None:
        super().__init__(name, description, price, quantity)
        self.efficiency = efficiency
        self.model = model
        self.memory = memory
        self.color = color


class LawnGrass(Product):
    """Класс для представления смартфона."""
    def __init__(self, name: str, description: str, price: float, quantity: int, country: str,
                 germination_period: str, color: str) -> None:
        super().__init__(name, description, price, quantity)
        self.country = country
        self.germination_period = germination_period
        self.color = color
