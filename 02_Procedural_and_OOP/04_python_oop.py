# ============================================
# PYTHON OBJECT-ORIENTED PROGRAMMING TUTORIAL
# ============================================
# This file covers comprehensive OOP concepts in Python
# with examples, best practices, and real-world applications

print("=" * 60)
print("PYTHON OBJECT-ORIENTED PROGRAMMING TUTORIAL")
print("=" * 60)

# ============================================
# SECTION 1: INTRODUCTION TO OOP
# ============================================
print("\n" + "=" * 60)
print("SECTION 1: INTRODUCTION TO OOP")
print("=" * 60)

print("\n1.1 What is Object-Oriented Programming?")
print("-" * 30)
print(
    """
Object-Oriented Programming (OOP) is a programming paradigm that:
- Organizes code into objects that contain data and behavior
- Models real-world entities as software objects
- Promotes code reusability and maintainability
- Provides structure for complex programs

Key Concepts:
1. Classes: Blueprints for creating objects
2. Objects: Instances of classes with data and behavior
3. Inheritance: Creating new classes from existing ones
4. Polymorphism: Same interface, different implementations
5. Encapsulation: Bundling data and methods together
6. Abstraction: Hiding complex implementation details

Benefits:
- Code reusability
- Maintainability
- Scalability
- Real-world modeling
- Team collaboration
"""
)

print("\n1.2 OOP vs Procedural Programming")
print("-" * 30)
print(
    """
PROCEDURAL PROGRAMMING:
- Focus on functions and procedures
- Data and functions are separate
- Linear execution flow
- Harder to maintain large programs

OBJECT-ORIENTED PROGRAMMING:
- Focus on objects and their interactions
- Data and behavior are bundled together
- Modular and organized structure
- Easier to maintain and extend
"""
)

# ============================================
# SECTION 2: CLASSES AND OBJECTS
# ============================================
print("\n" + "=" * 60)
print("SECTION 2: CLASSES AND OBJECTS")
print("=" * 60)

print("\n2.1 Creating a Simple Class")
print("-" * 30)


class Dog:
    """A simple class representing a dog"""

    # Class variable (shared by all instances)
    species = "Canis familiaris"

    def __init__(self, name, age, breed):
        """Constructor method - called when creating a new object"""
        self.name = name  # Instance variable
        self.age = age  # Instance variable
        self.breed = breed  # Instance variable

    def bark(self):
        """Instance method"""
        return f"{self.name} says Woof!"

    def describe(self):
        """Instance method"""
        return f"{self.name} is {self.age} years old and is a {self.breed}"

    def have_birthday(self):
        """Instance method that modifies object state"""
        self.age += 1
        return f"{self.name} is now {self.age} years old!"


# Creating objects (instances) of the Dog class
print("Creating Dog objects:")
my_dog = Dog("Buddy", 3, "Golden Retriever")
your_dog = Dog("Max", 5, "Labrador")

print(f"My dog: {my_dog.name}")
print(f"Your dog: {your_dog.name}")
print(f"Species: {Dog.species}")  # Accessing class variable

# Calling instance methods
print(f"\nMethod calls:")
print(my_dog.bark())
print(my_dog.describe())
print(your_dog.describe())

# Modifying object state
print(f"\nBirthday celebration:")
print(my_dog.have_birthday())
print(my_dog.describe())

print("\n2.2 Class Methods and Static Methods")
print("-" * 30)


class MathOperations:
    """Class demonstrating class methods and static methods"""

    class_variable = 10

    def __init__(self, value):
        self.value = value

    def instance_method(self):
        """Instance method - can access instance and class variables"""
        return f"Instance value: {self.value}, Class value: {self.class_variable}"

    @classmethod
    def class_method(cls, value):
        """Class method - can access class variables but not instance variables"""
        cls.class_variable = value
        return f"Class variable set to: {cls.class_variable}"

    @staticmethod
    def static_method(x, y):
        """Static method - cannot access class or instance variables"""
        return f"Sum of {x} and {y} is {x + y}"


# Testing different method types
math_obj = MathOperations(5)

