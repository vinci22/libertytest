from my_ecommerce.products import StandardProduct, SubscriptionProduct
from my_ecommerce.pricing import NoDiscountStrategy, BulkDiscountStrategy
from my_ecommerce.inventory import Inventory

def main():
    inv = Inventory()

    p1 = StandardProduct(name='Widget-A', sku='W-A-001', price=10.0, quantity=5, strategy=NoDiscountStrategy())
    p2 = StandardProduct(name='Widget-B', sku='W-B-002', price=8.0, quantity=25, strategy=BulkDiscountStrategy())
    p3 = SubscriptionProduct(name='Service-X', sku='S-X-001', price=5.0, quantity=3, subscription_period_months=12, strategy=NoDiscountStrategy())

    inv.add_product(p1)
    inv.add_product(p2)
    inv.add_product(p3)

    print('Products:')
    for p in inv.products:
        print(f' - {p} total={p.calculate_total_price():.2f}')

    total = inv.get_total_inventory_value()
    print(f'\nTotal inventory value: {total:.2f}')

if __name__ == '__main__':
    main()
