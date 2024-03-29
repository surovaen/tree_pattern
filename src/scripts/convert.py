import json

from node.tree_component import Product


class ProductJsonConverter:
    """Класс-обработчик данных продуктов."""

    @classmethod
    def execute(cls, json_data: str):
        """Метод преобразования данных JSON в объекты."""
        product_data = json.loads(json_data)
        products = [Product(**product) for product in product_data]

        return products
