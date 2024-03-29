import json
from typing import List, Optional

from config import Config
from node.base import Component


class BTree(Component):
    """Класс формирования дерева."""

    def __init__(self):
        super().__init__()
        self.children: List[Node] = []

    def add(self, leaf: 'Product') -> None:
        """Метод формирования узлов и добавления листа."""
        self.keys.add(leaf.price)
        self._add(leaf.price, leaf)

    def _add(self, price: int, leaf: Optional['Product'], start_component: int = -1) -> None:
        """Метод формирования узлов и добавления листа."""
        for idx, child in enumerate(self.children[start_component + 1:]):
            if not child.is_full:
                return child.add_leaf(leaf)

            if price < child.max_key:
                idx = idx + start_component + 1
                return self.split_children(idx, leaf)

            if price == child.max_key or price == child.min_key:
                return child.add_leaf(leaf)

        child = Node()
        self.children.append(child)
        return child.add_leaf(leaf)

    def split_children(self, start_component: int, leaf: Optional['Product']) -> None:
        """Метод разделения узлов."""
        child = self.children[start_component]
        child.add_leaf(leaf)

        removed_key = child.max_key
        leaves = child.remove_leaf(removed_key)
        self._add(removed_key, leaves, start_component)

    def to_json(self) -> str:
        """Формирование данных дерева в формате JSON."""
        child_data = {}

        for child in self.children:
            child_data.update(child.to_json())

        root_data = {
            '{left} - {right}'.format(left=self.min_key, right=self.max_key): child_data
        }

        with open('result.json', 'w') as f:
            json.dump(root_data, f, indent=4, separators=(',', ': '))

        return json.dumps(root_data)


class Node(Component):
    """Класс узла."""

    def __init__(self):
        super().__init__()
        self.children: List[Product] = []

    @property
    def is_full(self) -> bool:
        """Определяет, заполнены ли ключи узла."""
        return len(self.keys) == Config.MAX_KEYS

    def add_leaf(self, leaf: Optional['Product']) -> None:
        """Добавление листа в узел."""
        if isinstance(leaf, list):
            for item in leaf:
                self.keys.add(item.price)
                self.children.append(item)
        else:
            self.keys.add(leaf.price)
            self.children.append(leaf)

    def remove_leaf(self, price: int) -> List['Product']:
        """Удаление листа из узла."""
        self.keys.discard(price)
        leaves = [
            leaf for leaf in self.children if leaf.price == price
        ]
        for leaf in leaves:
            self.children.remove(leaf)
        return leaves

    def to_json(self) -> dict:
        """Формирование данных узла в формате словаря."""
        leaves_data = sorted([leaf.to_json() for leaf in self.children], key=lambda leaf: leaf['price'])
        data = {
            '{left} - {right}'.format(left=self.min_key, right=self.max_key): leaves_data
        }
        return data


class Product(Component):
    """Класс листа (товара)"""

    def __init__(self, name: str, price: int):
        self.name = name
        self.price = price
        super().__init__()

    def to_json(self) -> dict:
        """Формирование данных листа в формате словаря."""
        data = {
            'name': self.name,
            'price': self.price,
        }
        return data
