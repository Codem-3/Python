"""
Python Packages and Package Management Tutorial
==============================================

This tutorial covers:
1. What are packages and why use them
2. Package structure and organization
3. Creating your own packages
4. Package management with pip
5. Virtual environments
6. Requirements files
7. Package distribution
8. Best practices
"""

import os
import sys
import subprocess
import json
from pathlib import Path

# 1. WHAT ARE PACKAGES?
print("=" * 60)
print("1. WHAT ARE PACKAGES?")
print("=" * 60)

"""
A package is a collection of modules organized in a directory structure.
Packages help organize related modules and provide a namespace for them.
"""

# 2. PACKAGE STRUCTURE
print("\n" + "=" * 60)
print("2. PACKAGE STRUCTURE")
print("=" * 60)

print(
    """
Basic Package Structure:
my_package/
├── __init__.py          # Makes the directory a package
├── module1.py           # Individual modules
├── module2.py
├── subpackage/          # Sub-packages
│   ├── __init__.py
│   └── submodule.py
└── setup.py             # For distribution (optional)
"""
)

# 3. CREATING YOUR OWN PACKAGE
print("\n" + "=" * 60)
print("3. CREATING YOUR OWN PACKAGE")
print("=" * 60)


def create_sample_package():
    """Create a sample package structure for demonstration"""

    # Create package directory
    package_dir = Path("03_Packages_Modules_Libraries_Tools/Examples/my_math_package")
    package_dir.mkdir(parents=True, exist_ok=True)

    # Create __init__.py
    init_content = '''"""
My Math Package
A collection of mathematical utilities
"""

# Import main functions to make them available at package level
from .basic_math import add, subtract, multiply, divide
from .advanced_math import power, sqrt, factorial
from .statistics import mean, median, mode

# Package metadata
__version__ = "1.0.0"
__author__ = "Your Name"
__email__ = "your.email@example.com"

# Define what gets imported with 'from package import *'
__all__ = [
    'add', 'subtract', 'multiply', 'divide',
    'power', 'sqrt', 'factorial',
    'mean', 'median', 'mode'
]

print("My Math Package loaded successfully!")
'''

    with open(package_dir / "__init__.py", "w") as f:
        f.write(init_content)

    # Create basic_math.py
    basic_math_content = '''"""
Basic mathematical operations
"""

def add(a, b):
    """Add two numbers"""
    return a + b

def subtract(a, b):
    """Subtract b from a"""
    return a - b

def multiply(a, b):
    """Multiply two numbers"""
    return a * b

def divide(a, b):
    """Divide a by b"""
    if b == 0:
        raise ValueError("Cannot divide by zero")
    return a / b
'''

    with open(package_dir / "basic_math.py", "w") as f:
        f.write(basic_math_content)

    # Create advanced_math.py
    advanced_math_content = '''"""
Advanced mathematical operations
"""

import math

def power(base, exponent):
    """Raise base to the power of exponent"""
    return base ** exponent

def sqrt(number):
    """Calculate square root of a number"""
    if number < 0:
        raise ValueError("Cannot calculate square root of negative number")
    return math.sqrt(number)

def factorial(n):
    """Calculate factorial of n"""
    if n < 0:
        raise ValueError("Factorial is not defined for negative numbers")
    if n == 0 or n == 1:
        return 1
    return math.factorial(n)
'''

    with open(package_dir / "advanced_math.py", "w") as f:
        f.write(advanced_math_content)

    # Create statistics.py
    stats_content = '''"""
Statistical functions
"""

from collections import Counter

def mean(numbers):
    """Calculate arithmetic mean"""
    if not numbers:
        raise ValueError("Cannot calculate mean of empty list")
    return sum(numbers) / len(numbers)

def median(numbers):
    """Calculate median"""
    if not numbers:
        raise ValueError("Cannot calculate median of empty list")
    
    sorted_numbers = sorted(numbers)
    n = len(sorted_numbers)
    
    if n % 2 == 0:
        # Even number of elements
        mid1 = sorted_numbers[n // 2 - 1]
        mid2 = sorted_numbers[n // 2]
        return (mid1 + mid2) / 2
    else:
        # Odd number of elements
        return sorted_numbers[n // 2]

def mode(numbers):
    """Calculate mode (most frequent value)"""
    if not numbers:
        raise ValueError("Cannot calculate mode of empty list")
    
    counter = Counter(numbers)
    max_count = max(counter.values())
    modes = [num for num, count in counter.items() if count == max_count]
    
    return modes[0] if len(modes) == 1 else modes
'''

    with open(package_dir / "statistics.py", "w") as f:
        f.write(stats_content)

    # Create subpackage
    subpackage_dir = package_dir / "utils"
    subpackage_dir.mkdir(exist_ok=True)

    # Create subpackage __init__.py
    sub_init_content = '''"""
Utility functions subpackage
"""

from .helpers import format_number, validate_input

__all__ = ['format_number', 'validate_input']
'''

    with open(subpackage_dir / "__init__.py", "w") as f:
        f.write(sub_init_content)

    # Create helpers.py
    helpers_content = '''"""
Helper utility functions
"""

def format_number(number, decimal_places=2):
    """Format a number with specified decimal places"""
    return round(number, decimal_places)

def validate_input(value, expected_type):
    """Validate input type"""
    if not isinstance(value, expected_type):
        raise TypeError(f"Expected {expected_type.__name__}, got {type(value).__name__}")
    return value
'''

    with open(subpackage_dir / "helpers.py", "w") as f:
        f.write(helpers_content)

    print("Created sample package: my_math_package")
    print("Package structure:")
    print("my_math_package/")
    print("├── __init__.py")
    print("├── basic_math.py")
    print("├── advanced_math.py")
    print("├── statistics.py")
    print("└── utils/")
    print("    ├── __init__.py")
    print("    └── helpers.py")


