# Function and Variable Scope in Python
# This file demonstrates the four levels of scope in Python

print("=== FUNCTION AND VARIABLE SCOPE EXAMPLES ===\n")

# ========================================
# 1. LOCAL SCOPE
# ========================================

print("1. LOCAL SCOPE")
print("-" * 40)


def get_total(a, b):
    """Demonstrate local scope - variables declared inside a function"""
    # Local variable declared inside a function
    total = a + b
    print(f"Inside function: total = {total}")
    return total


# Call the function
result = get_total(5, 2)
print(f"Function returned: {result}")

# Try to access 'total' outside the function (will cause error)
try:
    print(f"Trying to access 'total' outside function: {total}")
except NameError as e:
    print(f"Error accessing 'total' outside function: {e}")

print()


def demonstrate_local_scope():
    """Show multiple local variables"""
    local_var1 = "I'm local to this function"
    local_var2 = 42
    local_var3 = [1, 2, 3]

    print(f"Inside function: {local_var1}")
    print(f"Inside function: {local_var2}")
    print(f"Inside function: {local_var3}")

    # All these variables are only accessible within this function
    return "Function completed"


demonstrate_local_scope()

# These variables are not accessible here
try:
    print(f"local_var1: {local_var1}")
except NameError as e:
    print(f"Cannot access local_var1: {e}")

print()

# ========================================
# 2. ENCLOSING SCOPE (NESTED FUNCTIONS)
# ========================================

print("2. ENCLOSING SCOPE")
print("-" * 40)


def outer_function(x, y):
    """Demonstrate enclosing scope with nested functions"""
    # Enclosing scope variable
    outer_var = x + y
    print(f"Outer function: outer_var = {outer_var}")

    def inner_function():
        """Inner function can access variables from enclosing scope"""
        # Can access outer_var from enclosing scope
        inner_result = outer_var * 2
        print(f"Inner function: outer_var * 2 = {inner_result}")

        # Local variable to inner function
        local_to_inner = "I'm local to inner function"
        print(f"Inner function: {local_to_inner}")

        return inner_result

    # Call inner function
    result = inner_function()

    # Cannot access local_to_inner here (it's local to inner_function)
    try:
        print(f"Trying to access local_to_inner from outer: {local_to_inner}")
    except NameError as e:
        print(f"Cannot access local_to_inner from outer: {e}")

    return result


# Test enclosing scope
outer_result = outer_function(3, 4)
print(f"Outer function returned: {outer_result}")

print()


def demonstrate_nested_scopes():
    """More complex example of nested scopes"""
    level1_var = "Level 1"

    def level2_function():
        level2_var = "Level 2"
        print(f"Level 2 can access: {level1_var}")

        def level3_function():
            level3_var = "Level 3"
            print(f"Level 3 can access: {level1_var} and {level2_var}")
            print(f"Level 3 has its own: {level3_var}")

        level3_function()
        # Level 2 cannot access level3_var
        try:
            print(f"Level 2 trying to access level3_var: {level3_var}")
        except NameError as e:
            print(f"Level 2 cannot access level3_var: {e}")

    level2_function()


demonstrate_nested_scopes()
print()

# ========================================
# 3. GLOBAL SCOPE
# ========================================

print("3. GLOBAL SCOPE")
print("-" * 40)

# Global variables declared outside any function
global_var1 = "I'm a global variable"
global_var2 = 100
global_list = [1, 2, 3, 4, 5]

print(f"Global variables accessible everywhere:")
print(f"global_var1: {global_var1}")
print(f"global_var2: {global_var2}")
print(f"global_list: {global_list}")


def access_global_variables():
    """Function that accesses global variables"""
    print(f"Inside function - global_var1: {global_var1}")
    print(f"Inside function - global_var2: {global_var2}")
    print(f"Inside function - global_list: {global_list}")

    # Can read global variables
    modified_list = global_list.copy()
    modified_list.append(6)
    print(f"Modified copy of global_list: {modified_list}")


access_global_variables()


def modify_global_variable():
    """Function that modifies a global variable"""
    global global_var2  # Declare that we want to modify the global variable

    print(f"Before modification: global_var2 = {global_var2}")
    global_var2 = 200
    print(f"After modification: global_var2 = {global_var2}")


