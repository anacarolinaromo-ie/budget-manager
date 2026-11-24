# Personal Budget Manager

## Description

This is a simple Python command-line application to manage personal income and expenses.

The program allows users to add transactions, view saved transactions, calculate income, expenses and balance, and create a backup.

## Requirements

- Python 3
- No external libraries required

## How to Run

Open the terminal in the main `budget-manager` folder.

**Add an expense:**

```bash
python3 src/budget_manager/cli.py add 25 food expense
```

**Add income:**

```bash
python3 src/budget_manager/cli.py add 100 salary income
```

**List transactions:**

```bash
python3 src/budget_manager/cli.py list
```

**Show summary:**

```bash
python3 src/budget_manager/cli.py summary
```

**Create a backup:**

```bash
python3 src/budget_manager/cli.py backup
```

**Show help:**

```bash
python3 src/budget_manager/cli.py --help
```

## Testing

The program was tested with valid and invalid inputs.

| Test | Input | Expected Result | Status |
|---|---|---|---|
| Valid transaction | `add 25 food expense` | Transaction added! | Passed |
| Negative amount | `add -20 food expense` | Error: amount must be greater than 0 | Passed |
| Invalid category | `add 20 dinosaur expense` | Error: invalid category | Passed |
| Invalid transaction kind | `add 50 food wrong` | Error: kind must be income or expense | Passed |
| Missing transactions file | Run `summary` without `transactions.json` | Zero income, expenses, and balance | Passed |

The valid transaction test adds a transaction to `transactions.json`. Invalid transactions are rejected and are not saved.

## Known Limitations

- The program currently supports EUR only.
- Transactions cannot be edited or deleted through the CLI.
- Backups use a fixed filename, so creating another backup with the same name causes an error.
- Existing JSON data is not fully validated when loaded.
- CSV import is not implemented.

## Sample Data

The file `data/sample_transactions.csv` contains sample transactions.

It includes valid and invalid examples to demonstrate the validation rules.

The program uses `transactions.json` to save and load data. The CSV file is provided as sample data and is not automatically imported.