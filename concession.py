menu = {"Burger" : 300,
        "Pizza" : 700,
        "Pasta" : 250,
        "Cold-drinks" : 60,
        "French Fry" : 100,
        "Wedges" : 150,
        "Shawarma" : 150,
        "Water" : 30}

cart = []
price = 0

print("___________ Menu ___________")
for key, value in menu.items():
    print(f"{key:<15} : {value:>5} Taka")
print("___________ Menu ___________")

while True:
    food = input("What do you want to buy? (press 'q' to quit): ")

    if food.lower() == "q":
        break
    elif menu.get(food.capitalize()) is not None:
        cart.append(food.capitalize())
    else:
        print("The item is not available")

print("___________ Your Order ___________")
for food in cart:
    price += menu.get(food)
    print(food, end=" ")

print()
print(f"Total is: {price} Taka")
print()
print("________Thanks for coming!________")