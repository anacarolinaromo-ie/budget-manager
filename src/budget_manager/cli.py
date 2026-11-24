
import json
import argparse
import sys

from datetime import date
from services import calculate_expenses, calculate_income, calculate_balance, add_transaction
from validation import validate_amount, validate_category
from storage import save_transactions, load_transactions
from models import create_transaction

# Creating different options for seeing/modifying information
def show_transactions(transactions):
    for transaction in transactions:
        print(transaction)


# Creating my interactive program · nargs=means it is optional
parser = argparse.ArgumentParser()

parser.add_argument("command", choices=["list", "add", "summary", "backup"])
parser.add_argument("amount", type=float, nargs="?")
parser.add_argument("category", nargs="?")
parser.add_argument("kind", nargs="?")

args = parser.parse_args()

if args.command == "list":
    #Shows all transactions
    saved_transactions = load_transactions()
    show_transactions(saved_transactions)

elif args.command == "add":
    if args.amount is None:
        print("Error: please enter an amount", file=sys.stderr)
        sys.exit(1)

    elif not validate_amount(args.amount):
        print("Error: amount must be greater than 0", file=sys.stderr)
        sys.exit(1)

    elif args.category is None:
        print("Error: please enter a category", file=sys.stderr)
        sys.exit(1)

    elif not validate_category(args.category):
        print("Error: invalid category", file=sys.stderr)
        sys.exit(1)

    elif args.kind not in ["income", "expense"]:
        print("Error: kind must be income or expense", file=sys.stderr)
        sys.exit(1)

    else:
        saved_transactions = load_transactions()

        next_id = 1

        for transaction in saved_transactions:
            number = int(transaction["id"][1:])

            if number >= next_id:
                next_id = number + 1

        new_transaction = create_transaction(
            "T" + str(next_id).zfill(3),
            str(date.today()),
            args.kind,
            args.category,
            args.amount,
            "EUR"
        )

        add_transaction(saved_transactions, new_transaction)
        save_transactions(saved_transactions)
        print("Transaction added!")


elif args.command == "summary":
    saved_transactions = load_transactions()

    print("Total income:", calculate_income(saved_transactions))
    print("Total expenses:", calculate_expenses(saved_transactions))
    print("Balance:", calculate_balance(saved_transactions))


elif args.command == "backup":
    saved_transactions = load_transactions()

    try:
        with open("backup.json", "x") as file:
            json.dump(saved_transactions, file)

        print("Backup created!")

    except FileExistsError:
        print("Error: backup.json already exists", file=sys.stderr)
        sys.exit(1)

