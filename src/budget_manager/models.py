# creating a function to create a transaction 

def create_transaction(id, date, kind, category, amount, currency):
    transaction = {
        "id": id,
        "date": date,
        "kind": kind,
        "category": category,
        "amount": amount,
        "currency": currency
    }

    return transaction
