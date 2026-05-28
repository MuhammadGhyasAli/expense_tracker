# Expense Tracker

A CLI expense tracker that accumulates expenses and displays a summary. Users enter amounts one at a time; the program shows a running total and final statistics.

## Features

- **Continuous entry** — Enter expenses until typing `done`
- **Running total** — See the updated total after each expense
- **Final summary** — Displays total spent, count, average, minimum, and maximum
- **Input validation** — Rejects non-numeric input, negative values, and zero

## How to Run

```bash
python expense_tracker.py
```

## Usage

Type a positive number to log an expense. Type `done` to finish and see the summary.

## Sample Session

```
===== EXPENSE TRACKER =====
Enter expense amounts. Type 'done' to finish.

Expense: 100
  Running total: 100.00
Expense: 50
  Running total: 150.00
Expense: 25.50
  Running total: 175.50
Expense: done

===== SUMMARY =====
Expenses entered: 3
Total spent:     175.50
Average:         58.50
Min expense:     25.50
Max expense:     100.00
===================
```

## Code Structure

- `total` — accumulator for running total
- `count` — number of expenses entered
- `expenses` — list of all amounts (used for min/max)
- Core logic: `total += amount` (accumulator pattern)
