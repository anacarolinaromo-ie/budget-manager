# Test Evidence

## Test 1: Valid transaction

Command: `python3 src/budget_manager/cli.py add 25 food expense`

Expected result: `Transaction added!`

Actual result: `Transaction added!`

Status: Passed

## Test 2: Negative amount

Command: `python3 src/budget_manager/cli.py add -20 food expense`

Expected result: `Error: amount must be greater than 0`

Actual result: `Error: amount must be greater than 0`

Status: Passed

## Test 3: Invalid category

Command: `python3 src/budget_manager/cli.py add 20 dinosaur expense`

Expected result: `Error: invalid category`

Actual result: `Error: invalid category`

Status: Passed

## Test 4: Invalid transaction kind

Command: `python3 src/budget_manager/cli.py add 50 food wrong`

Expected result: `Error: kind must be income or expense`

Actual result: `Error: kind must be income or expense`

Status: Passed

## Test 5: Missing transactions file

Expected result: Income 0, expenses 0, balance 0

Actual result: Income 0, expenses 0, balance 0

Status: Passed

## Test 6: JSON persistence

The application successfully saved transactions in `transactions.json` and loaded them again.

Status: Passed

## Test 7: Backup verification

The original JSON file and the backup were compared after backup creation. Their contents matched.

Status: Passed