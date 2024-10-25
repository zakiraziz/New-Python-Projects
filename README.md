
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


Cows and Bulls Game
This project is a Python implementation of the classic Cows and Bulls game. The game generates a random 4-digit number with unique digits, and the player attempts to guess the number. After each guess, the program provides feedback in the form of "cows" and "bulls."

Game Rules
Bulls: A "bull" means one of the guessed digits is correct and in the correct position.
Cows: A "cow" means one of the guessed digits is correct but in the wrong position.
The player wins when they guess the exact 4-digit number.
How It Works
The program generates a 4-digit secret number with unique digits.
The player enters a 4-digit guess with unique digits.
After each guess, the program shows the number of cows and bulls to guide the player.
The game continues until the player guesses the correct number (i.e., 4 bulls).
Installation
Clone the repository:

bash
Copy code
git clone https://github.com/zakiraziz/cows-and-bulls-game.git
cd cows-and-bulls-game
Run the game:

bash
Copy code
python cows_and_bulls.py
Code Overview
generate_secret(): Generates a random 4-digit number with unique digits.
calculate_cows_and_bulls(secret, guess): Compares the secret number to the player's guess and returns the number of cows and bulls.
main(): Runs the game loop, checking guesses and providing feedback.
Example
python
Copy code
Guess: 1234
1 cows, 2 bulls
In this example, one digit is correct but in the wrong position (1 cow), and two digits are correct and in the correct position (2 bulls).

Future Improvements
Adding a limit on the number of guesses.
Implementing a scoring system based on the number of guesses.
Adding difficulty levels with different lengths for the secret number.
Contributing
Feel free to fork this repository and submit pull requests if you'd like to improve the game!


