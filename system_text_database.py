import os
import json
from ast import literal_eval

# ===================== FILES =====================
BALANCE_FILE = "balance.txt"
INVENTORY_FILE = "inventory.txt"
HISTORY_FILE = "history.txt"


# ===================== LOAD FUNCTIONS =====================
def load_balance():
    try:
        if os.path.exists(BALANCE_FILE):
            with open(BALANCE_FILE, "r") as f:
                return float(f.read())
    except:
        pass
    return 1000.0  # default


def load_inventory():
    try:
        if os.path.exists(INVENTORY_FILE):
            with open(INVENTORY_FILE, "r") as f:
                return literal_eval(f.read())
    except:
        pass
    return {}


def load_history():
    try:
        if os.path.exists(HISTORY_FILE):
            with open(HISTORY_FILE, "r") as f:
                return literal_eval(f.read())
    except:
        pass
    return []


# ===================== SAVE FUNCTIONS =====================
def save_balance(balance):
    with open(BALANCE_FILE, "w") as f:
        f.write(str(balance))


def save_inventory(inventory):
    with open(INVENTORY_FILE, "w") as f:
        f.write(str(inventory))


def save_history(history):
    with open(HISTORY_FILE, "w") as f:
        f.write(str(history))


# ===================== INITIAL STATE =====================
balance = load_balance()
inventory = load_inventory()
history = load_history()


# ===================== OPERATIONS =====================
def purchase(product, price, qty):
    global balance, inventory, history

    total = price * qty

    if balance >= total:
        balance -= total
        inventory[product] = inventory.get(product, 0) + qty

        history.append(f"PURCHASE {product} x{qty} cost={total}")
        print(f"Purchased {qty} {product}")
    else:
        print("Not enough balance")


def sale(product, price, qty):
    global balance, inventory, history

    if inventory.get(product, 0) >= qty:
        inventory[product] -= qty
        total = price * qty
        balance += total

        history.append(f"SALE {product} x{qty} gain={total}")
        print(f"Sold {qty} {product}")
    else:
        print("Not enough stock")


def show_balance():
    print(f"Balance: {balance}")


def show_inventory():
    print("Inventory:")
    if not inventory:
        print("Empty")
    else:
        for k, v in inventory.items():
            print(k, ":", v)


def show_history():
    print("History:")
    for h in history:
        print("-", h)


# ===================== MAIN LOOP =====================
def main():
    try:
        while True:
            print("\nCommands: purchase, sale, balance, inventory, history, exit")
            cmd = input("> ").lower()

            if cmd == "purchase":
                p = input("Product: ")
                price = float(input("Price: "))
                qty = int(input("Quantity: "))
                purchase(p, price, qty)

            elif cmd == "sale":
                p = input("Product: ")
                price = float(input("Price: "))
                qty = int(input("Quantity: "))
                sale(p, price, qty)

            elif cmd == "balance":
                show_balance()

            elif cmd == "inventory":
                show_inventory()

            elif cmd == "history":
                show_history()

            elif cmd == "exit":
                break

            else:
                print("Invalid command")

    finally:
        # ===================== SAVE ON SHUTDOWN =====================
        save_balance(balance)
        save_inventory(inventory)
        save_history(history)
        print("\nData saved successfully.")


# ===================== RUN =====================
if __name__ == "__main__":
    main()