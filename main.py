def subtotal():
    payable_amount = price * quantity
    if payable_amount > 1000:
        payable_amount = payable_amount - (10/100)

class Items:
    def __init__(self, item_name, price, quantity):
        self.item_name = item_name
        self.price = price
        self.quantity = quantity

class Order:
    def __init(self, order_id, customer_name, items, status):
        self.order_id = order_id
        self.customer_name = customer_name
        self.items = Items
        self.status = status
            

print("---Add Order---")
int(input("Enter order id:"))
input("Enter customer name:")
input("Item name:")
int(input("Price:"))
int(input("Quantity:"))
