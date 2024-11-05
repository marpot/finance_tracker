from datetime import datetime

date_format = "%d-%m-%Y"
CATEGORIES = {"I": "Income", "E": "Expense"}

def get_date(prompt, allow_default=False):
    while True:
        date_str = input(prompt)
        if allow_default and not date_str:
            return datetime.today().strftime(date_format)
        try:
            valid_date = datetime.strptime(date_str, date_format)
            return valid_date.strftime(date_format)
        except ValueError:
            try:
                valid_date = datetime.strptime(date_str, "%d-%m-%y")
                return valid_date.strftime(date_format)
            except ValueError:
                print("Invalid date format, please use DD-MM-YYYY format.")

def get_amount():
    while True:
        try:
            amount = float(input("Enter the amount: "))
            if amount <= 0:
                raise ValueError("Amount cannot be negative or zero.")
            return amount
        except ValueError as e:
            print(e)
            print("Please enter a valid positive number.")

def get_category():
    while True:
        category = input("Enter the category ('I' for Income or 'E' for Expense): ").upper()
        if category in CATEGORIES:
            return CATEGORIES[category]
        else:
            print("Invalid category. Please enter 'I' for Income or 'E' for Expense.")

def get_description():
    return input("Enter the description (optional): ")
