from typing import List
from .products import Product


class Inventory:
    def __init__(self):
        self.products: List[Product] = []

    def add_product(self, product: Product):
        self.products.append(product)

    def get_total_inventory_value(self) -> float:
        return sum(product.calculate_total_price() for product in self.products)

    def __repr__(self):
        return f"Inventory(total_items={len(self.products)}, total_value={self.get_total_inventory_value():.2f})"