create_sample_package()

# 4. USING YOUR PACKAGE
print("\n" + "=" * 60)
print("4. USING YOUR PACKAGE")
print("=" * 60)

# Add the Examples directory to Python path
sys.path.append("03_Packages_Modules_Libraries_Tools/Examples")

print("\n--- Using the package ---")
try:
    # Import the entire package
    import my_math_package

    print(f"Package version: {my_math_package.__version__}")

    # Use functions from the package
    print(f"Add: {my_math_package.add(5, 3)}")
    print(f"Multiply: {my_math_package.multiply(4, 7)}")
    print(f"Power: {my_math_package.power(2, 8)}")
    print(f"Square root: {my_math_package.sqrt(16)}")

    # Use statistics functions
    numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
    print(f"Mean: {my_math_package.mean(numbers)}")
    print(f"Median: {my_math_package.median(numbers)}")

    # Use subpackage
    from my_math_package.utils import format_number, validate_input

    print(f"Formatted number: {format_number(3.14159, 3)}")

    # Import specific modules
    from my_math_package import basic_math, advanced_math

    print(f"From basic_math: {basic_math.divide(10, 2)}")
    print(f"From advanced_math: {advanced_math.factorial(5)}")

except ImportError as e:
    print(f"Import error: {e}")

# 5. PACKAGE MANAGEMENT WITH PIP
print("\n" + "=" * 60)
print("5. PACKAGE MANAGEMENT WITH PIP")
print("=" * 60)

print(
    """
Pip is Python's package installer. It allows you to install and manage
third-party packages from the Python Package Index (PyPI).

Common pip commands:
- pip install package_name          # Install a package
- pip install package_name==1.2.3   # Install specific version
- pip install -r requirements.txt   # Install from requirements file
- pip uninstall package_name        # Uninstall a package
- pip list                          # List installed packages
- pip show package_name             # Show package details
- pip freeze                        # Output installed packages
- pip search package_name           # Search for packages
- pip install --upgrade package_name # Upgrade a package
"""
)

# 6. VIRTUAL ENVIRONMENTS
print("\n" + "=" * 60)
print("6. VIRTUAL ENVIRONMENTS")
print("=" * 60)