print("Method types demonstration:")
print(f"Instance method: {math_obj.instance_method()}")
print(f"Class method: {MathOperations.class_method(20)}")
print(f"Static method: {MathOperations.static_method(10, 15)}")

print("\n2.3 Properties and Getters/Setters")
print("-" * 30)


class BankAccount:
    """Class demonstrating properties and getters/setters"""

    def __init__(self, account_holder, initial_balance=0):
        self._account_holder = account_holder  # Protected attribute
        self._balance = initial_balance  # Protected attribute

    @property
    def balance(self):
        """Getter for balance"""
        return self._balance

    @balance.setter
    def balance(self, value):
        """Setter for balance with validation"""
        if value < 0:
            raise ValueError("Balance cannot be negative")
        self._balance = value

    @property
    def account_holder(self):
        """Read-only property for account holder"""
        return self._account_holder

    def deposit(self, amount):
        """Deposit money into account"""
        if amount > 0:
            self.balance += amount
            return f"Deposited ${amount}. New balance: ${self.balance}"
        else:
            return "Invalid deposit amount"

    def withdraw(self, amount):
        """Withdraw money from account"""
        if amount > 0 and amount <= self.balance:
            self.balance -= amount
            return f"Withdrew ${amount}. New balance: ${self.balance}"
        else:
            return "Invalid withdrawal amount"


# Testing properties
account = BankAccount("Alice", 1000)
print("Bank account demonstration:")
print(f"Account holder: {account.account_holder}")
print(f"Initial balance: ${account.balance}")

print(account.deposit(500))
print(account.withdraw(200))

# This would raise an error (read-only property)
# account.account_holder = "Bob"  # AttributeError

# This would raise an error (negative balance)
# account.balance = -100  # ValueError

# ============================================
# SECTION 3: INHERITANCE
# ============================================
print("\n" + "=" * 60)
print("SECTION 3: INHERITANCE")
print("=" * 60)

print("\n3.1 Basic Inheritance")
print("-" * 30)


class Animal:
    """Base class (parent class)"""

    def __init__(self, name, species):
        self.name = name
        self.species = species

    def make_sound(self):
        return "Some generic animal sound"

    def describe(self):
        return f"{self.name} is a {self.species}"


class Cat(Dog):  # Cat inherits from Dog
    """Derived class (child class)"""

    def __init__(self, name, age, breed, color):
        # Call parent class constructor
        super().__init__(name, age, breed)
        self.color = color  # Additional attribute

    def make_sound(self):
        """Override parent method"""
        return f"{self.name} says Meow!"

    def scratch(self):
        """New method specific to Cat"""
        return f"{self.name} is scratching"

    def describe(self):
        """Override parent method with additional info"""
        return f"{self.name} is a {self.age}-year-old {self.color} {self.breed}"


# Testing inheritance
print("Inheritance demonstration:")
my_cat = Cat("Whiskers", 2, "Persian", "white")
print(my_cat.make_sound())  # Overridden method
print(my_cat.describe())  # Overridden method
print(my_cat.scratch())  # New method
print(f"Species: {my_cat.species}")  # Inherited attribute

print("\n3.2 Multiple Inheritance")
print("-" * 30)


class Flyable:
    """Mixin class for flying capability"""

    def fly(self):
        return f"{self.name} is flying"


class Swimmable:
    """Mixin class for swimming capability"""

    def swim(self):
        return f"{self.name} is swimming"


class Duck(Animal, Flyable, Swimmable):
    """Class with multiple inheritance"""

    def __init__(self, name, species="Duck"):
        super().__init__(name, species)

    def make_sound(self):
        return f"{self.name} says Quack!"

    def describe(self):
        return f"{self.name} is a {self.species} that can fly and swim"


# Testing multiple inheritance
duck = Duck("Donald")
print("Multiple inheritance demonstration:")
print(duck.make_sound())
print(duck.fly())
print(duck.swim())
print(duck.describe())

print("\n3.3 Method Resolution Order (MRO)")
print("-" * 30)


class A:
    def method(self):
        return "A"


class B(A):
    def method(self):
        return "B"


class C(A):
    def method(self):
        return "C"


