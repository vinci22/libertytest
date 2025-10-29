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

---

# Overall Architecture and Design Explanation

## Table of Contents
1. [Inventory Management System (Strategy Pattern + SOLID + OOP)](#question-1-inventory-management-system-strategy-pattern--solid--oop)
2. [AppTracer — Custom Observability Wrapper (Singleton + Context Manager + SOLID)](#question-2-apptracer--custom-observability-wrapper-singleton--context-manager--solid)
3. [Overall Architectural Integration](#overall-architectural-integration)
4. [Summary Table](#summary-table)
5. [Serverless Compute (AWS Lambda)](#serverless-compute-aws-lambda)

---

## Question 1: Inventory Management System (Strategy Pattern + SOLID + OOP)

### Architectural Overview
The system is structured around a modular and extensible object-oriented architecture.
It models real-world entities such as `Product`, `Inventory`, and `PricingStrategy` as classes with clear responsibilities and well-defined abstractions.

This design allows the system to easily incorporate new product types or discount mechanisms without modifying existing code, following the **Open/Closed Principle (OCP)**.

### Key OOP Principles and SOLID Application
1. **Single Responsibility Principle (SRP)** — Each class has a single, well-defined responsibility.
2. **Open/Closed Principle (OCP)** — The system supports new product or discount types without modifying existing code.
3. **Liskov Substitution Principle (LSP)** — Subclasses such as `StandardProduct` and `SubscriptionProduct` can replace the base class `Product`.
4. **Interface Segregation Principle (ISP)** — `PricingStrategy` provides a focused interface.
5. **Dependency Inversion Principle (DIP)** — `Product` depends on the abstract `PricingStrategy` rather than concrete implementations.

### Design Patterns Used
* **Strategy Pattern** — Enables dynamic selection of pricing strategies.
* **Composition over Inheritance** — Products *use* a strategy instance.
* **Polymorphism** — Product and strategy hierarchies allow flexible behavior.

### Benefits
* High cohesion and separation of concerns.
* Easy maintenance and scalability.
* Extensible product and pricing models through polymorphism.
* Improved testability due to dependency injection of strategies.

---

## Question 2: AppTracer — Custom Observability Wrapper (Singleton + Context Manager + SOLID)

### Architectural Overview
`AppTracer` is designed as a singleton-based observability utility that provides structured logging and tracing capabilities.
It maintains a `trace_id` and `span_id` for correlated logs across nested operations.

### Key OOP Principles and SOLID Application
1. **Single Responsibility Principle (SRP)** — `AppTracer` focuses on logging and trace management.
2. **Open/Closed Principle (OCP)** — Extendable via subclassing.
3. **Liskov Substitution Principle (LSP)** — Subclasses can replace the base implementation.
4. **Interface Segregation Principle (ISP)** — Minimal, cohesive API.
5. **Dependency Inversion Principle (DIP)** — Uses standard libraries, not external telemetry.

### Design Patterns Used
* **Singleton Pattern** — Ensures one instance manages tracing globally.
* **Context Manager Pattern** — `span()` manages lifecycle through `__enter__`/`__exit__`.
* **Encapsulation** — Private internal state prevents external tampering.

### Benefits
* Centralized and consistent trace management.
* Simplified nested tracing through context management.
* Decoupled from external systems.
* Extensible for integration with distributed tracing tools.

---

## Overall Architectural Integration
Both systems share a consistent philosophy grounded in OOP and SOLID:

* **Encapsulation** — Each class manages its own logic.
* **Polymorphism** — Behavior changes through abstraction.
* **Separation of Concerns** — Clear boundaries between modules.
* **Extensibility** — New features without altering existing code.

---

## Summary Table

| Concept           | Inventory System (Q1)            | AppTracer (Q2)                      |
| ----------------- | -------------------------------- | ----------------------------------- |
| **Main Pattern**  | Strategy Pattern                 | Singleton + Context Manager         |
| **Abstraction**   | Product, PricingStrategy         | AppTracer Interface                 |
| **Encapsulation** | Product data + strategy injection| Trace/Span state encapsulated       |
| **Polymorphism**  | Product and strategy hierarchies | Extendable tracer logic             |
| **SOLID Applied** | SRP, OCP, LSP, ISP, DIP          | SRP, OCP, LSP, DIP                  |
| **Extensibility** | New product or pricing types     | New output or integration layers    |
| **Main Benefit**  | Flexible pricing logic           | Centralized observability           |

---

# Serverless Compute (AWS Lambda)

## Scenario 1: Lambda Timeout and Performance

**Problem:**  
A Lambda function processing files from S3 occasionally fails with the error:  
`Task timed out after 30.00 seconds`.  
Average successful execution time: 10–15 seconds.

**Question:**  
Order the three most effective and recommended troubleshooting/resolution steps.

**Answer (in order):**
1. Use AWS X-Ray to trace the function’s execution path and identify the specific external service call causing the delay.  
2. Review the Lambda function’s code and dependencies for unoptimized loops, blocking calls, or recursive logic.  
3. Increase the Lambda function’s memory allocation to improve performance and reduce execution time.

**Explanation:**  
- Step 1 focuses on identifying the root cause using AWS X-Ray.  
- Step 2 addresses potential inefficiencies in the code itself.  
- Step 3 optimizes performance by providing more vCPU through higher memory allocation.  
Increasing the timeout or enabling provisioned concurrency does not solve the underlying issue.

---

## Scenario 2: Lambda and Networking

**Problem:**  
A Lambda function needs to connect to an Amazon RDS Aurora Serverless database (inside a VPC) but fails with a connection timeout error.

**Question:**  
What is the most likely initial misconfiguration?

**Answer:**  
B. The Lambda function has not been configured to run inside the VPC where the RDS database resides.

**Explanation:**  
RDS Aurora Serverless databases are accessible only within their VPC.  
If the Lambda function is not attached to that VPC (with proper subnets and security groups), it cannot reach the database endpoint.  
IAM permissions or Internet Gateway routes do not affect internal VPC connectivity.
