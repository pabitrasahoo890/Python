class bank_information:
    def __init__(self,account_holder_name,account_number,current_balance):
        self.account_holder_name = account_holder_name
        self.account_number = account_number
        self.current_balance = current_balance
        print("Account statement of",account_holder_name)

    def deposit(self,depo_amount):
        if depo_amount > 0:
            self.current_balance += depo_amount
            return f"Deposited ${depo_amount:.2f}. Current balance: ${self.current_balance:.2f}"
        else:
            return "Invalid deposit amount. Please enter a positive value."

    def withdraw(self,w_amount):
        if 0 < w_amount <= self.current_balance:
            self.current_balance -= w_amount
            return f"Withdrew ${w_amount:.2f}. Current balance: ${self.current_balance:.2f}"
        else:
            return "Insufficient funds or invalid withdrawal amount."

    def get_balance(self):
        return f"Current balance for account {self.account_number}: ${self.current_balance:.2f}"

if __name__ == "__main__":
    # Create a savings account
    ac_name = input("Enter account holder name: ")
    ac_num = input("Enter account number: ")
    savings = bank_information(account_holder_name=ac_name, account_number=ac_num, current_balance=0.0)
    print(savings.deposit(1000))
    print(savings.withdraw(500))
    print(savings.get_balance())  