class D(B, C):
    pass


# Check MRO
print("Method Resolution Order:")
print(f"D.__mro__: {D.__mro__}")

d = D()
print(f"d.method(): {d.method()}")  # Calls B's method

# ============================================
# SECTION 4: POLYMORPHISM
# ============================================
print("\n" + "=" * 60)
print("SECTION 4: POLYMORPHISM")
print("=" * 60)

print("\n4.1 Method Overriding")
print("-" * 30)


class Shape:
    """Base class for shapes"""

    def area(self):
        return "Area calculation not implemented"

    def perimeter(self):
        return "Perimeter calculation not implemented"


class Rectangle(Shape):
    """Rectangle class"""

    def __init__(self, width, height):
        self.width = width
        self.height = height

    def area(self):
        return self.width * self.height

    def perimeter(self):
        return 2 * (self.width + self.height)


class Circle(Shape):
    """Circle class"""

    def __init__(self, radius):
        self.radius = radius

    def area(self):
        import math

        return math.pi * self.radius**2

    def perimeter(self):
        import math

        return 2 * math.pi * self.radius


# Polymorphism demonstration
shapes = [Rectangle(5, 3), Circle(4), Rectangle(2, 2)]

print("Polymorphism demonstration:")
for shape in shapes:
    print(f"{type(shape).__name__}:")
    print(f"  Area: {shape.area():.2f}")
    print(f"  Perimeter: {shape.perimeter():.2f}")

print("\n4.2 Duck Typing")
print("-" * 30)


class Bird:
    def fly(self):
        return "Bird is flying"


class Airplane:
    def fly(self):
        return "Airplane is flying"


class Superman:
    def fly(self):
        return "Superman is flying"


def make_it_fly(flying_object):
    """Function that works with any object that has a fly method"""
    return flying_object.fly()


# Duck typing demonstration
objects = [Bird(), Airplane(), Superman()]

print("Duck typing demonstration:")
for obj in objects:
    print(f"{type(obj).__name__}: {make_it_fly(obj)}")

# ============================================
# SECTION 5: ENCAPSULATION
# ============================================
print("\n" + "=" * 60)
print("SECTION 5: ENCAPSULATION")
print("=" * 60)

print("\n5.1 Access Modifiers")
print("-" * 30)


class BankAccount:
    """Class demonstrating encapsulation"""

    def __init__(self, account_number, balance):
        self.account_number = account_number  # Public
        self._balance = balance  # Protected
        self.__pin = "1234"  # Private

    def get_balance(self):
        """Public method to access balance"""
        return self._balance

    def _validate_pin(self, pin):
        """Protected method for PIN validation"""
        return pin == self.__pin

    def __generate_statement(self):
        """Private method for internal use"""
        return f"Account: {self.account_number}, Balance: ${self._balance}"

    def withdraw(self, amount, pin):
        """Public method with encapsulation"""
        if not self._validate_pin(pin):
            return "Invalid PIN"

        if amount > self._balance:
            return "Insufficient funds"

        self._balance -= amount
        return f"Withdrew ${amount}. New balance: ${self._balance}"


# Testing encapsulation
account = BankAccount("12345", 1000)
print("Encapsulation demonstration:")
print(f"Account number: {account.account_number}")  # Public
print(f"Balance: ${account.get_balance()}")  # Public method
print(account.withdraw(100, "1234"))  # Valid PIN
print(account.withdraw(100, "0000"))  # Invalid PIN

# These would cause errors:
# print(account.__pin)                    # AttributeError
# print(account.__generate_statement())   # AttributeError

print("\n5.2 Name Mangling")
print("-" * 30)


class Example:
    def __init__(self):
        self.public_var = "public"
        self._protected_var = "protected"
        self.__private_var = "private"

    def public_method(self):
        return "public method"

    def _protected_method(self):
        return "protected method"

    def __private_method(self):
        return "private method"


obj = Example()

print("Name mangling demonstration:")
print(f"Public: {obj.public_var}")
print(f"Protected: {obj._protected_var}")
# print(f"Private: {obj.__private_var}")  # This would fail

