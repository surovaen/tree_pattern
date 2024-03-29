from node.tree_component import BTree
from scripts.convert import ProductJsonConverter
from scripts.generate import ProductJsonGenerator


if __name__ == '__main__':
    products_json = ProductJsonGenerator.execute()
    products_objs = ProductJsonConverter.execute(products_json)

    tree = BTree()
    for product in products_objs:
        tree.add(product)

    tree.to_json()
