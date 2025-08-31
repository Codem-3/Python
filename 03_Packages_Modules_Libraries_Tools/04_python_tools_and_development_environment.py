"""
Python Development Tools and Environment Tutorial
===============================================

This tutorial covers:
1. Integrated Development Environments (IDEs)
2. Code editors and extensions
3. Linters and code quality tools
4. Code formatters
5. Debuggers and debugging tools
6. Version control with Git
7. Virtual environments and dependency management
8. Testing tools and frameworks
9. Documentation tools
10. Performance profiling tools
"""

import os
import sys
import subprocess
import json
from pathlib import Path

# 1. INTEGRATED DEVELOPMENT ENVIRONMENTS (IDES)
print("=" * 60)
print("1. INTEGRATED DEVELOPMENT ENVIRONMENTS (IDES)")
print("=" * 60)

print("""
Popular Python IDEs and Editors:

1. PyCharm (JetBrains):
   - Professional IDE with advanced features
   - Excellent debugging and refactoring tools
   - Integrated testing and version control
   - Available in Community (free) and Professional versions

2. Visual Studio Code:
   - Lightweight but powerful editor
   - Extensive extension ecosystem
   - Excellent Python support with extensions
   - Free and open-source

3. Jupyter Notebooks:
   - Interactive computing environment
   - Great for data science and exploration
   - Combines code, documentation, and output
   - Web-based interface

4. Spyder:
   - Scientific Python development environment
   - Integrated plotting and variable explorer
   - Similar to MATLAB interface
   - Free and open-source

5. IDLE:
   - Python's built-in IDE
   - Simple and lightweight
   - Good for beginners
   - Comes with Python installation
""")

# 2. CODE EDITORS AND EXTENSIONS
print("\n" + "=" * 60)
print("2. CODE EDITORS AND EXTENSIONS")
print("=" * 60)

print("""
Essential VS Code Extensions for Python:

1. Python (Microsoft):
   - Core Python language support
   - IntelliSense and autocomplete
   - Linting and debugging

2. Pylance:
   - Fast, feature-rich language server
   - Type checking and inference
   - Advanced IntelliSense

3. Python Docstring Generator:
   - Automatic docstring generation
   - Multiple docstring formats
   - Template customization

4. Python Indent:
   - Smart indentation
   - Auto-indent on paste
   - Bracket pair colorization

5. Python Test Explorer:
   - Test discovery and execution
   - Visual test results
   - Debug test support

6. GitLens:
   - Enhanced Git capabilities
   - Line-by-line blame
   - Git history visualization

7. Prettier:
   - Code formatting
   - Multiple language support
   - Configurable formatting rules

8. Bracket Pair Colorizer:
   - Visual bracket matching
   - Nested bracket highlighting
   - Improved code readability
""")

# 3. LINTERS AND CODE QUALITY TOOLS
print("\n" + "=" * 60)
print("3. LINTERS AND CODE QUALITY TOOLS")
print("=" * 60)

