import json
from pathlib import Path

# Save our transactions
def save_transactions(transactions):
    with open("transactions.json", "w") as file:
        json.dump(transactions, file)


def load_transactions():
    file = Path("transactions.json")

    if not file.exists():
        return []

    try:
        with open("transactions.json", "r") as file:
            transactions = json.load(file)

        if not isinstance(transactions, list):
            raise ValueError("Transactions must be a list")

        return transactions

    except json.JSONDecodeError:
        print("Error: invalid JSON file")
        raise



