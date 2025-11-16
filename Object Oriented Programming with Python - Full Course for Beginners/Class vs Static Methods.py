import csv


class Item:
    pay_rate = 0.8     # The pay rate after 20% discount
    all = []

    def __init__(self, name: str, price: float, quantity=0):
        # Run Validations to the received arguments
        assert price >= 0, f"Price {price} is not greater than or equal to zero!"
        assert quantity >= 0, f"Quantity {quantity} is not greater or equal to zero!"

        # Assign to a self-object
        self.name = name
        self.price = price
        self.quantity = quantity

        # Append the instance to the all lists
        Item.all.append(self)

    # Actions to execute
    def calculate_total_price(self):
        return self.price * self.quantity

    def apply_discount(self):
        self.price = self.price * self.pay_rate

    @classmethod
    def instantiate_from_csv(cls):
        with open("items.csv", "r") as f:
            reader = csv.DictReader(f)
            items = list(reader)

        for item in items:
            Item(
                name = item.get("name"),
                price= float(item.get("price")),
                quantity=int(item.get("quantity")),
            )
    @staticmethod
    def is_integer(num):
        if isinstance(num, float):
            return num.is_integer()
        elif isinstance(num,int):
            return True
        else:
            return False
    def __repr__(self):
      return f"Item('{self.name}',{self.price}, {self.quantity})"

print(Item.is_integer(7.0))

# Item.instantiate_from_csv()
# print(Item.all)




# item1 = Item("Phone", 100, 1)
# item2 = Item("Laptop", 1000, 3)
# item3 = Item("Cable", 10, 5)
# item4 = Item("Mouse", 50, 5)
# item5 = Item("Keyboard", 75, 5)

# print(Item.all)