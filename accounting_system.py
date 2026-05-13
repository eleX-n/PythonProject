class Manager:
    def __init__(self):
        self.actions = {}

    # ----- ASSIGN DECORATOR -----
    def assign(self, name):
        def decorator(func):
            self.actions[name] = func
            return func
        return decorator

    # ----- LOG DECORATOR -----
    def log(self, func):
        def wrapper(*args, **kwargs):
            print(f"Executing {func.__name__}")
            result = func(*args, **kwargs)
            print(f"Finished {func.__name__}")
            return result
        return wrapper

    # ----- EXECUTE ACTION -----
    def execute(self, name, *args, **kwargs):
        if name not in self.actions:
            print("Action not found")
            return None

        return self.actions[name](*args, **kwargs)


# ===================== ACCOUNTING SYSTEM =====================
account = {
    "balance": 1000,
    "inventory": {}
}

manager = Manager()


# ===================== ACTIONS =====================

@manager.assign("sale")
@manager.log
def sale(account, product, price, quantity):
    total = price * quantity

    if product in account["inventory"] and account["inventory"][product] >= quantity:
        account["inventory"][product] -= quantity
        account["balance"] += total
        print(f"Sold {quantity} of {product} for {total}")
    else:
        print("Not enough product in inventory")


@manager.assign("purchase")
@manager.log
def purchase(account, product, price, quantity):
    total = price * quantity

    if account["balance"] >= total:
        account["balance"] -= total
        account["inventory"][product] = account["inventory"].get(product, 0) + quantity
        print(f"Purchased {quantity} of {product} for {total}")
    else:
        print("Not enough balance")


@manager.assign("balance")
@manager.log
def balance(account):
    print(f"Current balance: {account['balance']}")


@manager.assign("inventory")
@manager.log
def inventory(account):
    print("Inventory:")
    if not account["inventory"]:
        print("Empty")
    else:
        for product, qty in account["inventory"].items():
            print(f"{product}: {qty}")


# ===================== TEST =====================
manager.execute("purchase", account, "apple", 2, 10)
manager.execute("purchase", account, "banana", 1, 20)

manager.execute("inventory", account)
manager.execute("balance", account)

print()

manager.execute("sale", account, "apple", 3, 5)

manager.execute("inventory", account)
manager.execute("balance", account)