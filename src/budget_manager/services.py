# Creating different options for seeing/modifying information

def calculate_expenses(transactions):
    total = 0

    for transaction in transactions:
        if transaction["kind"] == "expense":
            total = total + transaction["amount"]

    return total


def calculate_income(transactions):
    total = 0

    for transaction in transactions:
        if transaction["kind"] == "income":
            total = total + transaction["amount"]

    return total


def calculate_balance(transactions):
    income = calculate_income(transactions)
    expenses = calculate_expenses(transactions)

    balance = income - expenses

    return balance


def add_transaction(transactions, new_transaction):
    transactions.append(new_transaction)

