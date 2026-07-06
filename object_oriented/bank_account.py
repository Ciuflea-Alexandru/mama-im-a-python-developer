class BankAccount:
    def __init__(self, owner, initial_balance=0):
        self.owner = owner
        self.__balance = initial_balance

    def deposit(self, amount):
        if amount > 0:
            self.__balance += amount
            print(f"Deposited ${amount}. New balance: ${self.__balance}")
        else:
            print("Deposit amount must be positive.")

    def withdraw(self, amount):
        if 0 < amount <= self.__balance:
            self.__balance -= amount
            print(f"Withdrew ${amount}. Remaining balance: ${self.__balance}")
        else:
            print("Invalid withdrawal amount or insufficient funds.")

    def get_balance(self):
        """Getter method to access the private balance safely."""
        return self.__balance

if __name__ == "__main__":
    account = BankAccount("Alice", 100)
    account.deposit(50)
    account.withdraw(30)
    
    print(f"Final balance for {account.owner}: ${account.get_balance()}")