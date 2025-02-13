from product import Product
class ProductManager:
    
    def __init__(self):
        self.products=[]
        
    def add_product(self,product):
            self.products.append(product)
    
    def display_all_info(self):
        for product in self.products:
            product.display_info()
            
    def total_value(self):
        total=sum(product.quantity*product.price for product in self.products)
        return total
    
    def name_removal(self,name):
        self.products=[product for product in self.products if product.name != name]
        
        
        