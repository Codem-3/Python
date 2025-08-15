# Parent Classes vs. Child Classes (Inheritance)
# Inheritance allows a child class to inherit attributes and methods from a parent class


# Parent Class (Base Class)
class Animal:
    def __init__(self, name, species, age):
        self.name = name
        self.species = species
        self.age = age
        self.is_alive = True

    def make_sound(self):
        print(f"{self.name} makes a generic animal sound")

    def eat(self, food):
        print(f"{self.name} is eating {food}")

    def sleep(self):
        print(f"{self.name} is sleeping")

    def get_info(self):
        return f"{self.name} is a {self.age}-year-old {self.species}"

    def birthday(self):
        self.age += 1
        print(f"{self.name} is now {self.age} years old!")


# Child Class 1: Dog inherits from Animal
class Dog(Animal):
    def __init__(self, name, age, breed):
        # Call parent class constructor
        super().__init__(name, "Dog", age)
        self.breed = breed
        self.loyalty_level = 10

    # Override parent method
    def make_sound(self):
        print(f"{self.name} barks: Woof! Woof!")

    # Add new method specific to Dog
    def fetch(self, item):
        print(f"{self.name} fetches the {item}")

    def wag_tail(self):
        print(f"{self.name} wags its tail happily")

    # Override get_info to include breed
    def get_info(self):
        return f"{self.name} is a {self.age}-year-old {self.breed} dog"


# Child Class 2: Cat inherits from Animal
class Cat(Animal):
    def __init__(self, name, age, color):
        super().__init__(name, "Cat", age)
        self.color = color
        self.independence_level = 10

    # Override parent method
    def make_sound(self):
        print(f"{self.name} meows: Meow!")

    # Add new method specific to Cat
    def purr(self):
        print(f"{self.name} purrs contentedly")

    def climb_tree(self):
        print(f"{self.name} climbs up a tree")

    # Override get_info to include color
    def get_info(self):
        return f"{self.name} is a {self.age}-year-old {self.color} cat"


# Child Class 3: Bird inherits from Animal
class Bird(Animal):
    def __init__(self, name, age, wing_span):
        super().__init__(name, "Bird", age)
        self.wing_span = wing_span
        self.can_fly = True

    # Override parent method
    def make_sound(self):
        print(f"{self.name} chirps: Tweet! Tweet!")

    # Add new method specific to Bird
    def fly(self):
        if self.can_fly:
            print(f"{self.name} flies through the sky")
        else:
            print(f"{self.name} cannot fly")

    def build_nest(self):
        print(f"{self.name} builds a nest")

    # Override get_info to include wing span
    def get_info(self):
        return f"{self.name} is a {self.age}-year-old bird with {self.wing_span}cm wingspan"


# Example with another inheritance hierarchy
class Vehicle:
    def __init__(self, brand, model, year):
        self.brand = brand
        self.model = model
        self.year = year
        self.is_running = False

    def start_engine(self):
        self.is_running = True
        print(f"{self.brand} {self.model} engine started")

    def stop_engine(self):
        self.is_running = False
        print(f"{self.brand} {self.model} engine stopped")

    def get_info(self):
        return f"{self.brand} {self.model} ({self.year})"


class Car(Vehicle):
    def __init__(self, brand, model, year, num_doors):
        super().__init__(brand, model, year)
        self.num_doors = num_doors
        self.fuel_type = "Gasoline"

    def honk(self):
        print(f"{self.brand} {self.model} honks: Beep! Beep!")

    def get_info(self):
        return f"{self.brand} {self.model} ({self.year}) - {self.num_doors} doors"


class Motorcycle(Vehicle):
    def __init__(self, brand, model, year, engine_size):
        super().__init__(brand, model, year)
        self.engine_size = engine_size
        self.has_sidecar = False

    def wheelie(self):
        print(f"{self.brand} {self.model} does a wheelie!")

    def get_info(self):
        return f"{self.brand} {self.model} ({self.year}) - {self.engine_size}cc engine"


# Demonstration
print("=== Animal Inheritance Demo ===\n")

# Create instances of different animals
my_dog = Dog("Buddy", 3, "Golden Retriever")
my_cat = Cat("Whiskers", 2, "Orange")
my_bird = Bird("Tweety", 1, 15)

# Demonstrate inheritance - all animals can use parent methods
print("All animals can eat and sleep:")
my_dog.eat("dog food")
my_cat.eat("cat food")
my_bird.eat("seeds")

print()
my_dog.sleep()
my_cat.sleep()
my_bird.sleep()

print("\n" + "=" * 50)
print("=== Method Overriding Demo ===\n")

# Each child class overrides the make_sound method
print("Different animals make different sounds:")
my_dog.make_sound()
my_cat.make_sound()
my_bird.make_sound()

print("\n" + "=" * 50)
print("=== Child-Specific Methods ===\n")

# Each child has its own unique methods
print("Dog-specific behavior:")
my_dog.fetch("ball")
my_dog.wag_tail()

print("\nCat-specific behavior:")
my_cat.purr()
my_cat.climb_tree()

print("\nBird-specific behavior:")
my_bird.fly()
my_bird.build_nest()

print("\n" + "=" * 50)
print("=== Information Display ===\n")

# Each child overrides get_info to show relevant information
print("Animal information:")
print(my_dog.get_info())
print(my_cat.get_info())
print(my_bird.get_info())

print("\n" + "=" * 50)
print("=== Vehicle Inheritance Demo ===\n")

# Create vehicle instances
my_car = Car("Toyota", "Camry", 2020, 4)
my_motorcycle = Motorcycle("Honda", "CBR600", 2019, 600)

# Demonstrate inheritance
print("Starting vehicles:")
my_car.start_engine()
my_motorcycle.start_engine()

print("\nVehicle-specific behavior:")
my_car.honk()
my_motorcycle.wheelie()

print("\nVehicle information:")
print(my_car.get_info())
print(my_motorcycle.get_info())

print("\n" + "=" * 50)
print("=== Inheritance Benefits ===\n")

# Demonstrate polymorphism - same method, different behavior
animals = [my_dog, my_cat, my_bird]
print("Polymorphism - same method, different behavior:")
for animal in animals:
    animal.make_sound()

print("\nAll animals can use parent methods:")
for animal in animals:
    animal.birthday()

print("\n" + "=" * 50)
print("=== Checking Inheritance ===\n")

# Check if objects are instances of their classes
print(f"Is my_dog a Dog? {isinstance(my_dog, Dog)}")
print(f"Is my_dog an Animal? {isinstance(my_dog, Animal)}")
print(f"Is my_cat a Dog? {isinstance(my_cat, Dog)}")

# Check class hierarchy
print(f"\nDog class bases: {Dog.__bases__}")
print(f"Cat class bases: {Cat.__bases__}")
print(f"Animal class bases: {Animal.__bases__}")