def create_linting_examples():
    """Create examples of linting configuration and usage"""
    
    # Flake8 configuration
    flake8_config = """[flake8]
max-line-length = 88
extend-ignore = E203, W503
exclude = .git,__pycache__,build,dist
per-file-ignores =
    __init__.py:F401
    tests/*:S101,S105,S106
"""
    
    with open("03_Packages_Modules_Libraries_Tools/Examples/.flake8", "w") as f:
        f.write(flake8_config)
    
    # Pylint configuration
    pylint_config = """[MASTER]
# Use multiple processes to speed up Pylint
jobs=0

[MESSAGES CONTROL]
# Disable specific warnings
disable=C0114,C0115,C0116,R0903,R0913,W0621

[REPORTS]
# Set the output format
output-format=text

# Include a brief explanation of each error
msg-template={path}:{line}: [{msg_id}({symbol}), {obj}] {msg}

[BASIC]
# Regular expression which should only match function or class names
good-names=i,j,k,ex,Run,_

[FORMAT]
# Maximum number of characters on a single line
max-line-length=88

# Maximum number of lines in a module
max-module-lines=1000

[SIMILARITIES]
# Minimum lines number of a similarity
min-similarity-lines=4

# Ignore imports when computing similarities
ignore-imports=yes
"""
    
    with open("03_Packages_Modules_Libraries_Tools/Examples/pylintrc", "w") as f:
        f.write(pylint_config)
    
    # Example code with linting issues
    code_with_issues = '''"""
Example code with various linting issues
"""

import os,sys  # Multiple imports on one line
import json
import time

# Unused import
import math

# Global variable (should be avoided)
GLOBAL_VAR = 42

def bad_function_name():  # Function name should be snake_case
    """Function with various issues"""
    x = 1
    y = 2
    z = x + y  # Unused variable
    
    # Too long line that exceeds the maximum line length and should be split into multiple lines
    very_long_string = "This is a very long string that exceeds the maximum line length and should be split into multiple lines"
    
    # Missing docstring
    def nested_function():
        pass
    
    return x

class BadClassName:  # Class name should be PascalCase
    """Class with issues"""
    
    def __init__(self):
        self.attr = 1
    
    def method(self):
        # Unused variable
        unused = "not used"
        return self.attr

# Unused function
def unused_function():
    pass

# Multiple statements on one line
a = 1; b = 2; c = 3

# Inconsistent indentation
def indentation_issue():
   return "wrong indentation"  # Should be 4 spaces
'''
    
    with open("03_Packages_Modules_Libraries_Tools/Examples/code_with_issues.py", "w") as f:
        f.write(code_with_issues)
    
    # Fixed version of the code
    fixed_code = '''"""
Example code with linting issues fixed
"""

import os
import sys
import json
import time

# Constants should be at module level
CONSTANT_VALUE = 42


def good_function_name():
    """Function with proper naming and structure."""
    x = 1
    y = 2
    result = x + y
    
    # Long line split properly
    very_long_string = (
        "This is a very long string that exceeds the maximum line length "
        "and should be split into multiple lines"
    )
    
    def nested_function():
        """Nested function with proper docstring."""
        return "nested"
    
    return result


class GoodClassName:
    """Class with proper naming and structure."""
    
    def __init__(self):
        """Initialize the class."""
        self.attr = 1
    
    def method(self):
        """Class method."""
        return self.attr


def main():
    """Main function."""
    obj = GoodClassName()
    return obj.method()


if __name__ == "__main__":
    main()
'''
    
    with open("03_Packages_Modules_Libraries_Tools/Examples/code_fixed.py", "w") as f:
        f.write(fixed_code)
    
    print("Created linting examples:")
    print("- .flake8 (Flake8 configuration)")
    print("- pylintrc (Pylint configuration)")
    print("- code_with_issues.py (Code with linting issues)")
    print("- code_fixed.py (Fixed version)")

create_linting_examples()

# 4. CODE FORMATTERS
print("\n" + "=" * 60)
print("4. CODE FORMATTERS")
print("=" * 60)

def create_formatting_examples():
    """Create examples of code formatting tools"""
    
    # Black configuration
    black_config = '''[tool.black]
line-length = 88
target-version = ['py37']
include = '\.pyi?$'
extend-exclude = '''
/(
  # directories
  \.eggs
  | \.git
  | \.hg
  | \.mypy_cache
  | \.tox
  | \.venv
  | build
  | dist
)/
'''
'''
    
    with open("03_Packages_Modules_Libraries_Tools/Examples/pyproject.toml", "w") as f:
        f.write(black_config)
    
    # isort configuration
    isort_config = '''[tool.isort]
profile = "black"
multi_line_output = 3
line_length = 88
known_first_party = ["my_package"]
known_third_party = ["requests", "numpy", "pandas"]
sections = ["FUTURE", "STDLIB", "THIRDPARTY", "FIRSTPARTY", "LOCALFOLDER"]
'''
    
    with open("03_Packages_Modules_Libraries_Tools/Examples/.isort.cfg", "w") as f:
        f.write(isort_config)
    
    # Example of unformatted code
    unformatted_code = '''"""
Unformatted code example
"""

import sys,os
import json
from datetime import datetime, timedelta
import numpy as np
import pandas as pd

def badly_formatted_function( x,y,z ):
    """This function is badly formatted"""
    result=x+y*z
    if result>10:
        print("Result is greater than 10")
    else:
        print("Result is less than or equal to 10")
    return result

class BadlyFormattedClass:
    def __init__(self,name,age):
        self.name=name
        self.age=age
    
    def get_info(self):
        return f"Name: {self.name}, Age: {self.age}"

# Badly formatted list
data=[1,2,3,4,5,6,7,8,9,10]

# Badly formatted dictionary
config={"name":"John","age":30,"city":"New York"}
'''
    
    with open("03_Packages_Modules_Libraries_Tools/Examples/unformatted_code.py", "w") as f:
        f.write(unformatted_code)
    
    print("Created formatting examples:")
    print("- pyproject.toml (Black configuration)")
    print("- .isort.cfg (isort configuration)")
    print("- unformatted_code.py (Code to be formatted)")

