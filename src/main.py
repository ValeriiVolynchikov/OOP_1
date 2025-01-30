from src.product import Product
from src.category import Category
from src.iterator import CategoryIterator

if __name__ == '__main__':
    product1 = Product("Samsung Galaxy S23 Ultra", "256GB, Серый цвет, 200MP камера", 180000.0, 5)
    product2 = Product("Iphone 15", "512GB, Gray space", 210000.0, 8)
    product3 = Product("Xiaomi Redmi Note 11", "1024GB, Синий", 31000.0, 14)

    print(str(product1))
    print(str(product2))
    print(str(product3))

    category1 = Category("Смартфоны", "Смартфоны, как средство не только коммуникации, но и получения дополнительных функций для удобства жизни")
    category1.add_product(product1)
    category1.add_product(product2)
    category1.add_product(product3)

    print(str(category1))
    print(category1.products)

    print(product1 + product2)
    print(product1 + product3)
    print(product2 + product3)

    # Пример использования итератора
    iterator = CategoryIterator(category1)
    for product in iterator:
        print(product)

# if __name__ == "__main__":
#     # Создаем продукты
#     product1 = Product("Samsung Galaxy S23 Ultra", "256GB, Серый цвет, 200MP камера", 180000.0, 5)
#     product2 = Product("Iphone 15", "512GB, Gray space", 210000.0, 8)
#     product3 = Product("Xiaomi Redmi Note 11", "1024GB, Синий", 31000.0, 14)
#
#     # Создаем категорию
#     category1 = Category(
#         "Смартфоны",
#         "Смартфоны, как средство не только коммуникации, но и получения дополнительных функций для удобства жизни",
#     )
#
#     # Добавляем продукты в категорию
#     category1.add_product(product1)
#     category1.add_product(product2)
#     category1.add_product(product3)
#
#     # Выводим список продуктов в категории
#     print(category1.products)
#
#     # Добавляем новый продукт
#     product4 = Product('55" QLED 4K', "Фоновая подсветка", 123000.0, 7)
#     category1.add_product(product4)
#     print("\nПосле добавления нового продукта:")
#     print(category1.products)
#
#     # Проверка работы класса-метода
#     new_product = Product.new_product(
#         {
#             "name": "Samsung Galaxy S23 Ultra",
#             "description": "256GB, Серый цвет, 200MP камера",
#             "price": 180000.0,
#             "quantity": 5,
#         }
#     )
#     print("\nСоздан новый продукт:")
#     print(new_product.name)
#     print(new_product.description)
#     print(new_product.price)
#     print(new_product.quantity)
#
#     # Проверка работы сеттера
#     new_product.price = 800
#     print("\nОбновленная цена продукта:", new_product.price)
#
#     new_product.price = -100  # Должно вывести предупреждение
#     print("Цена после неудачной попытки обновления:", new_product.price)
