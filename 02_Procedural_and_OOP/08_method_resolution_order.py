# Method Resolution Order (MRO) in Python
# MRO determines the order in which Python searches for methods in inheritance hierarchies


class A:
    def method(self):
        print("A.method() called")

    def common_method(self):
        print("A.common_method() called")


class B:
    def method(self):
        print("B.method() called")

    def common_method(self):
        print("B.common_method() called")


class C:
    def method(self):
        print("C.method() called")

    def common_method(self):
        print("C.common_method() called")


# Single Inheritance
class SingleChild(A):
    def child_method(self):
        print("SingleChild.child_method() called")


# Multiple Inheritance - Linear
class LinearChild(A, B):
    pass


# Multiple Inheritance - Diamond Problem
class DiamondChild(A, B, C):
    pass


# Multiple Inheritance - Complex
class ComplexChild(A, B, C):
    def complex_method(self):
        print("ComplexChild.complex_method() called")


# Example with method overriding
class OverrideChild(A, B, C):
    def method(self):
        print("OverrideChild.method() called")
        # Call parent method using super()
        super().method()


# Example with super() calls
class SuperChild(A, B, C):
    def method(self):
        print("SuperChild.method() called")
        # Call next method in MRO
        super().method()


# Example with __init__ methods
class Parent1:
    def __init__(self, name):
        self.name = name
        print(f"Parent1.__init__() called with name: {name}")


class Parent2:
    def __init__(self, age):
        self.age = age
        print(f"Parent2.__init__() called with age: {age}")


class ChildWithInit(Parent1, Parent2):
    def __init__(self, name, age, city):
        # Call parent constructors in MRO order
        Parent1.__init__(self, name)
        Parent2.__init__(self, age)
        self.city = city
        print(f"ChildWithInit.__init__() called with city: {city}")


# Demonstration
print("=== Method Resolution Order (MRO) Demo ===\n")

print("1. Single Inheritance MRO:")
print("-" * 30)
single = SingleChild()
print(f"SingleChild MRO: {SingleChild.__mro__}")
single.method()  # Calls A.method()
single.common_method()  # Calls A.common_method()
print()

print("2. Linear Multiple Inheritance MRO:")
print("-" * 30)
linear = LinearChild()
print(f"LinearChild MRO: {LinearChild.__mro__}")
linear.method()  # Calls A.method() (first in MRO)
linear.common_method()  # Calls A.common_method() (first in MRO)
print()

print("3. Diamond Problem MRO:")
print("-" * 30)
diamond = DiamondChild()
print(f"DiamondChild MRO: {DiamondChild.__mro__}")
diamond.method()  # Calls A.method() (first in MRO)
diamond.common_method()  # Calls A.common_method() (first in MRO)
print()

print("4. Complex Multiple Inheritance MRO:")
print("-" * 30)
complex_child = ComplexChild()
print(f"ComplexChild MRO: {ComplexChild.__mro__}")
complex_child.method()  # Calls A.method() (first in MRO)
complex_child.common_method()  # Calls A.common_method() (first in MRO)
complex_child.complex_method()  # Calls its own method
print()

print("5. Method Overriding MRO:")
print("-" * 30)
override = OverrideChild()
print(f"OverrideChild MRO: {OverrideChild.__mro__}")
override.method()  # Calls its own method, then A.method() via super()
print()

print("6. Super() Chain MRO:")
print("-" * 30)
super_child = SuperChild()
print(f"SuperChild MRO: {SuperChild.__mro__}")
super_child.method()  # Calls its own method, then A.method() via super()
print()

print("7. Constructor MRO:")
print("-" * 30)
child_init = ChildWithInit("John", 25, "New York")
print(f"ChildWithInit MRO: {ChildWithInit.__mro__}")
print(
    f"Attributes: name={child_init.name}, age={child_init.age}, city={child_init.city}"
)
print()

print("8. MRO Visualization:")
print("-" * 30)


def print_mro_hierarchy(class_name):
    """Print the MRO hierarchy in a readable format"""
    print(f"\nMRO for {class_name.__name__}:")
    for i, cls in enumerate(class_name.__mro__):
        print(f"  {i}: {cls.__name__}")


print_mro_hierarchy(SingleChild)
print_mro_hierarchy(LinearChild)
print_mro_hierarchy(DiamondChild)
print_mro_hierarchy(ComplexChild)
print_mro_hierarchy(OverrideChild)
print_mro_hierarchy(SuperChild)
print_mro_hierarchy(ChildWithInit)

print("\n9. MRO Rules and Examples:")
print("-" * 30)


# Example showing MRO with different inheritance orders
class X:
    def method(self):
        print("X.method() called")


class Y:
    def method(self):
        print("Y.method() called")


class Z:
    def method(self):
        print("Z.method() called")


class Order1(X, Y, Z):
    pass


class Order2(Y, Z, X):
    pass


class Order3(Z, X, Y):
    pass


print("Different inheritance orders result in different MROs:")
print(f"Order1(X, Y, Z) MRO: {Order1.__mro__}")
print(f"Order2(Y, Z, X) MRO: {Order2.__mro__}")
print(f"Order3(Z, X, Y) MRO: {Order3.__mro__}")

print("\nTesting method calls:")
order1 = Order1()
order2 = Order2()
order3 = Order3()

print("Order1.method():", end=" ")
order1.method()
print("Order2.method():", end=" ")
order2.method()
print("Order3.method():", end=" ")
order3.method()

print("\n10. MRO with Abstract Methods:")
print("-" * 30)

from abc import ABC, abstractmethod


class AbstractBase(ABC):
    @abstractmethod
    def abstract_method(self):
        pass

    def concrete_method(self):
        print("AbstractBase.concrete_method() called")


class ConcreteClass(AbstractBase):
    def abstract_method(self):
        print("ConcreteClass.abstract_method() called")


class MixedInheritance(ConcreteClass, AbstractBase):
    pass


print(f"MixedInheritance MRO: {MixedInheritance.__mro__}")
mixed = MixedInheritance()
mixed.abstract_method()
mixed.concrete_method()

print("\n11. MRO Benefits and Best Practices:")
print("-" * 30)
print("✅ Predictable method resolution order")
print("✅ Prevents the diamond problem")
print("✅ Enables cooperative multiple inheritance")
print("✅ Maintains consistency across Python versions")
print("✅ Allows for method chaining with super()")
print("✅ Provides clear inheritance hierarchy")

print("\n12. Common MRO Patterns:")
print("-" * 30)
print("• Single inheritance: Class -> Parent")
print("• Multiple inheritance: Class -> Parent1 -> Parent2 -> ...")
print("• Diamond inheritance: Class -> Parent1 -> Grandparent -> Parent2")
print("• Mixin pattern: Class -> Mixin1 -> Mixin2 -> BaseClass")
print("• Interface pattern: Class -> Interface1 -> Interface2 -> Object")