create_formatting_examples()

# 5. DEBUGGERS AND DEBUGGING TOOLS
print("\n" + "=" * 60)
print("5. DEBUGGERS AND DEBUGGING TOOLS")
print("=" * 60)

def create_debugging_examples():
    """Create examples of debugging tools and techniques"""
    
    # Example with debugging
    debugging_example = '''"""
Debugging Examples and Techniques
"""

import pdb
import logging
from typing import List, Dict, Any

# Configure logging
logging.basicConfig(
    level=logging.DEBUG,
    format='%(asctime)s - %(name)s - %(levelname)s - %(message)s'
)
logger = logging.getLogger(__name__)


def debug_with_print():
    """Debug using print statements (not recommended for production)"""
    print("=== Debug with Print ===")
    
    data = [1, 2, 3, 4, 5]
    print(f"Data: {data}")
    
    result = 0
    for i, value in enumerate(data):
        print(f"Processing index {i}, value {value}")
        result += value
        print(f"Running total: {result}")
    
    print(f"Final result: {result}")
    return result


def debug_with_logging():
    """Debug using logging (recommended approach)"""
    logger.info("=== Debug with Logging ===")
    
    data = [1, 2, 3, 4, 5]
    logger.debug(f"Input data: {data}")
    
    result = 0
    for i, value in enumerate(data):
        logger.debug(f"Processing index {i}, value {value}")
        result += value
        logger.debug(f"Running total: {result}")
    
    logger.info(f"Final result: {result}")
    return result


def debug_with_pdb():
    """Debug using Python debugger"""
    print("=== Debug with PDB ===")
    
    data = [1, 2, 3, 4, 5]
    result = 0
    
    # Set a breakpoint
    pdb.set_trace()  # Execution will pause here
    
    for i, value in enumerate(data):
        result += value
    
    return result


def debug_with_assertions():
    """Debug using assertions"""
    print("=== Debug with Assertions ===")
    
    def divide(a: float, b: float) -> float:
        """Divide a by b with assertions"""
        assert b != 0, "Cannot divide by zero"
        assert isinstance(a, (int, float)), "a must be a number"
        assert isinstance(b, (int, float)), "b must be a number"
        
        result = a / b
        assert isinstance(result, float), "Result should be a float"
        
        return result
    
    try:
        result = divide(10, 2)
        print(f"10 / 2 = {result}")
        
        # This will raise an assertion error
        # result = divide(10, 0)
        
    except AssertionError as e:
        print(f"Assertion error: {e}")


def debug_with_traceback():
    """Debug using traceback information"""
    import traceback
    
    print("=== Debug with Traceback ===")
    
    def problematic_function():
        """Function that might raise an exception"""
        try:
            # Simulate an error
            result = 1 / 0
        except Exception as e:
            print(f"Error occurred: {e}")
            print("Traceback:")
            traceback.print_exc()
    
    problematic_function()


def debug_with_decorator():
    """Debug using a custom decorator"""
    import functools
    import time
    
    def debug_decorator(func):
        """Decorator to debug function calls"""
        @functools.wraps(func)
        def wrapper(*args, **kwargs):
            logger.debug(f"Calling {func.__name__} with args={args}, kwargs={kwargs}")
            
            start_time = time.time()
            try:
                result = func(*args, **kwargs)
                logger.debug(f"{func.__name__} returned {result}")
                return result
            except Exception as e:
                logger.error(f"{func.__name__} raised {type(e).__name__}: {e}")
                raise
            finally:
                end_time = time.time()
                logger.debug(f"{func.__name__} took {end_time - start_time:.4f} seconds")
        
        return wrapper
    
    @debug_decorator
    def example_function(x, y):
        """Example function with debug decorator"""
        return x + y
    
    result = example_function(5, 3)
    print(f"Result: {result}")


def debug_with_context_manager():
    """Debug using context manager"""
    import contextlib
    
    @contextlib.contextmanager
    def debug_context(name):
        """Context manager for debugging"""
        logger.debug(f"Entering {name}")
        try:
            yield
        except Exception as e:
            logger.error(f"Error in {name}: {e}")
            raise
        finally:
            logger.debug(f"Exiting {name}")
    
    with debug_context("calculation"):
        result = 10 + 20
        print(f"Calculation result: {result}")


if __name__ == "__main__":
    # Run different debugging examples
    debug_with_print()
    debug_with_logging()
    # debug_with_pdb()  # Uncomment to test pdb
    debug_with_assertions()
    debug_with_traceback()
    debug_with_decorator()
    debug_with_context_manager()
'''
    
    with open("03_Packages_Modules_Libraries_Tools/Examples/debugging_examples.py", "w") as f:
        f.write(debugging_example)
    
    print("Created debugging examples:")
    print("- debugging_examples.py (Various debugging techniques)")