print(
    """
Virtual environments are isolated Python environments that allow you to:
- Install packages without affecting the system Python
- Have different package versions for different projects
- Avoid conflicts between project dependencies

Creating and using virtual environments:
1. Create: python -m venv myenv
2. Activate: 
   - Windows: myenv\\Scripts\\activate
   - Unix/Mac: source myenv/bin/activate
3. Deactivate: deactivate
4. Delete: Remove the directory
"""
)

# 7. REQUIREMENTS FILES
print("\n" + "=" * 60)
print("7. REQUIREMENTS FILES")
print("=" * 60)


def create_requirements_files():
    """Create example requirements files"""

    # Basic requirements.txt
    basic_requirements = """# Basic requirements file
# Core dependencies
requests>=2.25.0
numpy>=1.20.0
pandas>=1.3.0

# Development dependencies
pytest>=6.0.0
black>=21.0.0
flake8>=3.8.0

# Optional dependencies
matplotlib>=3.3.0
seaborn>=0.11.0
"""

    with open(
        "03_Packages_Modules_Libraries_Tools/Examples/requirements.txt", "w"
    ) as f:
        f.write(basic_requirements)

    # Development requirements
    dev_requirements = """# Development requirements
# Include all basic requirements
-r requirements.txt

# Additional development tools
pytest-cov>=2.10.0
pre-commit>=2.15.0
mypy>=0.800
"""

    with open(
        "03_Packages_Modules_Libraries_Tools/Examples/requirements-dev.txt", "w"
    ) as f:
        f.write(dev_requirements)

    print("Created requirements files:")
    print("- requirements.txt (basic dependencies)")
    print("- requirements-dev.txt (development dependencies)")


create_requirements_files()

# 8. PACKAGE DISTRIBUTION
print("\n" + "=" * 60)
print("8. PACKAGE DISTRIBUTION")
print("=" * 60)


def create_setup_files():
    """Create setup.py and other distribution files"""

    # setup.py
    setup_content = '''"""
Setup script for my_math_package
"""

from setuptools import setup, find_packages

with open("README.md", "r", encoding="utf-8") as fh:
    long_description = fh.read()

with open("requirements.txt", "r", encoding="utf-8") as fh:
    requirements = [line.strip() for line in fh if line.strip() and not line.startswith("#")]

setup(
    name="my-math-package",
    version="1.0.0",
    author="Your Name",
    author_email="your.email@example.com",
    description="A collection of mathematical utilities",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/yourusername/my-math-package",
    packages=find_packages(),
    classifiers=[
        "Development Status :: 3 - Alpha",
        "Intended Audience :: Developers",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
        "Programming Language :: Python :: 3",
        "Programming Language :: Python :: 3.7",
        "Programming Language :: Python :: 3.8",
        "Programming Language :: Python :: 3.9",
        "Programming Language :: Python :: 3.10",
    ],
    python_requires=">=3.7",
    install_requires=requirements,
    extras_require={
        "dev": [
            "pytest>=6.0.0",
            "black>=21.0.0",
            "flake8>=3.8.0",
        ],
    },
)
'''

    with open("03_Packages_Modules_Libraries_Tools/Examples/setup.py", "w") as f:
        f.write(setup_content)

    # README.md
    readme_content = """# My Math Package

A collection of mathematical utilities for Python.

## Installation

```bash
pip install my-math-package
```

## Usage

```python
import my_math_package

# Basic operations
result = my_math_package.add(5, 3)
print(result)  # 8

# Advanced operations
power_result = my_math_package.power(2, 8)
print(power_result)  # 256

# Statistics
numbers = [1, 2, 3, 4, 5]
mean_value = my_math_package.mean(numbers)
print(mean_value)  # 3.0
```

## Features

- Basic mathematical operations
- Advanced mathematical functions
- Statistical calculations
- Utility functions

## Development

1. Clone the repository
2. Create a virtual environment: `python -m venv venv`
3. Activate the virtual environment
4. Install development dependencies: `pip install -r requirements-dev.txt`
5. Run tests: `pytest`

## License

MIT License
"""

    with open("03_Packages_Modules_Libraries_Tools/Examples/README.md", "w") as f:
        f.write(readme_content)

    # MANIFEST.in
    manifest_content = """include README.md
include requirements.txt
include LICENSE
recursive-include my_math_package *.py
"""

    with open("03_Packages_Modules_Libraries_Tools/Examples/MANIFEST.in", "w") as f:
        f.write(manifest_content)

    print("Created distribution files:")
    print("- setup.py (package configuration)")
    print("- README.md (documentation)")
    print("- MANIFEST.in (include/exclude files)")


