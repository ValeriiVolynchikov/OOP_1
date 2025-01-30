from .category import Category

class CategoryIterator:
    """Класс для перебора товаров одной категории."""
    def __init__(self, category: Category):
        self._category = category
        self._index = 0

    def __iter__(self):
        return self

    def __next__(self):
        if self._index < len(self._category._products):
            product = self._category._products[self._index]
            self._index += 1
            return product
        else:
            raise StopIteration
