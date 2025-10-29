from abc import ABC, abstractmethod


class PricingStrategy(ABC):
    @abstractmethod
    def apply_discount(self, product, total_price: float) -> float:
        pass


class NoDiscountStrategy(PricingStrategy):
    def apply_discount(self, product, total_price: float) -> float:
        return total_price


class BulkDiscountStrategy(PricingStrategy):
    """Applies 10% discount when quantity >= 20"""
    def apply_discount(self, product, total_price: float) -> float:
        if getattr(product, 'quantity', 0) >= 20:
            return total_price * 0.9
        return total_price