create_setup_files()

# 9. BEST PRACTICES
print("\n" + "=" * 60)
print("9. BEST PRACTICES")
print("=" * 60)

print(
    """
Package Development Best Practices:

1. Package Structure:
   - Use clear, descriptive names
   - Organize modules logically
   - Include __init__.py files
   - Use relative imports within packages

2. Documentation:
   - Include docstrings for all functions/classes
   - Create a comprehensive README
   - Document installation and usage
   - Include examples

3. Version Management:
   - Use semantic versioning (MAJOR.MINOR.PATCH)
   - Keep version in __init__.py
   - Update version with each release

4. Dependencies:
   - Specify minimum versions
   - Use requirements files
   - Separate dev dependencies
   - Avoid unnecessary dependencies

5. Testing:
   - Write unit tests for all functions
   - Use pytest or unittest
   - Aim for high test coverage
   - Test on multiple Python versions

6. Code Quality:
   - Follow PEP 8 style guide
   - Use type hints
   - Run linters (flake8, pylint)
   - Use formatters (black, isort)

7. Distribution:
   - Use setuptools for packaging
   - Include setup.py or pyproject.toml
   - Create wheel distributions
   - Upload to PyPI for public packages
"""
)

# 10. ADVANCED PACKAGE FEATURES
print("\n" + "=" * 60)
print("10. ADVANCED PACKAGE FEATURES")
print("=" * 60)


def create_advanced_package():
    """Create an advanced package with more features"""

    advanced_dir = Path("03_Packages_Modules_Libraries_Tools/Examples/advanced_package")
    advanced_dir.mkdir(parents=True, exist_ok=True)

    # Advanced __init__.py with lazy loading
    advanced_init = '''"""
Advanced Package with Lazy Loading
"""

import importlib
import sys
from typing import Any

class LazyModule:
    """Lazy loading module wrapper"""
    
    def __init__(self, module_name: str):
        self.module_name = module_name
        self._module = None
    
    def __getattr__(self, name: str) -> Any:
        if self._module is None:
            self._module = importlib.import_module(self.module_name)
        return getattr(self._module, name)

# Lazy load heavy modules
numpy = LazyModule('numpy')
pandas = LazyModule('pandas')

# Version info
__version__ = "2.0.0"
__author__ = "Advanced Developer"

def get_version():
    """Get package version"""
    return __version__

def get_info():
    """Get package information"""
    return {
        "name": "advanced_package",
        "version": __version__,
        "author": __author__,
        "description": "Advanced package with lazy loading"
    }
'''

    with open(advanced_dir / "__init__.py", "w") as f:
        f.write(advanced_init)

    # Configuration module
    config_content = '''"""
Configuration management for the package
"""

import os
from typing import Dict, Any

class Config:
    """Configuration manager"""
    
    def __init__(self):
        self._config = {}
        self._load_defaults()
        self._load_from_env()
    
    def _load_defaults(self):
        """Load default configuration"""
        self._config = {
            "debug": False,
            "log_level": "INFO",
            "cache_enabled": True,
            "max_cache_size": 1000
        }
    
    def _load_from_env(self):
        """Load configuration from environment variables"""
        env_mapping = {
            "DEBUG": "debug",
            "LOG_LEVEL": "log_level",
            "CACHE_ENABLED": "cache_enabled",
            "MAX_CACHE_SIZE": "max_cache_size"
        }
        
        for env_var, config_key in env_mapping.items():
            if env_var in os.environ:
                value = os.environ[env_var]
                # Convert string values to appropriate types
                if config_key == "debug":
                    self._config[config_key] = value.lower() == "true"
                elif config_key == "max_cache_size":
                    self._config[config_key] = int(value)
                else:
                    self._config[config_key] = value
    
    def get(self, key: str, default: Any = None) -> Any:
        """Get configuration value"""
        return self._config.get(key, default)
    
    def set(self, key: str, value: Any) -> None:
        """Set configuration value"""
        self._config[key] = value
    
    def to_dict(self) -> Dict[str, Any]:
        """Get all configuration as dictionary"""
        return self._config.copy()

# Global configuration instance
config = Config()
'''

    with open(advanced_dir / "config.py", "w") as f:
        f.write(config_content)

    print("Created advanced package with:")
    print("- Lazy loading of heavy modules")
    print("- Configuration management")
    print("- Environment variable support")


