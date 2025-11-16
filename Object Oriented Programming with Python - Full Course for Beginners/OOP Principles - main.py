from phone import Phone
from keyboard import Keyboard

item1 = Keyboard("jscKeyboard", 1000, 3)

item1.apply_discount()  # Applying a discount of 10%

print(item1.price)