create_debugging_examples()

# 6. VERSION CONTROL WITH GIT
print("\n" + "=" * 60)
print("6. VERSION CONTROL WITH GIT")
print("=" * 60)

def create_git_examples():
    """Create Git configuration and examples"""
    
    # Git configuration
    git_config = """# Git configuration examples

# Basic Git setup
git config --global user.name "Your Name"
git config --global user.email "your.email@example.com"

# Common Git commands:
# git init                    # Initialize a new repository
# git clone <url>            # Clone a repository
# git add <file>             # Stage changes
# git commit -m "message"    # Commit changes
# git push                    # Push to remote
# git pull                    # Pull from remote
# git branch                  # List branches
# git checkout <branch>      # Switch branches
# git merge <branch>         # Merge branches
# git log                     # View commit history
"""
    
    with open("03_Packages_Modules_Libraries_Tools/Examples/git_commands.txt", "w") as f:
        f.write(git_config)
    
    # .gitignore for Python projects
    gitignore_content = """# Byte-compiled / optimized / DLL files
__pycache__/
*.py[cod]
*$py.class

# C extensions
*.so

# Distribution / packaging
.Python
build/
develop-eggs/
dist/
downloads/
eggs/
.eggs/
lib/
lib64/
parts/
sdist/
var/
wheels/
pip-wheel-metadata/
share/python-wheels/
*.egg-info/
.installed.cfg
*.egg
MANIFEST

# PyInstaller
*.manifest
*.spec

# Installer logs
pip-log.txt
pip-delete-this-directory.txt

# Unit test / coverage reports
htmlcov/
.tox/
.nox/
.coverage
.coverage.*
.cache
nosetests.xml
coverage.xml
*.cover
*.py,cover
.hypothesis/
.pytest_cache/

# Translations
*.mo
*.pot

# Django stuff:
*.log
local_settings.py
db.sqlite3
db.sqlite3-journal

# Flask stuff:
instance/
.webassets-cache

# Scrapy stuff:
.scrapy

# Sphinx documentation
docs/_build/

# PyBuilder
target/

# Jupyter Notebook
.ipynb_checkpoints

# IPython
profile_default/
ipython_config.py

# pyenv
.python-version

# pipenv
Pipfile.lock

# PEP 582
__pypackages__/

# Celery stuff
celerybeat-schedule
celerybeat.pid

# SageMath parsed files
*.sage.py

# Environments
.env
.venv
env/
venv/
ENV/
env.bak/
venv.bak/

# Spyder project settings
.spyderproject
.spyproject

# Rope project settings
.ropeproject

# mkdocs documentation
/site

# mypy
.mypy_cache/
.dmypy.json
dmypy.json

# Pyre type checker
.pyre/
"""
    
    with open("03_Packages_Modules_Libraries_Tools/Examples/.gitignore", "w") as f:
        f.write(gitignore_content)
    
    print("Created Git examples:")
    print("- git_commands.txt (Common Git commands)")
    print("- .gitignore (Python project gitignore)")

create_git_examples()

# 7. VIRTUAL ENVIRONMENTS AND DEPENDENCY MANAGEMENT
print("\n" + "=" * 60)
print("7. VIRTUAL ENVIRONMENTS AND DEPENDENCY MANAGEMENT")
print("=" * 60)

