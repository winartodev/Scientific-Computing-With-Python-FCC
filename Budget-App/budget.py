def create_spend_chart(categories):
    result = "Percentage spent by category \n"
    total = 0
    for category in categories:
        total += category.get_withdrawals()
    result += str(total)

    return result

class Category:
    def __init__(self, name):
        self.name = name
        self.ledger = list()

    def __str__(self):
        title = f"{self.name:*^30}\n"
        items = ""
        total = 0
        for item in self.ledger:
            items += f"{item['description'][0:23]:23}" + f"{item['amount']:>7.2f}" + "\n"
            total += item['amount']
        result = title + items + f"Total: {total}" 
        return result

    def deposit(self, amount, description=""):
        self.ledger.append({"amount": amount, "description": description})

    def withdraw(self, amount, description=""):
        if (self.check_funds(amount)):
            self.ledger.append({"amount": -amount, "description": description})
            return True
        return False
    
    def get_balance(self):
        total_cash = 0
        for item in self.ledger:
            total_cash += item["amount"]
        return total_cash

    def transfer(self, amount, category):
        if (self.check_funds(amount)):
            self.withdraw(amount, f"Transfer to {category.name}")
            category.deposit(amount,"Transfer from " + self.name)
            return True
        return False

    def check_funds(self, amount):
        if (self.ledger[0]["amount"] >= amount):
            return True 
        return False

    def get_withdrawals(self):
        total = 0
        for item in self.ledger:
            total += item['amount']
        print(total)
        return total


food = Category("Food")
food.deposit(1000, "initial deposit")
food.withdraw(10.15, "groceries")
food.withdraw(15.89, "restaurant and more food for dessert")
print(food.get_balance())
clothing = Category("Clothing")
food.transfer(50, clothing)
clothing.withdraw(25.55)
clothing.withdraw(100)
auto = Category("Auto")
auto.deposit(1000, "initial deposit")
auto.withdraw(15)

print(food)
print(clothing)

print(create_spend_chart([food, clothing, auto]))

expected1 = f"*************Food*************\ndeposit                 900.00\nmilk, cereal, eggs, bac -45.67\nTransfer to Entertainme -20.00\nTotal: 834.33"
expected2 = "Percentage spent by category\n100|          \n 90|          \n 80|          \n 70|    o     \n 60|    o     \n 50|    o     \n 40|    o     \n 30|    o     \n 20|    o  o  \n 10|    o  o  \n  0| o  o  o  \n    ----------\n     B  F  E  \n     u  o  n  \n     s  o  t  \n     i  d  e  \n     n     r  \n     e     t  \n     s     a  \n     s     i  \n           n  \n           m  \n           e  \n           n  \n           t  "

# print(expected2)
