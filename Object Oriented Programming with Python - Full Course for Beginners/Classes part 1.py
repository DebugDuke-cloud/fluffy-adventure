class Item:
    def calculate_total_price(self,x,y):
     return x * y

item1 = Item()
item1.name = "Phone"
item1.price = 100
item1.quantity = 5
item1.calculate_total_price(item1.price, item1.quantity)

item2 = Item()
item2.name = 'Laptop'
item2.price = 1000
item2.quantity = 3

print(item1)
print(item1.name)
print(item1.price)
print(item1.quantity)
print(item1.calculate_total_price,item1.price,item1.quantity)

print(item2)
print(item2.name)
print(item2.price)
print(item2.quantity)
print(item2.calculate_total_price,item2.price,item2.quantity)


# # For classes with a string example
# random_str = "aaa"
# print(random_str.upper())

