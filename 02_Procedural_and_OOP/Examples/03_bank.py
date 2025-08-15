# Lab Instructions: Abstract Classes and Methods
# Bank Abstract Class Implementation

from abc import ABC, abstractmethod


# Create a class called Bank and pass ABC to it
class Bank(ABC):
    # Inside the Bank class, define two methods:

    # basicinfo(): This function should print "This is a generic bank" and return "Generic bank: 0"
    def basicinfo(self):
        print("This is a generic bank")
        return "Generic bank: 0"

    # withdraw(): Leave this function empty by adding a pass keyword under it.
    # Mark it as an abstract method by placing @abstractmethod above the function declaration
    @abstractmethod
    def withdraw(self):
        pass


# Create a subclass called Swiss that inherits from Bank
class Swiss(Bank):
    # Define the constructor (__init__): Initialize an instance variable bal to 1000
    def __init__(self):
        self.bal = 1000

    # Override both methods from the Bank class in the Swiss class:

    # basicinfo(): This function should print "This is the Swiss Bank" and return "Swiss Bank: " followed by the current balance
    def basicinfo(self):
        print("This is the Swiss Bank")
        return f"Swiss Bank: {self.bal}"

    # withdraw(amount): Define a function called withdraw that accepts a parameter amount to withdraw
    def withdraw(self, amount):
        # If amount is less than or equal to bal: Deduct amount from bal, print the withdrawal amount and new balance, and return the new balance
        if amount <= self.bal:
            self.bal -= amount
            print(f"Withdrawn amount: {amount}")
            print(f"New Balance: {self.bal}")
            return self.bal
        # If amount is greater than bal: Print "Insufficient funds" and return the original balance
        else:
            print("Insufficient funds")
            return self.bal


# Test the implementation
if __name__ == "__main__":
    # Create a Swiss bank instance
    swiss_bank = Swiss()

    # Test basicinfo method
    print("Testing basicinfo method:")
    result = swiss_bank.basicinfo()
    print(f"Return value: {result}")
    print()

    # Test withdraw method with valid amount
    print("Testing withdraw method with valid amount (200):")
    new_balance = swiss_bank.withdraw(200)
    print(f"Return value: {new_balance}")
    print()

    # Test withdraw method with invalid amount
    print("Testing withdraw method with invalid amount (1000):")
    new_balance = swiss_bank.withdraw(1000)
    print(f"Return value: {new_balance}")
    print()

    # Test basicinfo again to see updated balance
    print("Testing basicinfo method again:")
    result = swiss_bank.basicinfo()
    print(f"Return value: {result}")
