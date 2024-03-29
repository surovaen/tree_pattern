import json
import random
from typing import List

from config import Config


class ProductJsonGenerator:
    """Класс-генератор данных по товарам в формате JSON."""

    @classmethod
    def execute(cls) -> str:
        """Метод генерации данных по товарам в формате JSON."""
        data = cls._get_data()
        product_json = cls._to_json(data)
        return product_json

    @classmethod
    def _get_data(cls) -> List[dict]:
        """Метод формирования списка товаров."""
        products = [
            {
                'name': 'Product {num}'.format(num=i),
                'price': cls._generate_product_price(),
            } for i in range(Config.PRODUCT_COUNT)
        ]

        return products

    @classmethod
    def _generate_product_price(cls) -> int:
        """Метод генерации цены товара."""
        return random.randint(
            Config.MIN_PRICE,
            Config.MAX_PRICE,
        )

    @classmethod
    def _to_json(cls, data: List[dict]) -> str:
        """Метод преобразования данных в формат JSON."""
        return json.dumps(data)


