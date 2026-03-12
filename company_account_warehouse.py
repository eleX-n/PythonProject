inventory = {
    "book": {"price": 15, "quantity": 78},
    "pen": {"price": 2, "quantity": 50},
    "pencil": {"price": 1, "quantity": 45},
    "notebook": {"price": 5, "quantity": 70},
    "rubber": {"price": 0.50, "quantity": 36}
}

balance = 0
operations = []
commands = ["balance", "sale", "purchase", "account", "list", "warehouse", "review", "end"]



while True:

    print("\nAvailable commands:")
    for item in commands:
        print("-", item)

    command = input("\nEnter a command: ").lower()

    if command == "end":
            print("...ending the program...")
            break



    elif command == "balance":
            amount = float(input("Enter amount to add or subtract: "))
            balance = balance + amount
            operations.append(f"balance change: {amount}")
            print("Balance updated.")

    elif command == "sale":
            print("Sale: product name and quantity")
            product = input("Enter product name: ").lower()
            quantity = int(input("Enter quantity: "))

            if product in inventory:
                price = inventory[product]["price"]

                if inventory[product]["quantity"] >= quantity:
                    inventory[product]["quantity"] -= quantity
                    balance += price * quantity

                    operations.append(f"sale: {product}, price {price}, quantity {quantity}")
                    print("Sale recorded")
                else:
                    print("Not enough products in the warehouse")
            else:
                print("Product not found")



    elif command == "purchase":
            print("Purchase: name of the product, price and quantity")
            product = input("Enter product name: ").lower()
            price = float(input("Enter product price: "))
            quantity = int(input("Enter quantity: "))

            cost = price * quantity

            if balance >= cost:
                balance = balance - cost

                if product in inventory:
                    inventory[product]["quantity"] += quantity
                    inventory[product]["price"] = price
                else:
                    inventory[product] = {"price": price, "quantity": quantity}

                operations.append(f"purchase: {product}, price {price}, quantity {quantity}")
                print("Purchase recorded")
            else:
                print("Not enough balance")



    elif command == "account":
            print(f"Current account balance: {balance}")



    elif command == "LIST":
            if inventory:
                print("Total inventory in the warehouse:")
                for product, data in inventory.items():
                    price = data["price"]
                    quantity = data["quantity"]
                    print(f"{product}: price {price}, quantity {quantity}")



    elif command == "warehouse":
            product = input("Enter product name: ").lower()

            if product in inventory:
                data = inventory[product]
                print(f"{product}: price {data['price']}, quantity {data['quantity']}")
            else:
                print("Product not found in warehouse")



    elif command == "review":
            start = input("From index: ")
            end = input("To index: ")

            if start == "" and end == "":
                for op in operations:
                    print(op)
            else:
                start = int(start)
                end = int(end)

                if start < 0 or end > len(operations):
                    print("Index out of range")
                else:
                    for op in operations[start:end]:
                        print(op)

    else:
        print("Invalid command. Please enter a valid commands: Balance, Sale, Purchase, Account, List, Warehouse, Review, End.")



print()
print("End of the program")


