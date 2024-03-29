import abc
from typing import Optional


class Component(abc.ABC):
    """Базовый класс компонента дерева."""

    def __init__(self):
        self.keys = set()

    @property
    def min_key(self) -> int:
        """Минимальное значение ключа."""
        return min(self.keys)

    @property
    def max_key(self) -> int:
        """Максимальное значение ключа."""
        return max(self.keys)

    @property
    def is_full(self) -> Optional[bool]:
        """Определяет, заполнены ли ключи узла."""
        return None

    @abc.abstractmethod
    def to_json(self):
        """Формирование данных дерева в формате JSON."""
        pass
