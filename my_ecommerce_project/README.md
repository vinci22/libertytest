# 🛒 My E-Commerce Project

This project implements:

1. **Inventory Management System (Strategy Pattern)**
   - Abstract `Product` base class
   - Concrete products: `StandardProduct`, `SubscriptionProduct`
   - Pricing strategies: `NoDiscountStrategy`, `BulkDiscountStrategy`
   - Inventory aggregation

2. **Custom Observability Wrapper (Singleton + Context Manager)**
   - `AppTracer` handles trace and span management
   - Structured logging with correlation IDs

## 🚀 Run locally
```bash
python src/my_ecommerce/demo_inventory.py
python src/my_ecommerce/demo_tracer.py
```

## 🐳 Run with Docker
```bash
docker build -t ecommerce-demo .
docker run --rm ecommerce-demo
```
