# menu
menu = {
    "pizza": 300,
    "burger": 100,
    "chicken soup": 150,
    "salad": 50,
    "meat": 80,
    "rice": 20,
    "desserts": 180,
    "fries": 60
}

# greet
print("Welcome to our Python Hotel!")

print("Menu:")
print("Pizza : 300 BDT")
print("Burger : 100 BDT")
print("Chicken Soup : 150 BDT")
print("Salad : 50 BDT")
print("Meat : 80 BDT")
print("Rice : 20 BDT")
print("Desserts : 180 BDT")
print("Fries : 60 BDT")

order_total = 0
item_1 = input(" Enter the dish name that you want to order =")
if item_1 in menu:
    order_total += menu[item_1]
    print(f"Your order {item_1} has been Added into your order list")
else:
    print(" The dish you ordered it is not Available for now please enter another dish that we can serve you")
another_order = input("Do you want to order something else ? (YES OR NO)")
if another_order == "yes":
    item_2 = input(" Enter the name of the second dish you want to order =")
    if item_2 in menu:
        order_total += menu[item_2]

        print(f"Your order {item_2} has been Added into your order list")
else:
    print(" The dish you ordered it is not Available for now please enter another dish that we can serve you")

print(" The total bill you have to pay is :",order_total,f"BDT")