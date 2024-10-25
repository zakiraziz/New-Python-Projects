
ATM Simulator
This project is a command-line ATM (Automated Teller Machine) simulator in Python. It provides basic banking functionalities such as checking balance, depositing funds, and withdrawing funds, along with a simple, user-friendly menu system.

Features
Check Balance: View your current balance in the account.
Deposit Funds: Add money to your account.
Withdraw Funds: Withdraw money from your account (with checks for sufficient funds).
Exit: End the session.
Class Structure
ATM Class: Handles account balance and provides methods for balance check, deposit, and withdrawal.
ATMController Class: Manages the interaction with the user through a menu-driven interface and validates user input.
Installation
Clone the repository:

bash
Copy code
git clone https://github.com/zakiraziz/ATM-Simulator.git
cd ATM-Simulator
Run the ATM simulator using Python:

bash
Copy code
python atm.py
How to Use
After starting the program, you'll see a welcome message and a list of options.
Select an option by entering the corresponding number.
Follow the prompts for deposit or withdrawal actions.
To exit, select the "Exit" option.
Code Example
Here's a snippet of how the classes are structured:

python
Copy code
class ATM:
    def __init__(self):
        self.balance = 0

    def check_balance(self):
        return self.balance

    def deposit(self, amount):
        if amount <= 0:
            raise ValueError('Deposit amount must be positive.')
        self.balance += amount

    def withdraw(self, amount):
        if amount <= 0:
            raise ValueError('Withdrawal amount must be positive.')
        if amount > self.balance:
            raise ValueError('Insufficient funds.')
        self.balance -= amount
Future Improvements
Adding a transaction history feature.
Implementing a user authentication system.
Adding more advanced banking features (e.g., transfer between accounts, loan applications).
Contributing
Feel free to contribute to this project by submitting issues or pull requests!