# But we can access it with name mangling:
print(f"Private (mangled): {obj._Example__private_var}")

# ============================================
# SECTION 6: ABSTRACTION
# ============================================
print("\n" + "=" * 60)
print("SECTION 6: ABSTRACTION")
print("=" * 60)

print("\n6.1 Abstract Base Classes")
print("-" * 30)

from abc import ABC, abstractmethod


class Vehicle(ABC):
    """Abstract base class for vehicles"""

    def __init__(self, brand, model):
        self.brand = brand
        self.model = model

    @abstractmethod
    def start_engine(self):
        """Abstract method - must be implemented by subclasses"""
        pass

    @abstractmethod
    def stop_engine(self):
        """Abstract method - must be implemented by subclasses"""
        pass

    def get_info(self):
        """Concrete method - can be used by all subclasses"""
        return f"{self.brand} {self.model}"


class Car(Vehicle):
    """Concrete class implementing Vehicle"""

    def start_engine(self):
        return f"{self.get_info()} engine started"

    def stop_engine(self):
        return f"{self.get_info()} engine stopped"


class Motorcycle(Vehicle):
    """Concrete class implementing Vehicle"""

    def start_engine(self):
        return f"{self.get_info()} engine started with a roar"

    def stop_engine(self):
        return f"{self.get_info()} engine stopped"


# Testing abstraction
print("Abstraction demonstration:")
car = Car("Toyota", "Camry")
motorcycle = Motorcycle("Honda", "CBR")

vehicles = [car, motorcycle]
for vehicle in vehicles:
    print(f"{vehicle.get_info()}:")
    print(f"  {vehicle.start_engine()}")
    print(f"  {vehicle.stop_engine()}")

# This would cause an error:
# vehicle = Vehicle("Generic", "Model")  # TypeError

print("\n6.2 Interface-like Classes")
print("-" * 30)


class DatabaseInterface(ABC):
    """Interface-like class for database operations"""

    @abstractmethod
    def connect(self):
        pass

    @abstractmethod
    def disconnect(self):
        pass

    @abstractmethod
    def execute_query(self, query):
        pass


class MySQLDatabase(DatabaseInterface):
    """MySQL database implementation"""

    def connect(self):
        return "Connected to MySQL database"

    def disconnect(self):
        return "Disconnected from MySQL database"

    def execute_query(self, query):
        return f"Executing query on MySQL: {query}"


class PostgreSQLDatabase(DatabaseInterface):
    """PostgreSQL database implementation"""

    def connect(self):
        return "Connected to PostgreSQL database"

    def disconnect(self):
        return "Disconnected from PostgreSQL database"

    def execute_query(self, query):
        return f"Executing query on PostgreSQL: {query}"


# Testing interface-like classes
databases = [MySQLDatabase(), PostgreSQLDatabase()]

print("Interface demonstration:")
for db in databases:
    print(f"{type(db).__name__}:")
    print(f"  {db.connect()}")
    print(f"  {db.execute_query('SELECT * FROM users')}")
    print(f"  {db.disconnect()}")

# ============================================
# SECTION 7: REAL-WORLD APPLICATIONS
# ============================================
print("\n" + "=" * 60)
print("SECTION 7: REAL-WORLD APPLICATIONS")
print("=" * 60)

print("\n7.1 E-commerce System")
print("-" * 30)


class Product:
    """Product class for e-commerce"""

    def __init__(self, product_id, name, price, stock):
        self.product_id = product_id
        self.name = name
        self.price = price
        self.stock = stock

    def update_stock(self, quantity):
        if self.stock + quantity >= 0:
            self.stock += quantity
            return True
        return False

    def get_info(self):
        return f"{self.name} - ${self.price} (Stock: {self.stock})"


class ShoppingCart:
    """Shopping cart for e-commerce"""

    def __init__(self):
        self.items = {}  # product_id: quantity

    def add_item(self, product, quantity=1):
        if product.product_id in self.items:
            self.items[product.product_id] += quantity
        else:
            self.items[product.product_id] = quantity

    def remove_item(self, product_id):
        if product_id in self.items:
            del self.items[product_id]

    def get_total(self, products):
        total = 0
        for product_id, quantity in self.items.items():
            if product_id in products:
                total += products[product_id].price * quantity
        return total


