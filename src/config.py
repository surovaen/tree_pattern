import os

from dotenv import load_dotenv

dotenv_path = './.env'
load_dotenv(dotenv_path)


class Config:
    """Класс настроек."""

    PRODUCT_COUNT = int(os.environ.get('PRODUCT_COUNT', 50))
    MIN_PRICE = int(os.environ.get('MIN_PRICE', 1))
    MAX_PRICE = int(os.environ.get('MAX_PRICE', 1000))
    MAX_KEYS = int(os.environ.get('MAX_KEYS', 5))
