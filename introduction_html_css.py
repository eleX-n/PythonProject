from flask import Flask, render_template, request, redirect, url_for

app = Flask(__name__)


# ===================== DATABASE =====================
account_balance = 1000.0

warehouse = {
    "Apples": 20,
    "Bananas": 15,
    "Oranges": 8
}

history = []


# ===================== HOME =====================
@app.route("/")
def index():
    return render_template(
        "index.html",
        balance=account_balance,
        warehouse=warehouse
    )


# ===================== PURCHASE =====================
@app.route("/purchase/", methods=["GET", "POST"])
def purchase():
    global account_balance

    error = None

    if request.method == "POST":
        try:
            product = request.form["product"]
            price = float(request.form["price"])
            quantity = int(request.form["quantity"])

            if price < 0 or quantity <= 0:
                raise ValueError

            total = price * quantity

            if account_balance < total:
                error = "Not enough balance."
            else:
                account_balance -= total

                warehouse[product] = warehouse.get(product, 0) + quantity

                history.append(
                    f"Purchased {quantity} {product} for ${total:.2f}"
                )

                return redirect(url_for("index"))

        except:
            error = "Invalid data."

    return render_template("purchase.html", error=error)


# ===================== SALE =====================
@app.route("/sale/", methods=["GET", "POST"])
def sale():
    global account_balance

    error = None

    if request.method == "POST":
        try:
            product = request.form["product"]
            price = float(request.form["price"])
            quantity = int(request.form["quantity"])

            if price < 0 or quantity <= 0:
                raise ValueError

            if warehouse.get(product, 0) < quantity:
                error = "Not enough products in warehouse."
            else:
                warehouse[product] -= quantity

                total = price * quantity
                account_balance += total

                history.append(
                    f"Sold {quantity} {product} for ${total:.2f}"
                )

                return redirect(url_for("index"))

        except:
            error = "Invalid data."

    return render_template("sale.html", error=error)


# ===================== BALANCE =====================
@app.route("/balance/", methods=["GET", "POST"])
def balance():
    global account_balance

    error = None

    if request.method == "POST":
        try:
            operation = request.form["operation"]
            amount = float(request.form["amount"])

            if amount < 0:
                raise ValueError

            if operation == "add":
                account_balance += amount

                history.append(
                    f"Balance increased by ${amount:.2f}"
                )

            elif operation == "subtract":
                if account_balance < amount:
                    error = "Not enough balance."
                else:
                    account_balance -= amount

                    history.append(
                        f"Balance decreased by ${amount:.2f}"
                    )

            return redirect(url_for("index"))

        except:
            error = "Invalid data."

    return render_template("balance.html", error=error)


# ===================== HISTORY =====================
@app.route("/history/")
@app.route("/history/<int:line_from>/<int:line_to>/")
def show_history(line_from=None, line_to=None):

    if line_from is None or line_to is None:
        selected_history = history
    else:
        selected_history = history[line_from:line_to]

    return render_template(
        "history.html",
        history=selected_history
    )


# ===================== RUN =====================
if __name__ == "__main__":
    app.run(debug=True)