expenses =[]

def add_expense(description, amount, category):

    expense = {
        'description': description,
        'amount': amount,
        'category': category
    }

    expenses.append(expense)

def calculate_total_expenses(expenses):
    total = 0
    for expense in expenses:
        total += expense['amount']
    return total

while True:
    try:
        description = input("Enter expense description: ").title()
        amount = float(input("Enter expense amount: "))
        if amount <= 0:
            print("Amount cannot be zero or negative.")
            continue
        category = input("Enter expense category: ").title()
        add_expense(description, amount, category)
        response = input("Add another expense? (y/n): ")
        if response.lower() != 'y':
            print("Expenses recorded:")
            print()
            for expense in expenses:
                print(f"Description: {expense['description']}")
                print(f"Amount: ${expense['amount']:.2f}")
                print(f"Category: {expense['category']}")
            print()
            break
        
    except ValueError:
        print(f"Error:Please enter a valid number for the amount.")
        continue
total = calculate_total_expenses(expenses)
print(f"Total expenses: ${total:.2f}")
