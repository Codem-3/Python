# Instance Methods in Python
# Instance methods are functions defined inside a class that can access and modify the instance's data


class Student:
    def __init__(self, name, age, grade):
        # Instance variables (attributes)
        self.name = name
        self.age = age
        self.grade = grade
        self.courses = []

    # Instance method to display student information
    def display_info(self):
        print(f"Student: {self.name}")
        print(f"Age: {self.age}")
        print(f"Grade: {self.grade}")
        print(f"Number of courses: {len(self.courses)}")
        print("-" * 30)

    # Instance method to add a course
    def add_course(self, course_name):
        self.courses.append(course_name)
        print(f"Added course: {course_name}")

    # Instance method to remove a course
    def remove_course(self, course_name):
        if course_name in self.courses:
            self.courses.remove(course_name)
            print(f"Removed course: {course_name}")
        else:
            print(f"Course '{course_name}' not found")

    # Instance method to update grade
    def update_grade(self, new_grade):
        self.grade = new_grade
        print(f"Grade updated to: {new_grade}")

    # Instance method to check if student is eligible for honors
    def is_honors_eligible(self):
        return self.grade >= 3.5

    # Instance method that returns a formatted string
    def get_summary(self):
        return f"{self.name} (Grade {self.grade}) - {len(self.courses)} courses"


# Example usage
print("=== Instance Methods Demo ===\n")

# Create student objects
student1 = Student("Alice Johnson", 20, 3.8)
student2 = Student("Bob Smith", 19, 3.2)

# Call instance methods on student1
print("Student 1 Information:")
student1.display_info()

# Add courses using instance method
student1.add_course("Python Programming")
student1.add_course("Data Structures")
student1.add_course("Calculus")

# Display updated information
print("After adding courses:")
student1.display_info()

# Check if student is honors eligible
if student1.is_honors_eligible():
    print(f"{student1.name} is eligible for honors!")
else:
    print(f"{student1.name} is not eligible for honors.")

# Get summary using instance method
summary = student1.get_summary()
print(f"Summary: {summary}")

print("\n" + "=" * 50 + "\n")

# Work with student2
print("Student 2 Information:")
student2.display_info()

# Add and remove courses
student2.add_course("English Literature")
student2.add_course("History")
student2.display_info()

student2.remove_course("History")
student2.display_info()

# Update grade
student2.update_grade(3.6)
student2.display_info()

# Check honors eligibility
if student2.is_honors_eligible():
    print(f"{student2.name} is now eligible for honors!")
else:
    print(f"{student2.name} is not eligible for honors.")


# Example with a different class
class BankAccount:
    def __init__(self, account_holder, initial_balance=0):
        self.account_holder = account_holder
        self.balance = initial_balance
        self.transaction_history = []

    def deposit(self, amount):
        if amount > 0:
            self.balance += amount
            self.transaction_history.append(f"Deposit: +${amount}")
            print(f"Deposited ${amount}. New balance: ${self.balance}")
        else:
            print("Invalid deposit amount")

    def withdraw(self, amount):
        if amount > 0 and amount <= self.balance:
            self.balance -= amount
            self.transaction_history.append(f"Withdrawal: -${amount}")
            print(f"Withdrew ${amount}. New balance: ${self.balance}")
        else:
            print("Invalid withdrawal amount or insufficient funds")

    def get_balance(self):
        return self.balance

    def display_transactions(self):
        print(f"\nTransaction history for {self.account_holder}:")
        for transaction in self.transaction_history:
            print(f"  {transaction}")
        print(f"Current balance: ${self.balance}")


print("\n" + "=" * 50)
print("=== Bank Account Example ===")

# Create a bank account
account = BankAccount("John Doe", 1000)

# Use instance methods
account.deposit(500)
account.withdraw(200)
account.deposit(100)
account.withdraw(50)

# Display transaction history
account.display_transactions()