def create_environment_examples():
    """Create virtual environment and dependency management examples"""
    
    # Virtual environment setup script
    venv_script = '''#!/bin/bash
# Virtual Environment Setup Script

echo "Creating virtual environment..."
python -m venv venv

echo "Activating virtual environment..."
source venv/bin/activate  # On Windows: venv\\Scripts\\activate

echo "Upgrading pip..."
pip install --upgrade pip

echo "Installing dependencies..."
pip install -r requirements.txt

echo "Virtual environment setup complete!"
echo "To activate: source venv/bin/activate"
echo "To deactivate: deactivate"
'''
    
    with open("03_Packages_Modules_Libraries_Tools/Examples/setup_venv.sh", "w") as f:
        f.write(venv_script)
    
    # Windows batch script
    venv_batch = '''@echo off
REM Virtual Environment Setup Script for Windows

echo Creating virtual environment...
python -m venv venv

echo Activating virtual environment...
call venv\\Scripts\\activate

echo Upgrading pip...
python -m pip install --upgrade pip

echo Installing dependencies...
pip install -r requirements.txt

echo Virtual environment setup complete!
echo To activate: venv\\Scripts\\activate
echo To deactivate: deactivate
pause
'''
    
    with open("03_Packages_Modules_Libraries_Tools/Examples/setup_venv.bat", "w") as f:
        f.write(venv_batch)
    
    # Poetry configuration
    pyproject_poetry = '''[tool.poetry]
name = "my-python-project"
version = "0.1.0"
description = "A sample Python project"
authors = ["Your Name <your.email@example.com>"]
readme = "README.md"

[tool.poetry.dependencies]
python = "^3.8"
requests = "^2.28.0"
pandas = "^1.5.0"
numpy = "^1.24.0"

[tool.poetry.group.dev.dependencies]
pytest = "^7.0.0"
black = "^22.0.0"
flake8 = "^5.0.0"
mypy = "^0.991"

[build-system]
requires = ["poetry-core"]
build-backend = "poetry.core.masonry.api"
'''
    
    with open("03_Packages_Modules_Libraries_Tools/Examples/pyproject_poetry.toml", "w") as f:
        f.write(pyproject_poetry)
    
    print("Created environment examples:")
    print("- setup_venv.sh (Linux/Mac virtual environment setup)")
    print("- setup_venv.bat (Windows virtual environment setup)")
    print("- pyproject_poetry.toml (Poetry configuration)")

create_environment_examples()

# 8. TESTING TOOLS AND FRAMEWORKS
print("\n" + "=" * 60)
print("8. TESTING TOOLS AND FRAMEWORKS")
print("=" * 60)

def create_testing_examples():
    """Create testing framework examples"""
    
    # Pytest configuration
    pytest_config = '''[tool.pytest.ini_options]
minversion = "6.0"
addopts = "-ra -q --strict-markers --strict-config"
testpaths = [
    "tests",
]
markers = [
    "slow: marks tests as slow (deselect with '-m \"not slow\"')",
    "integration: marks tests as integration tests",
    "unit: marks tests as unit tests",
]
'''
    
    with open("03_Packages_Modules_Libraries_Tools/Examples/pytest.ini", "w") as f:
        f.write(pytest_config)
    
    # Coverage configuration
    coverage_config = '''[run]
source = .
omit = 
    */tests/*
    */venv/*
    setup.py

[report]
exclude_lines =
    pragma: no cover
    def __repr__
    raise AssertionError
    raise NotImplementedError
    if 0:
    if __name__ == .__main__.:
    class .*\\bProtocol\\):
    @(abc\\.)?abstractmethod
'''
    
    with open("03_Packages_Modules_Libraries_Tools/Examples/.coveragerc", "w") as f:
        f.write(coverage_config)
    
    print("Created testing examples:")
    print("- pytest.ini (Pytest configuration)")
    print("- .coveragerc (Coverage configuration)")

create_testing_examples()

# 9. DOCUMENTATION TOOLS
print("\n" + "=" * 60)
print("9. DOCUMENTATION TOOLS")
print("=" * 60)

