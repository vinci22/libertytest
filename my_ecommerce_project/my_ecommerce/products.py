from abc import ABC, abstractmethod
from .pricing import PricingStrategy, NoDiscountStrategy


class Product(ABC):
    def __init__(self, name: str, sku: str, price: float, quantity: int, strategy: PricingStrategy = None):
        self.name = name
        self.sku = sku
        self.price = price
        self.quantity = quantity
        self.strategy = strategy or NoDiscountStrategy()

    @abstractmethod
    def calculate_total_price(self) -> float:
        pass

    def __repr__(self) -> str:
        return f"<Product name={self.name} sku={self.sku} price={self.price} qty={self.quantity}>"

class StandardProduct(Product):
    def calculate_total_price(self) -> float:
        base_total = self.price * self.quantity
        return self.strategy.apply_discount(self, base_total)


class SubscriptionProduct(Product):
    def __init__(self, name: str, sku: str, price: float, quantity: int, subscription_period_months: int, strategy: PricingStrategy = None):
        super().__init__(name, sku, price, quantity, strategy)
        self.subscription_period_months = subscription_period_months

    def calculate_total_price(self) -> float:
        base_total = self.price * self.quantity * self.subscription_period_months
        return self.strategy.apply_discount(self, base_total)
