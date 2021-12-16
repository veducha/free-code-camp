class Category:
    def __init__(self, category):
        self.category = category
        self.ledger = list()
        self.balance = 0

    def __str__(self):
        text = self.category.center(30, "*")+"\n"
        for item in self.ledger:
            d = item["description"]
            a = item["amount"]

            # Here we use slicing of strings, left-justified method of strings
            # and format codes to insert the number a in the right shape
            newline = d[:23].ljust(23, " ") + "{:7.2f}".format(a) + "\n"
            text += newline
        text += "Total: {0:.2f}".format(self.balance)
        return text

    def check_funds(self, amount):
        if self.balance-amount >= 0:
            return True
        else:
            return False

    def deposit(self, amount, description=""):
        self.ledger.append({'amount': amount, 'description': description})
        self.balance += amount

    def withdraw(self, amount, description=""):
        if self.check_funds(amount) >= 0:
            self.ledger.append({'amount': -amount, 'description': description})
            self.balance -= amount
            return True

        else:
            return False

    def get_balance(self):
        return self.balance

    def transfer(self, amount, budgetCat):
        if self.check_funds(amount):
            self.withdraw(amount, f"Transfer to {budgetCat.category}")
            budgetCat.deposit(amount, f"Transfer from {self.category}")
            return True
        else:
            return False


def create_spend_chart(categories):
    pass
