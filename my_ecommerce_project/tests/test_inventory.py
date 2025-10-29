import pytest
import os
import sys
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

from my_ecommerce.products import StandardProduct, SubscriptionProduct
from my_ecommerce.pricing import NoDiscountStrategy, BulkDiscountStrategy
from my_ecommerce.inventory import Inventory


def test_standard_product_total():
    p = StandardProduct('A', 'SKU-A', 2.0, 3, strategy=NoDiscountStrategy())
    assert p.calculate_total_price() == 6.0

def test_subscription_product_total():
    p = SubscriptionProduct('S', 'SKU-S', 1.0, 2, subscription_period_months=6, strategy=NoDiscountStrategy())
    assert p.calculate_total_price() == 12.0

def test_bulk_discount_applies():
    p = StandardProduct('Bulk', 'SKU-B', 10.0, 20, strategy=BulkDiscountStrategy())
    total = p.calculate_total_price()
    assert pytest.approx(total, rel=1e-6) == 10.0 * 20 * 0.9

def test_inventory_total_value():
    inv = Inventory()
    inv.add_product(StandardProduct('A', 'SKU-A', 2.0, 3, strategy=NoDiscountStrategy()))
    inv.add_product(StandardProduct('Bulk', 'SKU-B', 10.0, 20, strategy=BulkDiscountStrategy()))
    assert inv.get_total_inventory_value() > 0
