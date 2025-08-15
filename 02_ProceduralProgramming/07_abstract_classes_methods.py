# Abstract Classes and Methods in Python
# Abstract classes cannot be instantiated directly and may contain abstract methods
# that must be implemented by child classes

from abc import ABC, abstractmethod
from typing import List, Dict, Any


# Abstract Base Class Example 1: Shape
class Shape(ABC):
    def __init__(self, name: str):
        self.name = name

    # Abstract method - must be implemented by child classes
    @abstractmethod
    def calculate_area(self) -> float:
        """Calculate the area of the shape. Must be implemented by subclasses."""
        pass

    @abstractmethod
    def calculate_perimeter(self) -> float:
        """Calculate the perimeter of the shape. Must be implemented by subclasses."""
        pass

    # Regular method - inherited by all child classes
    def display_info(self):
        area = self.calculate_area()
        perimeter = self.calculate_perimeter()
        print(f"{self.name}:")
        print(f"  Area: {area:.2f}")
        print(f"  Perimeter: {perimeter:.2f}")


# Concrete implementation of Shape
class Circle(Shape):
    def __init__(self, radius: float):
        super().__init__("Circle")
        self.radius = radius

    def calculate_area(self) -> float:
        import math

        return math.pi * self.radius**2

    def calculate_perimeter(self) -> float:
        import math

        return 2 * math.pi * self.radius


class Rectangle(Shape):
    def __init__(self, width: float, height: float):
        super().__init__("Rectangle")
        self.width = width
        self.height = height

    def calculate_area(self) -> float:
        return self.width * self.height

    def calculate_perimeter(self) -> float:
        return 2 * (self.width + self.height)


class Triangle(Shape):
    def __init__(self, base: float, height: float, side1: float, side2: float):
        super().__init__("Triangle")
        self.base = base
        self.height = height
        self.side1 = side1
        self.side2 = side2

    def calculate_area(self) -> float:
        return 0.5 * self.base * self.height

    def calculate_perimeter(self) -> float:
        return self.base + self.side1 + self.side2


# Abstract Base Class Example 2: Database Interface
class DatabaseInterface(ABC):
    def __init__(self, connection_string: str):
        self.connection_string = connection_string
        self.is_connected = False

    @abstractmethod
    def connect(self) -> bool:
        """Connect to the database. Must be implemented by subclasses."""
        pass

    @abstractmethod
    def disconnect(self) -> bool:
        """Disconnect from the database. Must be implemented by subclasses."""
        pass

    @abstractmethod
    def execute_query(self, query: str) -> List[Dict[str, Any]]:
        """Execute a query and return results. Must be implemented by subclasses."""
        pass

    @abstractmethod
    def insert_record(self, table: str, data: Dict[str, Any]) -> bool:
        """Insert a record into the specified table. Must be implemented by subclasses."""
        pass

    # Regular method that uses abstract methods
    def safe_execute(self, query: str) -> List[Dict[str, Any]]:
        if not self.is_connected:
            print("Not connected to database. Connecting first...")
            self.connect()

        try:
            return self.execute_query(query)
        except Exception as e:
            print(f"Error executing query: {e}")
            return []


# Concrete implementation of DatabaseInterface
class MySQLDatabase(DatabaseInterface):
    def connect(self) -> bool:
        # Simulate MySQL connection
        print(f"Connecting to MySQL database: {self.connection_string}")
        self.is_connected = True
        return True

    def disconnect(self) -> bool:
        print("Disconnecting from MySQL database")
        self.is_connected = False
        return True

    def execute_query(self, query: str) -> List[Dict[str, Any]]:
        print(f"Executing MySQL query: {query}")
        # Simulate query results
        return [{"id": 1, "name": "John"}, {"id": 2, "name": "Jane"}]

    def insert_record(self, table: str, data: Dict[str, Any]) -> bool:
        print(f"Inserting into MySQL table '{table}': {data}")
        return True


class PostgreSQLDatabase(DatabaseInterface):
    def connect(self) -> bool:
        # Simulate PostgreSQL connection
        print(f"Connecting to PostgreSQL database: {self.connection_string}")
        self.is_connected = True
        return True

    def disconnect(self) -> bool:
        print("Disconnecting from PostgreSQL database")
        self.is_connected = False
        return True

    def execute_query(self, query: str) -> List[Dict[str, Any]]:
        print(f"Executing PostgreSQL query: {query}")
        # Simulate query results
        return [{"id": 1, "name": "Alice"}, {"id": 2, "name": "Bob"}]

    def insert_record(self, table: str, data: Dict[str, Any]) -> bool:
        print(f"Inserting into PostgreSQL table '{table}': {data}")
        return True


