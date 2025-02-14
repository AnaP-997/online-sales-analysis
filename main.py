import random
from product import Product
from cart import Cart
from product_manager import ProductManager

product_manager=ProductManager()

product1=Product("Laptop",1200,65)
product2=Product("iPhone",890,87)
product3=Product("Earphones",15,980)
product4=Product("Tablet",890,89)
product5=Product("USB",24,980)
product6=Product("Mouse",7,567)

product_manager.add_product(product1)
product_manager.add_product(product2)
product_manager.add_product(product3)

product_manager.display_all_info()

total_value=product_manager.total_value()
print(f"Total amount is : {total_value}")

cart_instance=Cart()

random_products=random.sample(product_manager.products,3)

for product in random_products:
    cart_instance.add_product_cart(product)
    
cart_instance.display_cart_info()

total_value=cart_instance.total_sum()
print(f"Ukupni iznos korpe je: {total_value}")