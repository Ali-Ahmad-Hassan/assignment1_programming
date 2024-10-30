class BankAccount:
    # BankAccount class with accountID and balance attributes
    def __init__(self, accountID, balance):
        self.accountID = accountID
        self.balance = balance

    def deposit(self, amount):
        # Add amount to the balance
        self.balance += amount

    def withdraw(self, amount):
        # Subtract amount if balance is sufficient
        if amount <= self.balance:
            self.balance -= amount
        else:
            print(f"Insufficient balance in account {self.accountID}")

    def __str__(self):
        return f"BankAccount[ID: {self.accountID}, Balance: {self.balance}]"


class SavingsAccount(BankAccount):
    # SavingsAccount class inherits from BankAccount and adds interest
    def __init__(self, accountID, balance, interest):
        super().__init__(accountID, balance)
        self.interest = interest

    def check_balance(self):
        # Display current balance
        print(f"Balance for Savings Account {self.accountID}: {self.balance}")

    def __str__(self):
        return f"SavingsAccount[ID: {self.accountID}, Balance: {self.balance}, Interest: {self.interest}%]"


class MilesAccount(BankAccount):
    # MilesAccount class inherits from BankAccount and adds rewards and points
    def __init__(self, accountID, balance, rewards, points):
        super().__init__(accountID, balance)
        self.rewards = rewards
        self.points = points

    def display_details(self):
        # Display miles account details
        print(f"Account ID: {self.accountID}, Balance: {self.balance}, Rewards: {self.rewards}, Points: {self.points}")

    def __str__(self):
        return f"MilesAccount[ID: {self.accountID}, Balance: {self.balance}, Rewards: {self.rewards}, Points: {self.points}]"


class Customer:
    # Customer class with a list of BankAccount objects
    def __init__(self, customerID, name):
        self.customerID = customerID
        self.name = name
        self.bank_accounts = []

    def create_account(self, account):
        # Add a bank account to the customer
        if isinstance(account, BankAccount):
            self.bank_accounts.append(account)
        else:
            print("Invalid account type")

    def print_accounts(self):
        # Print details of all accounts for the customer
        print(f"Customer: {self.name} (ID: {self.customerID})")
        for account in self.bank_accounts:
            print(account)


# Testing the classes

# Create a customer
customer1 = Customer("C001", "Alice")

# Create a savings account and add it to the customer
savings_account = SavingsAccount("A001", 1000.0, 2.5)
customer1.create_account(savings_account)

# Create a miles account and add it to the customer
miles_account = MilesAccount("A002", 2000.0, 500, 3000)
customer1.create_account(miles_account)

# Print customer and their account details
customer1.print_accounts()

# Check balance of savings account
savings_account.check_balance()

# Display details of miles account
miles_account.display_details()
