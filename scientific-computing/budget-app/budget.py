class Category:
    def __init__(self, category):
        self.name = category
        self.ledger = list()
        self.balance = 0

    def __str__(self):
        text = self.name.center(30, "*")+"\n"
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
        if self.check_funds(amount):
            self.ledger.append({'amount': -amount, 'description': description})
            self.balance -= amount
            return True

        else:
            return False

    def get_balance(self):
        return self.balance

    def transfer(self, amount, at):
        if self.check_funds(amount):
            self.withdraw(amount, f"Transfer to {at.name}")
            at.deposit(amount, f"Transfer from {self.name}")
            return True
        else:
            return False


# Extremely clunky and ugly code!
# Redo if possible
def create_spend_chart(categories):

    names = list()
    wthdr = list()  # List containing withdrawn amount in each category
    # Computes the percentage spent
    for cat in categories:
        names.append(cat.name)
        spent = 0
        for item in cat.ledger:
            if item['amount'] <= 0:
                spent += abs(item['amount'])
        wthdr.append(spent)

    totalSpent = sum(wthdr)
    perSpent = [round(s*100/totalSpent) for s in wthdr]
    # print(perSpent)

    # Creating the text output
    # Create first line title
    line = 'Percentage spent by category'+'\n'
    for y in range(100, -1, -10):
        auxLine = ""
        # Creates an array keeping track of the o's
        for perc in perSpent:
            if perc >= y:
                auxLine += "o  "
            else:
                auxLine += "   "
        # Creates line of the graph
        line += str(y).rjust(3, " ")+"| " + auxLine + "\n"
    # Creates line of dashes ---
    line += "    "+"-"*(1+3*len(categories)) + "\n"

    # Figures out spacing for the vertical letters
    maxName = max(names, key=len)
    L = len(maxName)
    rjustNames = [name.ljust(L, " ") for name in names]

    # almost_all_names = rjustNames[:-1]

    # Creates vertical words
    for i in range(0, L):
        line += " "*5
        for word in rjustNames:
            line += word[i]+" "*2
        # The last line should not en in a linebreak,
        # thus the following conditional
        if i != L-1:
            line += "\n"

    return line
