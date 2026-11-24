#  Validate correct amounts and categories
def validate_amount(amount):
    if amount <= 0:
        return False
    else:
        return True

def validate_category(category):
    categories = ["food", "transport", "shopping", "rent", "salary", "other"]

    if category in categories:
        return True
    else:
        return False