class Customer:
    """Customer class for e-commerce"""

    def __init__(self, customer_id, name, email):
        self.customer_id = customer_id
        self.name = name
        self.email = email
        self.cart = ShoppingCart()

    def add_to_cart(self, product, quantity=1):
        self.cart.add_item(product, quantity)

    def checkout(self, products):
        total = self.cart.get_total(products)
        return f"Checkout complete for {self.name}. Total: ${total:.2f}"


# E-commerce system demonstration
print("E-commerce system demonstration:")
products = {
    1: Product(1, "Laptop", 999.99, 10),
    2: Product(2, "Mouse", 29.99, 50),
    3: Product(3, "Keyboard", 79.99, 25),
}

customer = Customer(1, "Alice", "alice@example.com")

print("Available products:")
for product in products.values():
    print(f"  {product.get_info()}")

customer.add_to_cart(products[1], 1)
customer.add_to_cart(products[2], 2)

print(f"\nCustomer cart total: ${customer.cart.get_total(products):.2f}")
print(customer.checkout(products))

print("\n7.2 Library Management System")
print("-" * 30)


class Book:
    """Book class for library system"""

    def __init__(self, book_id, title, author, isbn):
        self.book_id = book_id
        self.title = title
        self.author = author
        self.isbn = isbn
        self.is_borrowed = False
        self.borrowed_by = None

    def borrow(self, member):
        if not self.is_borrowed:
            self.is_borrowed = True
            self.borrowed_by = member
            return f"'{self.title}' borrowed by {member.name}"
        return f"'{self.title}' is already borrowed"

    def return_book(self):
        if self.is_borrowed:
            borrower = self.borrowed_by.name
            self.is_borrowed = False
            self.borrowed_by = None
            return f"'{self.title}' returned by {borrower}"
        return f"'{self.title}' is not borrowed"


class LibraryMember:
    """Library member class"""

    def __init__(self, member_id, name, email):
        self.member_id = member_id
        self.name = name
        self.email = email
        self.borrowed_books = []

    def borrow_book(self, book):
        result = book.borrow(self)
        if "borrowed" in result and "already" not in result:
            self.borrowed_books.append(book)
        return result

    def return_book(self, book):
        if book in self.borrowed_books:
            self.borrowed_books.remove(book)
            return book.return_book()
        return f"{self.name} hasn't borrowed '{book.title}'"


class Library:
    """Library class"""

    def __init__(self):
        self.books = {}
        self.members = {}

    def add_book(self, book):
        self.books[book.book_id] = book

    def add_member(self, member):
        self.members[member.member_id] = member

    def search_book(self, title):
        for book in self.books.values():
            if title.lower() in book.title.lower():
                return book
        return None


# Library system demonstration
print("Library system demonstration:")
library = Library()

# Add books
book1 = Book(1, "Python Programming", "John Doe", "123-456-789")
book2 = Book(2, "Data Science", "Jane Smith", "987-654-321")
library.add_book(book1)
library.add_book(book2)

# Add member
member = LibraryMember(1, "Alice", "alice@example.com")
library.add_member(member)

print("Library operations:")
print(member.borrow_book(book1))
print(member.borrow_book(book2))
print(member.return_book(book1))

print("\n7.3 Bank Account System")
print("-" * 30)


class Account:
    """Base account class"""

    def __init__(self, account_number, holder_name, balance=0):
        self.account_number = account_number
        self.holder_name = holder_name
        self.balance = balance
        self.transactions = []

    def deposit(self, amount):
        if amount > 0:
            self.balance += amount
            self.transactions.append(f"Deposit: +${amount}")
            return f"Deposited ${amount}. New balance: ${self.balance}"
        return "Invalid deposit amount"

    def withdraw(self, amount):
        if amount > 0 and amount <= self.balance:
            self.balance -= amount
            self.transactions.append(f"Withdrawal: -${amount}")
            return f"Withdrew ${amount}. New balance: ${self.balance}"
        return "Invalid withdrawal amount"

    def get_balance(self):
        return self.balance

    def get_transactions(self):
        return self.transactions


