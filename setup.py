from setuptools import setup, find_packages

setup(
    name="my_ecommerce",
    version="1.0.0",
    description="E-commerce inventory and tracing system (challenge solution)",
    author="Dario Arteaga",
    packages=find_packages(where="src"),
    package_dir={"": "src"},
    python_requires=">=3.8",
)