def create_documentation_examples():
    """Create documentation tool examples"""
    
    # Sphinx configuration
    sphinx_conf = '''# Configuration file for the Sphinx documentation builder

project = 'My Python Project'
copyright = '2023, Your Name'
author = 'Your Name'

extensions = [
    'sphinx.ext.autodoc',
    'sphinx.ext.napoleon',
    'sphinx.ext.viewcode',
    'sphinx.ext.githubpages',
]

templates_path = ['_templates']
exclude_patterns = ['_build', 'Thumbs.db', '.DS_Store']

html_theme = 'sphinx_rtd_theme'
html_static_path = ['_static']

# Napoleon settings
napoleon_google_docstring = True
napoleon_numpy_docstring = True
napoleon_include_init_with_doc = False
napoleon_include_private_with_doc = False
napoleon_include_special_with_doc = True
napoleon_use_admonition_for_examples = False
napoleon_use_admonition_for_notes = False
napoleon_use_admonition_for_references = False
napoleon_use_ivar = False
napoleon_use_param = True
napoleon_use_rtype = True
napoleon_use_keyword = True
napoleon_custom_sections = None
'''
    
    with open("03_Packages_Modules_Libraries_Tools/Examples/conf.py", "w") as f:
        f.write(sphinx_conf)
    
    # MkDocs configuration
    mkdocs_config = '''site_name: My Python Project
site_description: A comprehensive Python project
site_author: Your Name
site_url: https://yourusername.github.io/my-python-project/

repo_name: yourusername/my-python-project
repo_url: https://github.com/yourusername/my-python-project
edit_uri: edit/main/docs/

theme:
  name: material
  language: en
  features:
    - navigation.tabs
    - navigation.sections
    - navigation.expand
    - search.suggest
    - search.highlight

plugins:
  - search
  - mkdocstrings:
      default_handler: python
      handlers:
        python:
          paths: [../src]
          options:
            show_source: true
            show_root_heading: true

nav:
  - Home: index.md
  - Installation: installation.md
  - Usage: usage.md
  - API Reference: api.md
  - Contributing: contributing.md

markdown_extensions:
  - admonition
  - codehilite
  - pymdownx.superfences
  - pymdownx.tabbed
  - toc:
      permalink: true
'''
    
    with open("03_Packages_Modules_Libraries_Tools/Examples/mkdocs.yml", "w") as f:
        f.write(mkdocs_config)
    
    print("Created documentation examples:")
    print("- conf.py (Sphinx configuration)")
    print("- mkdocs.yml (MkDocs configuration)")

create_documentation_examples()

# 10. PERFORMANCE PROFILING TOOLS
print("\n" + "=" * 60)
print("10. PERFORMANCE PROFILING TOOLS")
print("=" * 60)

def create_profiling_examples():
    """Create performance profiling examples"""
    
    # Profiling example
    profiling_example = '''"""
Performance Profiling Examples
"""

import time
import cProfile
import pstats
import io
from functools import wraps
from typing import Callable, Any


def timing_decorator(func: Callable) -> Callable:
    """Decorator to measure function execution time"""
    @wraps(func)
    def wrapper(*args, **kwargs) -> Any:
        start_time = time.time()
        result = func(*args, **kwargs)
        end_time = time.time()
        print(f"{func.__name__} took {end_time - start_time:.4f} seconds")
        return result
    return wrapper


def profile_function(func: Callable) -> Callable:
    """Decorator to profile function using cProfile"""
    @wraps(func)
    def wrapper(*args, **kwargs) -> Any:
        profiler = cProfile.Profile()
        profiler.enable()
        result = func(*args, **kwargs)
        profiler.disable()
        
        # Create stats object
        s = io.StringIO()
        ps = pstats.Stats(profiler, stream=s).sort_stats('cumulative')
        ps.print_stats(10)  # Print top 10 functions
        print(f"Profile for {func.__name__}:")
        print(s.getvalue())
        
        return result
    return wrapper


# Example functions to profile
@timing_decorator
def slow_function():
    """Function with poor performance"""
    result = 0
    for i in range(1000000):
        result += i
    return result


@timing_decorator
def fast_function():
    """Function with better performance"""
    return sum(range(1000000))


@profile_function
def function_with_profiling():
    """Function that will be profiled"""
    result = 0
    for i in range(100000):
        result += i ** 2
    return result


def memory_intensive_function():
    """Function that uses a lot of memory"""
    large_list = []
    for i in range(100000):
        large_list.append(i ** 2)
    return sum(large_list)


def optimized_memory_function():
    """Memory-optimized version"""
    return sum(i ** 2 for i in range(100000))


if __name__ == "__main__":
    print("=== Performance Comparison ===")
    
    # Compare slow vs fast function
    print("\\nSlow function:")
    slow_result = slow_function()
    
    print("\\nFast function:")
    fast_result = fast_function()
    
    print(f"\\nResults are equal: {slow_result == fast_result}")
    
    # Profile a function
    print("\\n=== Profiling Example ===")
    profiled_result = function_with_profiling()
    
    # Memory usage comparison
    print("\\n=== Memory Usage Comparison ===")
    
    import sys
    
    # Note: This is a simplified memory measurement
    # For more accurate memory profiling, use memory_profiler library
    
    print("Memory-intensive function:")
    start_memory = sys.getsizeof([])
    memory_intensive_function()
    print("Function completed")
    
    print("\\nOptimized function:")
    optimized_memory_function()
    print("Function completed")
'''
    
    with open("03_Packages_Modules_Libraries_Tools/Examples/profiling_examples.py", "w") as f:
        f.write(profiling_example)
    
    print("Created profiling examples:")
    print("- profiling_examples.py (Performance profiling techniques)")