class SavingsAccount(Account):
    """Savings account with interest"""

    def __init__(self, account_number, holder_name, balance=0, interest_rate=0.02):
        super().__init__(account_number, holder_name, balance)
        self.interest_rate = interest_rate

    def add_interest(self):
        interest = self.balance * self.interest_rate
        self.balance += interest
        self.transactions.append(f"Interest: +${interest:.2f}")
        return f"Interest added: ${interest:.2f}. New balance: ${self.balance:.2f}"


class CheckingAccount(Account):
    """Checking account with overdraft protection"""

    def __init__(self, account_number, holder_name, balance=0, overdraft_limit=100):
        super().__init__(account_number, holder_name, balance)
        self.overdraft_limit = overdraft_limit

    def withdraw(self, amount):
        if amount > 0 and amount <= (self.balance + self.overdraft_limit):
            self.balance -= amount
            self.transactions.append(f"Withdrawal: -${amount}")
            return f"Withdrew ${amount}. New balance: ${self.balance}"
        return "Withdrawal exceeds available funds"


# Bank system demonstration
print("Bank system demonstration:")
savings = SavingsAccount("SA001", "Alice", 1000)
checking = CheckingAccount("CA001", "Bob", 500)

print("Savings account:")
print(savings.deposit(500))
print(savings.add_interest())
print(savings.withdraw(200))

print("\nChecking account:")
print(checking.deposit(300))
print(checking.withdraw(800))  # Uses overdraft
print(checking.withdraw(200))  # Exceeds limit

# ============================================
# SECTION 8: DESIGN PATTERNS
# ============================================
print("\n" + "=" * 60)
print("SECTION 8: DESIGN PATTERNS")
print("=" * 60)

print("\n8.1 Singleton Pattern")
print("-" * 30)


class Singleton:
    """Singleton pattern implementation"""

    _instance = None

    def __new__(cls):
        if cls._instance is None:
            cls._instance = super().__new__(cls)
            cls._instance.data = []
        return cls._instance

    def add_data(self, item):
        self.data.append(item)

    def get_data(self):
        return self.data


# Singleton demonstration
print("Singleton pattern demonstration:")
singleton1 = Singleton()
singleton2 = Singleton()

print(f"Are they the same object? {singleton1 is singleton2}")

singleton1.add_data("Item 1")
singleton2.add_data("Item 2")

print(f"Data from singleton1: {singleton1.get_data()}")
print(f"Data from singleton2: {singleton2.get_data()}")

print("\n8.2 Factory Pattern")
print("-" * 30)


class AnimalFactory:
    """Factory pattern for creating animals"""

    @staticmethod
    def create_animal(animal_type, name):
        if animal_type.lower() == "dog":
            return Dog(name, 1, "Mixed")
        elif animal_type.lower() == "cat":
            return Cat(name, 1, "Mixed", "Unknown")
        else:
            raise ValueError(f"Unknown animal type: {animal_type}")


# Factory pattern demonstration
print("Factory pattern demonstration:")
try:
    dog = AnimalFactory.create_animal("dog", "Rex")
    cat = AnimalFactory.create_animal("cat", "Fluffy")

    print(f"Created: {dog.describe()}")
    print(f"Created: {cat.describe()}")

    # This would raise an error
    # unknown = AnimalFactory.create_animal("elephant", "Dumbo")
except ValueError as e:
    print(f"Error: {e}")

print("\n8.3 Observer Pattern")
print("-" * 30)


class Subject:
    """Subject class for observer pattern"""

    def __init__(self):
        self._observers = []
        self._state = None

    def attach(self, observer):
        self._observers.append(observer)

    def detach(self, observer):
        self._observers.remove(observer)

    def notify(self):
        for observer in self._observers:
            observer.update(self._state)

    @property
    def state(self):
        return self._state

    @state.setter
    def state(self, value):
        self._state = value
        self.notify()


class Observer:
    """Observer class for observer pattern"""

    def __init__(self, name):
        self.name = name

    def update(self, state):
        print(f"{self.name} received update: {state}")


