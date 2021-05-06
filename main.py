class Customer:
    def __init__(self, name, email):
        self.name = name
        self.email = email
        self.purchases = []

    def purchase(self, inventory_dict, product):
        # inventory_dict = inventory_obj.inventory
        if product in inventory_dict:
            if inventory_dict[product] > 0:
                self.purchases.append(product)
                inventory_dict[product] -=1
            else:
                print("Out of stock.")
        else:
            print("We don't have this product.")

    def print_purchases(self):
        for item in self.purchases:
            print(item.name)




class Product:
    def __init__(self, name, price):
        self.name = name
        self.price = price


class Inventory:
    def __init__(self):
        self.inventory = {
            mac: 100
        }

    def add_product(self, product, quantity):
        if product not in self.inventory:
            self.inventory[product] = quantity
        else:
            self.inventory[product]+=quantity

    def print_inventory(self):
        for key, value in self.inventory.items():
            print(key.name + ":" + str(value))
        print()





customer = Customer("Joe", "joe.be@gmail.com")

apple_watch = Product("Apple Watch", 299)
mac = Product("Mac", 1299)

inventory = Inventory()
inventory.add_product(apple_watch, 10)
inventory.print_inventory()
inventory.add_product(mac, 100)
customer.purchase(inventory.inventory, mac)
inventory.print_inventory()