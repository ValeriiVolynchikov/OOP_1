class ZeroQuantityError(Exception):
    """Исключение для обработки попытки добавления товара с нулевым количеством."""

    def __init__(self, message="Товар с нулевым количеством не может быть добавлен"):
        self.message = message
        super().__init__(self.message)
#
# class InvalidProductError(Exception):
#     """Исключение для случаев, когда товар недопустим."""
#     def __init__(self, message="Товар не может быть добавлен из-за недопустимого состояния."):
#         self.message = message
#         super().__init__(self.message)