create_advanced_package()

# 11. PACKAGE TESTING
print("\n" + "=" * 60)
print("11. PACKAGE TESTING")
print("=" * 60)


def create_test_files():
    """Create test files for the package"""

    test_dir = Path("03_Packages_Modules_Libraries_Tools/Examples/tests")
    test_dir.mkdir(parents=True, exist_ok=True)

    # Test __init__.py
    test_init = '''"""
Test package
"""
'''

    with open(test_dir / "__init__.py", "w") as f:
        f.write(test_init)

    # Test basic math
    test_basic_math = '''"""
Tests for basic math functions
"""

import sys
import os
sys.path.append(os.path.join(os.path.dirname(__file__), '..'))

import pytest
from my_math_package.basic_math import add, subtract, multiply, divide

class TestBasicMath:
    """Test basic mathematical operations"""
    
    def test_add(self):
        """Test addition function"""
        assert add(2, 3) == 5
        assert add(-1, 1) == 0
        assert add(0, 0) == 0
    
    def test_subtract(self):
        """Test subtraction function"""
        assert subtract(5, 3) == 2
        assert subtract(1, 1) == 0
        assert subtract(0, 5) == -5
    
    def test_multiply(self):
        """Test multiplication function"""
        assert multiply(2, 3) == 6
        assert multiply(-2, 3) == -6
        assert multiply(0, 5) == 0
    
    def test_divide(self):
        """Test division function"""
        assert divide(6, 2) == 3
        assert divide(5, 2) == 2.5
        assert divide(0, 5) == 0
    
    def test_divide_by_zero(self):
        """Test division by zero raises error"""
        with pytest.raises(ValueError, match="Cannot divide by zero"):
            divide(5, 0)
'''

    with open(test_dir / "test_basic_math.py", "w") as f:
        f.write(test_basic_math)

    # pytest.ini
    pytest_ini = """[pytest]
testpaths = tests
python_files = test_*.py
python_classes = Test*
python_functions = test_*
addopts = -v --tb=short
"""

    with open("03_Packages_Modules_Libraries_Tools/Examples/pytest.ini", "w") as f:
        f.write(pytest_ini)

    print("Created test files:")
    print("- tests/test_basic_math.py")
    print("- pytest.ini (test configuration)")


create_test_files()

# 12. EXERCISES
print("\n" + "=" * 60)
print("12. EXERCISES")
print("=" * 60)

print(
    """
Exercises to practice package development:

1. Create a package for string utilities with functions like:
   - reverse_string()
   - count_vowels()
   - is_palindrome()
   - format_phone_number()

2. Create a package for file operations with functions like:
   - read_file_safely()
   - write_json()
   - backup_file()
   - find_files_by_extension()

3. Create a package with subpackages:
   - data_processing/
     - cleaning.py
     - validation.py
     - transformation.py
   - visualization/
     - charts.py
     - plots.py

4. Add configuration management to your packages

5. Write comprehensive tests for your packages

6. Create setup.py and requirements files

7. Practice using virtual environments

8. Learn to use pip for package management
"""
)

if __name__ == "__main__":
    print("\n" + "=" * 60)
    print("PACKAGE MANAGEMENT TUTORIAL COMPLETED!")
    print("=" * 60)
    print(
        "Check the Examples folder for sample packages and files created during this tutorial."
    )
