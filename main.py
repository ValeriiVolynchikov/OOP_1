class Product:
    """ Класс для представления продукта."""
    def __init__(self, name: str, description: str, price: float, quantity: int):
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
        self.price = price
        self.quantity = quantity


class Category:
    """Класс для представления категории продуктов."""
    category_count = 0  # Количество категорий
    product_count = 0  # Количество всех товаров

    def __init__(self, name: str, description: str, products: list):
        """
                Инициализация объекта Category.

                :param name: Название категории.
                :param description: Описание категории.
                :param products: Список продуктов в категории.
                """
        self.name = name
        self.description = description
        self.products = products

        # Увеличиваем статические атрибуты класса
        Category.category_count += 1
        Category.product_count += len(products)


if __name__ == "__main__":
    product1 = Product(
        "Samsung Galaxy S23 Ultra", "256GB, Серый цвет, 200MP камера", 180000.0, 5
    )
    product2 = Product("Iphone 15", "512GB, Gray space", 210000.0, 8)
    product3 = Product("Xiaomi Redmi Note 11", "1024GB, Синий", 31000.0, 14)

    print(product1.name)
    print(product1.description)
    print(product1.price)
    print(product1.quantity)

    print(product2.name)
    print(product2.description)
    print(product2.price)
    print(product2.quantity)

    print(product3.name)
    print(product3.description)
    print(product3.price)
    print(product3.quantity)

    category1 = Category(
        "Смартфоны",
        "Смартфоны, как средство не только коммуникации, но и получения дополнительных функций для удобства жизни",
        [product1, product2, product3],
    )

    print(category1.name == "Смартфоны")
    print(category1.description)
    print(len(category1.products))
    print(category1.category_count)
    print(category1.product_count)

    product4 = Product('55" QLED 4K', "Фоновая подсветка", 123000.0, 7)
    category2 = Category(
        "Телевизоры",
        "Современный телевизор, который позволяет наслаждаться просмотром, станет вашим другом и помощником",
        [product4],
    )

    print(category2.name)
    print(category2.description)
    print(len(category2.products))
    # Выводим информацию о продуктах в категории
    for product in category2.products:
        print(
            f"Продукт: {product.name}, Описание: {product.description}, Цена: {product.price},\
             Количество: {product.quantity}")

    print(Category.category_count)
    print(Category.product_count)