# Abstract Base Class Example 3: Payment Processor
class PaymentProcessor(ABC):
    def __init__(self, api_key: str):
        self.api_key = api_key
        self.transaction_count = 0

    @abstractmethod
    def process_payment(self, amount: float, currency: str) -> Dict[str, Any]:
        """Process a payment. Must be implemented by subclasses."""
        pass

    @abstractmethod
    def refund_payment(self, transaction_id: str) -> bool:
        """Refund a payment. Must be implemented by subclasses."""
        pass

    def get_transaction_count(self) -> int:
        return self.transaction_count


class StripePaymentProcessor(PaymentProcessor):
    def process_payment(self, amount: float, currency: str) -> Dict[str, Any]:
        print(f"Processing Stripe payment: ${amount} {currency}")
        self.transaction_count += 1
        return {
            "transaction_id": f"stripe_{self.transaction_count}",
            "status": "success",
            "amount": amount,
            "currency": currency,
        }

    def refund_payment(self, transaction_id: str) -> bool:
        print(f"Processing Stripe refund for transaction: {transaction_id}")
        return True


class PayPalPaymentProcessor(PaymentProcessor):
    def process_payment(self, amount: float, currency: str) -> Dict[str, Any]:
        print(f"Processing PayPal payment: ${amount} {currency}")
        self.transaction_count += 1
        return {
            "transaction_id": f"paypal_{self.transaction_count}",
            "status": "success",
            "amount": amount,
            "currency": currency,
        }

    def refund_payment(self, transaction_id: str) -> bool:
        print(f"Processing PayPal refund for transaction: {transaction_id}")
        return True


# Demonstration
print("=== Abstract Classes and Methods Demo ===\n")

print("1. Shape Calculations:")
print("-" * 30)

# Create shape instances
circle = Circle(5.0)
rectangle = Rectangle(4.0, 6.0)
triangle = Triangle(3.0, 4.0, 5.0, 5.0)

# Display information for each shape
shapes = [circle, rectangle, triangle]
for shape in shapes:
    shape.display_info()
    print()

print("2. Database Operations:")
print("-" * 30)

# Create database instances
mysql_db = MySQLDatabase("mysql://localhost:3306/mydb")
postgres_db = PostgreSQLDatabase("postgresql://localhost:5432/mydb")

databases = [mysql_db, postgres_db]

for db in databases:
    # Use the safe_execute method that uses abstract methods
    results = db.safe_execute("SELECT * FROM users")
    print(f"Query results: {results}")

    # Insert a record
    db.insert_record("users", {"name": "Test User", "email": "test@example.com"})
    print()

print("3. Payment Processing:")
print("-" * 30)

# Create payment processor instances
stripe_processor = StripePaymentProcessor("stripe_api_key_123")
paypal_processor = PayPalPaymentProcessor("paypal_api_key_456")

processors = [stripe_processor, paypal_processor]

for processor in processors:
    # Process a payment
    result = processor.process_payment(99.99, "USD")
    print(f"Payment result: {result}")

    # Refund the payment
    processor.refund_payment(result["transaction_id"])
    print(f"Transaction count: {processor.get_transaction_count()}")
    print()

print("4. Abstract Class Instantiation Error:")
print("-" * 30)

try:
    # This will raise an error - cannot instantiate abstract class
    shape = Shape("Generic Shape")
except TypeError as e:
    print(f"Error: {e}")
    print("Abstract classes cannot be instantiated directly!")

print("\n5. Polymorphism with Abstract Classes:")
print("-" * 30)


# Demonstrate polymorphism - treat different implementations uniformly
def process_shapes(shapes_list: List[Shape]):
    print("Processing all shapes:")
    for shape in shapes_list:
        area = shape.calculate_area()
        print(f"{shape.name} area: {area:.2f}")


def process_payments(processors_list: List[PaymentProcessor]):
    print("Processing payments with different processors:")
    for processor in processors_list:
        result = processor.process_payment(50.00, "USD")
        print(f"Payment processed: {result}")


# Use polymorphism
process_shapes(shapes)
print()
process_payments(processors)

print("\n6. Benefits of Abstract Classes:")
print("-" * 30)
print("✅ Enforce method implementation in child classes")
print("✅ Provide common interface for related classes")
print("✅ Enable polymorphism and code reuse")
print("✅ Prevent instantiation of incomplete classes")
print("✅ Define contracts that child classes must follow")