# Observer pattern demonstration
print("Observer pattern demonstration:")
subject = Subject()

observer1 = Observer("Observer 1")
observer2 = Observer("Observer 2")

subject.attach(observer1)
subject.attach(observer2)

subject.state = "New state"  # This will notify all observers

# ============================================
# SECTION 9: BEST PRACTICES
# ============================================
print("\n" + "=" * 60)
print("SECTION 9: BEST PRACTICES")
print("=" * 60)

print("\n9.1 Class Design Principles")
print("-" * 30)
print(
    """
1. Single Responsibility Principle (SRP):
   - Each class should have one reason to change
   - Keep classes focused and cohesive

2. Open/Closed Principle (OCP):
   - Open for extension, closed for modification
   - Use inheritance and polymorphism

3. Liskov Substitution Principle (LSP):
   - Subclasses should be substitutable for base classes
   - Maintain behavioral compatibility

4. Interface Segregation Principle (ISP):
   - Clients shouldn't depend on interfaces they don't use
   - Keep interfaces small and focused

5. Dependency Inversion Principle (DIP):
   - Depend on abstractions, not concretions
   - Use dependency injection
"""
)

print("\n9.2 Code Organization")
print("-" * 30)
print(
    """
1. Class Structure:
   - Class variables first
   - Constructor (__init__)
   - Properties (@property)
   - Public methods
   - Protected methods (_method)
   - Private methods (__method)

2. Naming Conventions:
   - Class names: PascalCase (MyClass)
   - Method names: snake_case (my_method)
   - Variables: snake_case (my_variable)
   - Constants: UPPER_CASE (MAX_VALUE)

3. Documentation:
   - Use docstrings for classes and methods
   - Include examples in docstrings
   - Document parameters and return values
"""
)

print("\n9.3 Performance Considerations")
print("-" * 30)
print(
    """
1. Memory Management:
   - Use __slots__ for classes with many instances
   - Implement __del__ for cleanup if needed
   - Be careful with circular references

2. Method Resolution:
   - Keep inheritance hierarchies shallow
   - Use composition over inheritance when possible
   - Understand MRO for multiple inheritance

3. Object Creation:
   - Use __new__ for immutable objects
   - Implement __copy__ and __deepcopy__ if needed
   - Consider object pooling for expensive objects
"""
)

# ============================================
# SUMMARY
# ============================================
print("\n" + "=" * 60)
print("SUMMARY")
print("=" * 60)

print(
    """
🎯 WHAT YOU'VE LEARNED:

1. CLASSES AND OBJECTS
   - Creating classes and objects
   - Instance variables and methods
   - Class variables and methods
   - Properties and getters/setters

2. INHERITANCE
   - Single inheritance
   - Multiple inheritance
   - Method overriding
   - Method Resolution Order (MRO)

3. POLYMORPHISM
   - Method overriding
   - Duck typing
   - Same interface, different implementations
   - Flexible code design

4. ENCAPSULATION
   - Access modifiers (public, protected, private)
   - Name mangling
   - Data hiding and protection
   - Controlled access to attributes

5. ABSTRACTION
   - Abstract base classes
   - Interface-like classes
   - Hiding implementation details
   - Defining contracts

6. REAL-WORLD APPLICATIONS
   - E-commerce system
   - Library management system
   - Bank account system
   - Practical OOP implementations

7. DESIGN PATTERNS
   - Singleton pattern
   - Factory pattern
   - Observer pattern
   - Common OOP patterns

8. BEST PRACTICES
   - SOLID principles
   - Code organization
   - Performance considerations
   - OOP guidelines

🚀 KEY TAKEAWAYS:
- OOP organizes code into objects with data and behavior
- Inheritance promotes code reuse and hierarchy
- Polymorphism enables flexible and extensible code
- Encapsulation protects data and controls access
- Abstraction hides complexity and defines interfaces
- Design patterns solve common programming problems
- Follow best practices for maintainable code

To run this tutorial: python python_oop.py
"""
)

print("\nHappy coding with Python OOP! 🐍🏗️")
print("Remember: Objects are the building blocks of great software!")
