# Shopping Cart Bill Calculator
print("Welcome to the Bal Krishna Shopping Cart!")

# List of items and their prices
cart = [
    {"item": "Apples", "price": 100},
    {"item": "Bananas", "price": 50},
    {"item": "Milk", "price": 70},
    {"item": "Bread", "price": 40},
]
total_bill = 0

# For loop to calculate the total bill
for product in cart:
    print("Adding %s - ₹%s to your cart." % (product["item"], product["price"]))
    total_bill += product["price"]

print("\nYour total bill amount is: ₹%s" % total_bill)
print("Thank you for shopping with us!")
