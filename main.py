from product import Product
from product_manager import ProductManager

product_manager=ProductManager()

product1=Product("Laptop",1200,65)
product2=Product("iPhone",890,87)
product3=Product("Earphones",15,980)

product_manager.add_product(product1)
product_manager.add_product(product2)
product_manager.add_product(product3)

product_manager.display_all_info()

total_value=product_manager.total_value()
print(f"Total amount is : {total_value}")