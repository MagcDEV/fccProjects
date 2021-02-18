class Category:
    def __init__(self, name):
        self.name = name
        self.ledger = []

    def deposit(self, amount, description=""):
        self.ledger.append({"amount": amount, "description": description})

    def withdraw(self, amount, description=""):
        if self.check_funds(amount):
            self.ledger.append(
                {"amount": - amount, "description": description})
            return True
        else:
            return False

    def get_balance(self):
        balance = 0
        for x in self.ledger:
            balance += x["amount"]
        return balance

    def transfer(self, amount, category):
        if self.check_funds(amount):
            category.deposit(amount, "Transfer from " + self.name)
            self.withdraw(amount, "Transfer to " + category.name)
            return True

        else:
            return False

    def check_funds(self, amount):
        if amount > self.get_balance():
            return False
        else:
            return True

    def __str__(self):
        count = 1
        toPrint = ""
        for x in self.ledger:
            if count < len(self.ledger):
                toPrint += (x["description"] + "                       ")[0:23] + ("                       " +
                                                                                   str("{:.2f}".format(x["amount"])))[-7:] + "\n"
            else:
                toPrint += (x["description"] + "                       ")[0:23] + ("                       " +
                                                                                   str("{:.2f}".format(x["amount"])))[-7:]
            count += 1

        if len(self.name) % 2 == 0:
            return ("*" * int(((30 - (len(self.name))) / 2)) +
                    self.name + "*" * int(((30 - (len(self.name))) / 2))) + "\n" + toPrint + "\n" + "Total: " + str("{:.2f}".format(self.get_balance()))
        else:
            return ("*" * int(((30 - (len(self.name))) / 2)) + self.name +
                    "*" * int(((30 - (len(self.name))) / 2) + 1)) + "\n" + toPrint + "\n" + "Total: " + str("{:.2f}".format(self.get_balance()))


def create_spend_chart(categories):
    percList = []
    numList = ["100|", " 90|", " 80|", " 70|", " 60|",
               " 50|", " 40|", " 30|", " 20|", " 10|", "  0|"]
    totalCount = 0
    for x in categories:
        count = 0
        for y in x.ledger:
            if y["amount"] < 0:
                count += abs(y["amount"])
        totalCount += count
    for x in categories:
        count = 0
        for y in x.ledger:
            if y["amount"] < 0:
                count += abs(y["amount"])
        percList.append(
            [int((0.10 * round((count / totalCount) / 0.10)) * 100), x.name])
    chart = "Percentage spent by category\n"
    for x in numList:
        chart += x + " "
        for y in percList:
            if y[0] >= int(x[0:3]):
                chart += "o  "
            else:
                chart += "   "
        chart += "\n"
    chart += "    "
    for i in percList:
        chart += "---"
    chart += "-" + "\n"
    categoNames = []
    for z in categories:
        categoNames.append(len(z.name))
    maxLen = max(categoNames)
    count = 0
    categoNames = []
    for z in categories:
        categoNames.append(z.name + (" " * maxLen))
    while maxLen > count:
        chart += "    "
        for v in categoNames:
            chart += " " + v[count] + " "
        if (count + 1) == maxLen:
            chart += " "
        else:
            chart += " \n"
        count += 1
    return chart
 
""" food = Category("Food")
entertainment = Category("Entertainment")
business = Category("Business")
food.deposit(900, "deposit")
entertainment.deposit(900, "deposit")
business.deposit(900, "deposit")
food.withdraw(105.55)
entertainment.withdraw(33.40)
business.withdraw(10.99)
print(create_spend_chart([business, food, entertainment]))

expected = "Percentage spent by category\n100|          \n 90|          \n 80|          \n 70|    o     \n 60|    o     \n 50|    o     \n 40|    o     \n 30|    o     \n 20|    o  o  \n 10| o  o  o  \n  0| o  o  o  \n    ----------\n     B  F  E  \n     u  o  n  \n     s  o  t  \n     i  d  e  \n     n     r  \n     e     t  \n     s     a  \n     s     i  \n           n  \n           m  \n           e  \n           n  \n           t  "
        
print(expected) """