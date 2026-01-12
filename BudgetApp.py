class Category:
    def __init__(self, name):
        self.name = name
        self.ledger = []

    def deposit(self, amount, description=""):
        self.ledger.append({'amount': amount, 'description': description})

    def withdraw(self, amount, description=""):
        if self.check_funds(amount):
            self.ledger.append({'amount': -amount, 'description': description})
            return True
        return False

    def get_balance(self):
        return sum(item['amount'] for item in self.ledger)

    def transfer(self, amount, category):
        if self.check_funds(amount):
            self.withdraw(amount, f"Transfer to {category.name}")
            category.deposit(amount, f"Transfer from {self.name}")
            return True
        return False

    def check_funds(self, amount):
        return amount <= self.get_balance()

    def __str__(self):
        # Title line with asterisks
        title = self.name.center(30, '*')
        lines = [title]

        # Ledger items
        for item in self.ledger:
            description = item['description'][:23]
            amount = f"{item['amount']:.2f}"
            line = f"{description:<23}{amount:>7}"
            lines.append(line)

        # Total line
        total = f"Total: {self.get_balance():.2f}"
        lines.append(total)

        return '\n'.join(lines)


def create_spend_chart(categories):
    # Calculate withdrawals for each category
    withdrawals = []
    for category in categories:
        total = sum(-item['amount']
                    for item in category.ledger if item['amount'] < 0)
        withdrawals.append(total)

    total_withdrawals = sum(withdrawals)

    # Calculate percentages (rounded down to nearest 10)
    percentages = []
    for withdrawal in withdrawals:
        if total_withdrawals == 0:
            percentage = 0
        else:
            percentage = int((withdrawal / total_withdrawals) * 100)
            percentage = (percentage // 10) * 10
        percentages.append(percentage)

    # Build the chart
    lines = ["Percentage spent by category"]

    # Y-axis and bars (from 100 to 0)
    for i in range(100, -1, -10):
        line = f"{i:>3}| "
        for percentage in percentages:
            if percentage >= i:
                line += "o  "
            else:
                line += "   "
        lines.append(line)

    # Horizontal line
    dashes = "---" * len(categories) + "-"
    lines.append(f"    {dashes}")

    # Category names (vertical)
    max_name_length = max(len(category.name) for category in categories)
    for i in range(max_name_length):
        line = "     "
        for category in categories:
            if i < len(category.name):
                line += category.name[i] + "  "
            else:
                line += "   "
        lines.append(line)

    return '\n'.join(lines)


# Test the code
food = Category("Food")
food.deposit(900, 'deposit')
food.withdraw(45.67, 'milk, cereal, eggs, bacon, bread')
print(food)
print(f"\nBalance: {food.get_balance()}")

# Test transfer
clothing = Category("Clothing")
food.deposit(1000, "initial deposit")
food.transfer(50, clothing)
print(f"\nFood balance after transfer: {food.get_balance()}")
print(f"Clothing balance after transfer: {clothing.get_balance()}")

# Test create_spend_chart
auto = Category("Auto")
auto.deposit(1000, "deposit")
auto.withdraw(200, "gas")

print("\n" + create_spend_chart([food, clothing, auto]))