modify_global_variable()
print(f"Outside function - global_var2 is now: {global_var2}")


def demonstrate_global_vs_local():
    """Show the difference between global and local variables"""
    local_var = "I'm local"
    print(f"Inside function - local_var: {local_var}")
    print(f"Inside function - global_var1: {global_var1}")


demonstrate_global_vs_local()

# Cannot access local_var from global scope
try:
    print(f"Global scope trying to access local_var: {local_var}")
except NameError as e:
    print(f"Cannot access local_var from global scope: {e}")

print()

# ========================================
# 4. BUILT-IN SCOPE
# ========================================

print("4. BUILT-IN SCOPE")
print("-" * 40)

print("Built-in functions and objects are available everywhere:")
print(f"len() function: {len([1, 2, 3])}")
print(f"print() function: available")
print(f"str() function: {str(42)}")
print(f"int() function: {int('42')}")
print(f"list() function: {list('hello')}")


def demonstrate_built_in_scope():
    """Show that built-in functions are available in any scope"""
    # These are all built-in functions
    my_list = list(range(5))
    my_string = str(123)
    my_length = len(my_list)

    print(f"Built-ins work in functions: {my_list}, {my_string}, {my_length}")


demonstrate_built_in_scope()


# Shadowing built-in functions (not recommended)
def demonstrate_shadowing():
    """Show how local variables can shadow built-in functions"""
    # This shadows the built-in len() function
    len = "I'm not the len() function anymore"
    print(f"Local 'len' variable: {len}")

    # Now we can't use the built-in len() function
    try:
        length = len([1, 2, 3])
        print(f"Length: {length}")
    except TypeError as e:
        print(f"Cannot use built-in len() because it's shadowed: {e}")


demonstrate_shadowing()

# Built-in len() is still available in global scope
print(f"Built-in len() still works in global scope: {len([1, 2, 3])}")

print()

# ========================================
# 5. PRACTICAL EXAMPLES
# ========================================

print("5. PRACTICAL EXAMPLES")
print("-" * 40)

# Example 1: Counter with global variable
counter = 0


def increment_counter():
    global counter
    counter += 1
    return counter


def reset_counter():
    global counter
    counter = 0
    return counter


print("Counter example:")
print(f"Initial counter: {counter}")
print(f"After increment: {increment_counter()}")
print(f"After increment: {increment_counter()}")
print(f"After reset: {reset_counter()}")

print()

# Example 2: Configuration with global variables
CONFIG = {"debug": True, "max_retries": 3, "timeout": 30}


def get_config(key):
    """Get configuration value"""
    return CONFIG.get(key)


def update_config(key, value):
    """Update configuration value"""
    global CONFIG
    CONFIG[key] = value


print("Configuration example:")
print(f"Debug mode: {get_config('debug')}")
print(f"Max retries: {get_config('max_retries')}")
update_config("timeout", 60)
print(f"Updated timeout: {get_config('timeout')}")

print()


# Example 3: Factory function with closure
def create_multiplier(factor):
    """Create a function that multiplies by the given factor"""

    def multiplier(x):
        return x * factor  # factor is from enclosing scope

    return multiplier


double = create_multiplier(2)
triple = create_multiplier(3)

print("Factory function example:")
print(f"double(5): {double(5)}")
print(f"triple(5): {triple(5)}")

print()

# Example 4: Scope resolution order demonstration
x = "global x"


def scope_demo():
    x = "local x"

    def inner():
        x = "inner x"
        print(f"Inner function: x = {x}")

    inner()
    print(f"Outer function: x = {x}")


print("Scope resolution order:")
scope_demo()
print(f"Global scope: x = {x}")

print()


# Example 5: Nonlocal keyword (Python 3)
def outer_nonlocal():
    x = "outer"

    def inner():
        nonlocal x  # Refers to x in the enclosing scope
        x = "modified by inner"
        print(f"Inner function: x = {x}")

    print(f"Before inner: x = {x}")
    inner()
    print(f"After inner: x = {x}")


print("Nonlocal keyword example:")
outer_nonlocal()

print("\n=== END OF SCOPE EXAMPLES ===")
