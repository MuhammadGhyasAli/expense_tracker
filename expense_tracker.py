total = 0.0
count = 0
expenses = []

print("===== EXPENSE TRACKER =====")
print("Enter expense amounts. Type 'done' to finish.\n")

while True:
    raw = input("Expense: ").strip().lower()
    if raw == "done":
        break
    try:
        amount = float(raw)
        if amount <= 0:
            print("Amount must be positive.")
            continue
        total += amount
        count += 1
        expenses.append(amount)
        print(f"  Running total: {total:.2f}")
    except ValueError:
        print("Invalid input. Enter a number or 'done'.")

print("\n===== SUMMARY =====")
print(f"Expenses entered: {count}")
if count > 0:
    print(f"Total spent:     {total:.2f}")
    print(f"Average:         {total / count:.2f}")
    print(f"Min expense:     {min(expenses):.2f}")
    print(f"Max expense:     {max(expenses):.2f}")
print("===================")
