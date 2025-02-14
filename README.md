# online-sales-analysis

Description: Programme that contains three separate classes in three separate files, along with the main programme. Each of the classes have their own functionality. 

Class Product in product.py deals with setting up initial methods for products (like def __init__ (self,...),displaying the info about name,price, quantity for the desired product, and updates quantity status).

Class ProductManager in product_manager.py has more methods (initializing an empty list and adding products to this list, contains a method for displaying all objects in the list,sums up total value of the list, loops over a list and deletes the object that the user wants)

Class Cart in cart.py contains similar methods to ProductManager class. It has its own list, sums the total purchased value of the list (user's list). It also has a method for displaying information about every product in the list.

main.py represents the main programme of the project. This is where we call the methods and use them on instances of the previous classes that we have created. It also has additional "import random" method,which allows us to link the cart_instance.add_products_cart(product) method to product_manager.products list by implementing a method, that allows to randomly select products from product_manager.products and add them to the cart_instance, which was also initiated in the cart.py as a list. So we create a list by randomly selecting other products from the previously created list. 