create_profiling_examples()

# 11. BEST PRACTICES
print("\n" + "=" * 60)
print("11. BEST PRACTICES")
print("=" * 60)

print("""
Development Environment Best Practices:

1. IDE/Editor Setup:
   - Choose an IDE that fits your workflow
   - Install essential extensions and plugins
   - Configure keyboard shortcuts and preferences
   - Set up code templates and snippets

2. Code Quality:
   - Use linters (flake8, pylint) consistently
   - Format code with tools like Black and isort
   - Set up pre-commit hooks for automatic checks
   - Follow PEP 8 style guidelines

3. Version Control:
   - Use Git for all projects
   - Write meaningful commit messages
   - Create feature branches for new work
   - Use .gitignore to exclude unnecessary files
   - Review code before merging

4. Virtual Environments:
   - Use virtual environments for all projects
   - Keep requirements.txt updated
   - Use tools like Poetry for dependency management
   - Document environment setup

5. Testing:
   - Write tests for all new code
   - Aim for high test coverage
   - Use appropriate testing frameworks
   - Run tests before committing

6. Documentation:
   - Write clear docstrings for all functions
   - Maintain up-to-date README files
   - Use documentation generators
   - Include usage examples

7. Performance:
   - Profile code to identify bottlenecks
   - Use appropriate data structures
   - Optimize critical paths
   - Monitor memory usage

8. Security:
   - Keep dependencies updated
   - Use secure coding practices
   - Validate all inputs
   - Follow security guidelines

9. Collaboration:
   - Use consistent coding standards
   - Review each other's code
   - Communicate effectively
   - Share knowledge and best practices

10. Continuous Integration:
    - Set up automated testing
    - Use CI/CD pipelines
    - Automate code quality checks
    - Deploy automatically when tests pass
""")

# 12. EXERCISES
print("\n" + "=" * 60)
print("12. EXERCISES")
print("=" * 60)

print("""
Exercises to practice development tools:

1. IDE/Editor Setup:
   - Set up VS Code with Python extensions
   - Configure linting and formatting
   - Create custom snippets
   - Set up debugging configuration

2. Code Quality:
   - Run linters on your code
   - Fix all linting issues
   - Set up pre-commit hooks
   - Format code with Black and isort

3. Version Control:
   - Initialize a Git repository
   - Make commits with good messages
   - Create and merge branches
   - Set up remote repository

4. Virtual Environments:
   - Create virtual environments for projects
   - Install and manage dependencies
   - Use requirements files
   - Document environment setup

5. Testing:
   - Write unit tests for functions
   - Use pytest for testing
   - Measure test coverage
   - Set up automated testing

6. Documentation:
   - Write comprehensive docstrings
   - Create README files
   - Set up documentation generation
   - Include usage examples

7. Performance:
   - Profile your code
   - Identify and fix bottlenecks
   - Optimize slow functions
   - Monitor memory usage

8. Debugging:
   - Use debugging tools effectively
   - Set breakpoints and inspect variables
   - Use logging for debugging
   - Handle exceptions properly

9. Project Structure:
   - Organize code into packages
   - Use proper import statements
   - Create setup files
   - Structure projects professionally

10. Automation:
    - Set up CI/CD pipelines
    - Automate testing and deployment
    - Use scripts for common tasks
    - Automate code quality checks
""")

if __name__ == "__main__":
    print("\n" + "=" * 60)
    print("DEVELOPMENT TOOLS TUTORIAL COMPLETED!")
    print("=" * 60)
    print("Check the Examples folder for configuration files and examples created during this tutorial.") 