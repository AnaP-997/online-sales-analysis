from product import Product
import random

class Cart:
    
    def __init__(self):
        self.items=[]
    
    
    def add_product_cart(self,product):
        self.items.append(product)
        
    def total_sum(self):
        cart_total=sum(product.price*product.quantity for product in self.items)
        return cart_total
    
    def display_cart_info(self):
        for product in self.items:
            print(f"Product: {product.name}, price: {product.price}, quantity: {product.quantity}")