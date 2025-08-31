"""
Python Libraries and Frameworks Tutorial
=======================================

This tutorial covers:
1. What are libraries and frameworks
2. Popular Python libraries by domain
3. Web development frameworks
4. Data science libraries
5. Machine learning libraries
6. GUI frameworks
7. Testing frameworks
8. Best practices for using libraries
"""

import sys
import os
import json
import time
from pathlib import Path
from typing import List, Dict, Any

# 1. WHAT ARE LIBRARIES AND FRAMEWORKS?
print("=" * 60)
print("1. WHAT ARE LIBRARIES AND FRAMEWOWS?")
print("=" * 60)

"""
Libraries: Collections of pre-written code that you can import and use
Frameworks: More comprehensive structures that provide a foundation for applications

Key differences:
- Libraries: You call the library code
- Frameworks: The framework calls your code (inversion of control)
"""

# 2. POPULAR PYTHON LIBRARIES BY DOMAIN
print("\n" + "=" * 60)
print("2. POPULAR PYTHON LIBRARIES BY DOMAIN")
print("=" * 60)

print("""
Python Libraries by Domain:

1. Data Science & Analytics:
   - NumPy: Numerical computing
   - Pandas: Data manipulation and analysis
   - Matplotlib: Plotting and visualization
   - Seaborn: Statistical data visualization
   - SciPy: Scientific computing

2. Machine Learning & AI:
   - Scikit-learn: Machine learning
   - TensorFlow: Deep learning
   - PyTorch: Deep learning
   - Keras: Neural networks
   - OpenCV: Computer vision

3. Web Development:
   - Flask: Lightweight web framework
   - Django: Full-featured web framework
   - FastAPI: Modern API framework
   - Requests: HTTP library
   - Beautiful Soup: Web scraping

4. GUI Development:
   - Tkinter: Built-in GUI toolkit
   - PyQt: Cross-platform GUI
   - Kivy: Mobile and multi-touch
   - wxPython: Native GUI

5. Testing:
   - pytest: Testing framework
   - unittest: Built-in testing
   - nose2: Test discovery
   - coverage: Code coverage

6. Utilities:
   - Click: Command-line interfaces
   - PyYAML: YAML parser
   - Pillow: Image processing
   - python-dotenv: Environment variables
""")

# 3. WEB DEVELOPMENT FRAMEWORKS
print("\n" + "=" * 60)
print("3. WEB DEVELOPMENT FRAMEWORKS")
print("=" * 60)

def create_web_framework_examples():
    """Create examples of web framework usage"""
    
    # Flask example
    flask_example = '''"""
Flask Web Framework Example
"""

from flask import Flask, request, jsonify, render_template_string

app = Flask(__name__)

# Simple route
@app.route('/')
def home():
    return '<h1>Welcome to Flask!</h1>'

# Route with parameters
@app.route('/user/<name>')
def user(name):
    return f'<h1>Hello, {name}!</h1>'

# API endpoint
@app.route('/api/data', methods=['GET', 'POST'])
def api_data():
    if request.method == 'POST':
        data = request.get_json()
        return jsonify({'message': 'Data received', 'data': data})
    else:
        return jsonify({'message': 'GET request', 'data': [1, 2, 3, 4, 5]})

# Template example
@app.route('/template')
def template_example():
    template = '''
    <!DOCTYPE html>
    <html>
    <head><title>Flask Template</title></head>
    <body>
        <h1>{{ title }}</h1>
        <p>{{ message }}</p>
        <ul>
        {% for item in items %}
            <li>{{ item }}</li>
        {% endfor %}
        </ul>
    </body>
    </html>
    '''
    return render_template_string(template, 
                                title="Flask Template", 
                                message="This is a template example",
                                items=['Apple', 'Banana', 'Cherry'])

if __name__ == '__main__':
    app.run(debug=True, port=5000)
'''
    
    with open("03_Packages_Modules_Libraries_Tools/Examples/flask_example.py", "w") as f:
        f.write(flask_example)
    
    # FastAPI example
    fastapi_example = '''"""
FastAPI Web Framework Example
"""

from fastapi import FastAPI, HTTPException
from pydantic import BaseModel
from typing import List, Optional

app = FastAPI(title="FastAPI Example", version="1.0.0")

# Data model
class Item(BaseModel):
    id: Optional[int] = None
    name: str
    description: Optional[str] = None
    price: float
    is_offer: bool = False

# Sample data
items_db = [
    Item(id=1, name="Laptop", description="High-performance laptop", price=999.99),
    Item(id=2, name="Mouse", description="Wireless mouse", price=29.99),
]

@app.get("/")
def read_root():
    return {"message": "Welcome to FastAPI!"}

@app.get("/items/", response_model=List[Item])
def read_items():
    return items_db

@app.get("/items/{item_id}", response_model=Item)
def read_item(item_id: int):
    for item in items_db:
        if item.id == item_id:
            return item
    raise HTTPException(status_code=404, detail="Item not found")

@app.post("/items/", response_model=Item)
def create_item(item: Item):
    item.id = len(items_db) + 1
    items_db.append(item)
    return item

@app.put("/items/{item_id}", response_model=Item)
def update_item(item_id: int, item: Item):
    for i, existing_item in enumerate(items_db):
        if existing_item.id == item_id:
            item.id = item_id
            items_db[i] = item
            return item
    raise HTTPException(status_code=404, detail="Item not found")

if __name__ == "__main__":
    import uvicorn
    uvicorn.run(app, host="0.0.0.0", port=8000)
'''
    
    with open("03_Packages_Modules_Libraries_Tools/Examples/fastapi_example.py", "w") as f:
        f.write(fastapi_example)
    
    print("Created web framework examples:")
    print("- flask_example.py")
    print("- fastapi_example.py")

create_web_framework_examples()

# 4. DATA SCIENCE LIBRARIES
print("\n" + "=" * 60)
print("4. DATA SCIENCE LIBRARIES")
print("=" * 60)

def create_data_science_examples():
    """Create examples of data science library usage"""
    
    # NumPy example
    numpy_example = '''"""
NumPy Library Example
"""

import numpy as np

# Creating arrays
print("=== NumPy Arrays ===")
arr1 = np.array([1, 2, 3, 4, 5])
arr2 = np.array([[1, 2, 3], [4, 5, 6]])
arr3 = np.zeros((3, 3))
arr4 = np.ones((2, 4))
arr5 = np.arange(0, 10, 2)  # [0, 2, 4, 6, 8]
arr6 = np.linspace(0, 1, 5)  # [0, 0.25, 0.5, 0.75, 1]

print(f"1D Array: {arr1}")
print(f"2D Array:\\n{arr2}")
print(f"Zeros Array:\\n{arr3}")
print(f"Ones Array:\\n{arr4}")
print(f"Range Array: {arr5}")
print(f"Linear Space: {arr6}")

# Array operations
print("\\n=== Array Operations ===")
a = np.array([1, 2, 3, 4])
b = np.array([5, 6, 7, 8])

print(f"Addition: {a + b}")
print(f"Multiplication: {a * b}")
print(f"Square: {a ** 2}")
print(f"Square root: {np.sqrt(a)}")
print(f"Sum: {np.sum(a)}")
print(f"Mean: {np.mean(a)}")
print(f"Standard deviation: {np.std(a)}")

# Matrix operations
print("\\n=== Matrix Operations ===")
matrix1 = np.array([[1, 2], [3, 4]])
matrix2 = np.array([[5, 6], [7, 8]])

print(f"Matrix 1:\\n{matrix1}")
print(f"Matrix 2:\\n{matrix2}")
print(f"Matrix multiplication:\\n{np.dot(matrix1, matrix2)}")
print(f"Transpose:\\n{matrix1.T}")
print(f"Determinant: {np.linalg.det(matrix1)}")
print(f"Inverse:\\n{np.linalg.inv(matrix1)}")

# Random numbers
print("\\n=== Random Numbers ===")
random_array = np.random.rand(3, 3)
normal_array = np.random.normal(0, 1, (3, 3))
integers = np.random.randint(1, 100, 10)

print(f"Random array:\\n{random_array}")
print(f"Normal distribution:\\n{normal_array}")
print(f"Random integers: {integers}")

# Broadcasting
print("\\n=== Broadcasting ===")
arr = np.array([[1, 2, 3], [4, 5, 6]])
scalar = 2

print(f"Original array:\\n{arr}")
print(f"Scalar: {scalar}")
print(f"Broadcasted multiplication:\\n{arr * scalar}")
'''
    
    with open("03_Packages_Modules_Libraries_Tools/Examples/numpy_example.py", "w") as f:
        f.write(numpy_example)
    
    # Pandas example
    pandas_example = '''"""
Pandas Library Example
"""

import pandas as pd
import numpy as np

# Creating DataFrames
print("=== Creating DataFrames ===")

# From dictionary
data_dict = {
    'Name': ['Alice', 'Bob', 'Charlie', 'Diana'],
    'Age': [25, 30, 35, 28],
    'City': ['New York', 'Los Angeles', 'Chicago', 'Boston'],
    'Salary': [50000, 60000, 70000, 55000]
}
df1 = pd.DataFrame(data_dict)
print("DataFrame from dictionary:")
print(df1)

# From list of lists
data_list = [
    ['Alice', 25, 'New York', 50000],
    ['Bob', 30, 'Los Angeles', 60000],
    ['Charlie', 35, 'Chicago', 70000],
    ['Diana', 28, 'Boston', 55000]
]
columns = ['Name', 'Age', 'City', 'Salary']
df2 = pd.DataFrame(data_list, columns=columns)
print("\\nDataFrame from list:")
print(df2)

# Reading data
print("\\n=== Reading Data ===")
# Create sample CSV file
sample_data = '''Name,Age,City,Salary
Alice,25,New York,50000
Bob,30,Los Angeles,60000
Charlie,35,Chicago,70000
Diana,28,Boston,55000
Eve,32,Seattle,65000'''

with open('sample_data.csv', 'w') as f:
    f.write(sample_data)

# Read CSV
df_csv = pd.read_csv('sample_data.csv')
print("DataFrame from CSV:")
print(df_csv)

# Basic operations
print("\\n=== Basic Operations ===")
print(f"Shape: {df_csv.shape}")
print(f"Columns: {df_csv.columns.tolist()}")
print(f"Data types:\\n{df_csv.dtypes}")
print(f"\\nFirst 3 rows:")
print(df_csv.head(3))
print(f"\\nLast 2 rows:")
print(df_csv.tail(2))

# Data selection
print("\\n=== Data Selection ===")
print("Select specific columns:")
print(df_csv[['Name', 'Age']])

print("\\nSelect rows by condition:")
print(df_csv[df_csv['Age'] > 30])

print("\\nSelect specific row and column:")
print(df_csv.loc[1, 'Name'])

# Data manipulation
print("\\n=== Data Manipulation ===")
# Add new column
df_csv['Bonus'] = df_csv['Salary'] * 0.1
print("Added bonus column:")
print(df_csv)

# Group by operations
print("\\n=== Group By Operations ===")
city_stats = df_csv.groupby('City').agg({
    'Age': ['mean', 'count'],
    'Salary': ['mean', 'sum']
}).round(2)
print("Statistics by city:")
print(city_stats)

# Missing data handling
print("\\n=== Missing Data Handling ===")
df_with_missing = df_csv.copy()
df_with_missing.loc[2, 'Age'] = np.nan
df_with_missing.loc[1, 'Salary'] = np.nan

print("DataFrame with missing values:")
print(df_with_missing)

print("\\nFill missing values:")
df_filled = df_with_missing.fillna({
    'Age': df_with_missing['Age'].mean(),
    'Salary': df_with_missing['Salary'].median()
})
print(df_filled)

# Data visualization (basic)
print("\\n=== Basic Statistics ===")
print("Descriptive statistics:")
print(df_csv.describe())

print("\\nCorrelation matrix:")
print(df_csv[['Age', 'Salary']].corr())
'''
    
    with open("03_Packages_Modules_Libraries_Tools/Examples/pandas_example.py", "w") as f:
        f.write(pandas_example)
    
    print("Created data science examples:")
    print("- numpy_example.py")
    print("- pandas_example.py")

create_data_science_examples()

# 5. MACHINE LEARNING LIBRARIES
print("\n" + "=" * 60)
print("5. MACHINE LEARNING LIBRARIES")
print("=" * 60)

def create_ml_examples():
    """Create examples of machine learning library usage"""
    
    # Scikit-learn example
    sklearn_example = '''"""
Scikit-learn Machine Learning Example
"""

import numpy as np
import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import StandardScaler
from sklearn.linear_model import LinearRegression, LogisticRegression
from sklearn.ensemble import RandomForestClassifier
from sklearn.metrics import accuracy_score, classification_report, mean_squared_error
from sklearn.datasets import make_classification, make_regression

# 1. Classification Example
print("=== Classification Example ===")

# Generate sample data
X_class, y_class = make_classification(n_samples=1000, n_features=20, 
                                      n_informative=15, n_redundant=5, 
                                      random_state=42)

# Split data
X_train, X_test, y_train, y_test = train_test_split(
    X_class, y_class, test_size=0.2, random_state=42
)

# Scale features
scaler = StandardScaler()
X_train_scaled = scaler.fit_transform(X_train)
X_test_scaled = scaler.transform(X_test)

# Train Logistic Regression
lr_model = LogisticRegression(random_state=42)
lr_model.fit(X_train_scaled, y_train)

# Make predictions
lr_pred = lr_model.predict(X_test_scaled)
lr_accuracy = accuracy_score(y_test, lr_pred)

print(f"Logistic Regression Accuracy: {lr_accuracy:.4f}")
print("\\nClassification Report:")
print(classification_report(y_test, lr_pred))

# Train Random Forest
rf_model = RandomForestClassifier(n_estimators=100, random_state=42)
rf_model.fit(X_train, y_train)

# Make predictions
rf_pred = rf_model.predict(X_test)
rf_accuracy = accuracy_score(y_test, rf_pred)

print(f"\\nRandom Forest Accuracy: {rf_accuracy:.4f}")
print("\\nClassification Report:")
print(classification_report(y_test, rf_pred))

# Feature importance
feature_importance = rf_model.feature_importances_
print(f"\\nTop 5 Feature Importances:")
top_features = np.argsort(feature_importance)[-5:]
for i, feature_idx in enumerate(reversed(top_features)):
    print(f"Feature {feature_idx}: {feature_importance[feature_idx]:.4f}")

# 2. Regression Example
print("\\n=== Regression Example ===")

# Generate sample data
X_reg, y_reg = make_regression(n_samples=1000, n_features=10, 
                              n_informative=8, noise=0.1, random_state=42)

# Split data
X_train_reg, X_test_reg, y_train_reg, y_test_reg = train_test_split(
    X_reg, y_reg, test_size=0.2, random_state=42
)

# Scale features
scaler_reg = StandardScaler()
X_train_reg_scaled = scaler_reg.fit_transform(X_train_reg)
X_test_reg_scaled = scaler_reg.transform(X_test_reg)

# Train Linear Regression
linear_model = LinearRegression()
linear_model.fit(X_train_reg_scaled, y_train_reg)

# Make predictions
linear_pred = linear_model.predict(X_test_reg_scaled)
linear_mse = mean_squared_error(y_test_reg, linear_pred)

print(f"Linear Regression MSE: {linear_mse:.4f}")
print(f"Linear Regression R² Score: {linear_model.score(X_test_reg_scaled, y_test_reg):.4f}")

# 3. Cross-validation Example
print("\\n=== Cross-validation Example ===")

from sklearn.model_selection import cross_val_score

# Perform cross-validation
cv_scores = cross_val_score(rf_model, X_class, y_class, cv=5)
print(f"Cross-validation scores: {cv_scores}")
print(f"Mean CV score: {cv_scores.mean():.4f} (+/- {cv_scores.std() * 2:.4f})")

# 4. Model Persistence
print("\\n=== Model Persistence ===")

import pickle

# Save model
with open('random_forest_model.pkl', 'wb') as f:
    pickle.dump(rf_model, f)

# Load model
with open('random_forest_model.pkl', 'rb') as f:
    loaded_model = pickle.load(f)

# Test loaded model
loaded_pred = loaded_model.predict(X_test)
loaded_accuracy = accuracy_score(y_test, loaded_pred)
print(f"Loaded model accuracy: {loaded_accuracy:.4f}")

# 5. Pipeline Example
print("\\n=== Pipeline Example ===")

from sklearn.pipeline import Pipeline

# Create pipeline
pipeline = Pipeline([
    ('scaler', StandardScaler()),
    ('classifier', RandomForestClassifier(n_estimators=100, random_state=42))
])

# Train pipeline
pipeline.fit(X_train, y_train)

# Make predictions
pipeline_pred = pipeline.predict(X_test)
pipeline_accuracy = accuracy_score(y_test, pipeline_pred)

print(f"Pipeline Accuracy: {pipeline_accuracy:.4f}")

# Save pipeline
with open('ml_pipeline.pkl', 'wb') as f:
    pickle.dump(pipeline, f)
'''
    
    with open("03_Packages_Modules_Libraries_Tools/Examples/sklearn_example.py", "w") as f:
        f.write(sklearn_example)
    
    print("Created machine learning example:")
    print("- sklearn_example.py")

create_ml_examples()

# 6. GUI FRAMEWORKS
print("\n" + "=" * 60)
print("6. GUI FRAMEWORKS")
print("=" * 60)

def create_gui_examples():
    """Create examples of GUI framework usage"""
    
    # Tkinter example
    tkinter_example = '''"""
Tkinter GUI Framework Example
"""

import tkinter as tk
from tkinter import ttk, messagebox, filedialog
import json

class SimpleCalculator:
    def __init__(self, root):
        self.root = root
        self.root.title("Simple Calculator")
        self.root.geometry("300x400")
        
        # Variables
        self.current_number = tk.StringVar()
        self.result_var = tk.StringVar()
        self.result_var.set("0")
        
        self.create_widgets()
    
    def create_widgets(self):
        # Display
        display_frame = ttk.Frame(self.root)
        display_frame.pack(pady=10, padx=10, fill="x")
        
        ttk.Label(display_frame, text="Calculator", font=("Arial", 16)).pack()
        
        # Current number display
        ttk.Entry(display_frame, textvariable=self.current_number, 
                 font=("Arial", 14), justify="right").pack(fill="x", pady=5)
        
        # Result display
        ttk.Label(display_frame, textvariable=self.result_var, 
                 font=("Arial", 18), background="lightgray").pack(fill="x", pady=5)
        
        # Buttons frame
        buttons_frame = ttk.Frame(self.root)
        buttons_frame.pack(pady=10, padx=10)
        
        # Number buttons
        numbers = [
            ['7', '8', '9', '/'],
            ['4', '5', '6', '*'],
            ['1', '2', '3', '-'],
            ['0', '.', '=', '+']
        ]
        
        for i, row in enumerate(numbers):
            for j, num in enumerate(row):
                btn = ttk.Button(buttons_frame, text=num, 
                               command=lambda n=num: self.button_click(n))
                btn.grid(row=i, column=j, padx=2, pady=2, sticky="nsew")
        
        # Clear button
        ttk.Button(buttons_frame, text="C", 
                  command=self.clear).grid(row=4, column=0, columnspan=2, 
                                          padx=2, pady=2, sticky="nsew")
        
        # Configure grid weights
        for i in range(5):
            buttons_frame.grid_rowconfigure(i, weight=1)
        for i in range(4):
            buttons_frame.grid_columnconfigure(i, weight=1)
    
    def button_click(self, value):
        if value == '=':
            try:
                result = eval(self.current_number.get())
                self.result_var.set(str(result))
                self.current_number.set(str(result))
            except:
                messagebox.showerror("Error", "Invalid expression")
                self.clear()
        else:
            current = self.current_number.get()
            self.current_number.set(current + value)
    
    def clear(self):
        self.current_number.set("")
        self.result_var.set("0")

class FileManager:
    def __init__(self, root):
        self.root = root
        self.root.title("File Manager")
        self.root.geometry("400x300")
        
        self.create_widgets()
    
    def create_widgets(self):
        # Menu
        menubar = tk.Menu(self.root)
        self.root.config(menu=menubar)
        
        file_menu = tk.Menu(menubar, tearoff=0)
        menubar.add_cascade(label="File", menu=file_menu)
        file_menu.add_command(label="Open", command=self.open_file)
        file_menu.add_command(label="Save", command=self.save_file)
        file_menu.add_separator()
        file_menu.add_command(label="Exit", command=self.root.quit)
        
        # Main frame
        main_frame = ttk.Frame(self.root)
        main_frame.pack(fill="both", expand=True, padx=10, pady=10)
        
        # Text area
        self.text_area = tk.Text(main_frame, wrap="word")
        scrollbar = ttk.Scrollbar(main_frame, orient="vertical", command=self.text_area.yview)
        self.text_area.configure(yscrollcommand=scrollbar.set)
        
        self.text_area.pack(side="left", fill="both", expand=True)
        scrollbar.pack(side="right", fill="y")
        
        # Status bar
        self.status_var = tk.StringVar()
        self.status_var.set("Ready")
        status_bar = ttk.Label(self.root, textvariable=self.status_var, relief="sunken")
        status_bar.pack(side="bottom", fill="x")
    
    def open_file(self):
        file_path = filedialog.askopenfilename(
            filetypes=[("Text files", "*.txt"), ("All files", "*.*")]
        )
        if file_path:
            try:
                with open(file_path, 'r') as file:
                    content = file.read()
                    self.text_area.delete(1.0, tk.END)
                    self.text_area.insert(1.0, content)
                self.status_var.set(f"Opened: {file_path}")
            except Exception as e:
                messagebox.showerror("Error", f"Could not open file: {e}")
    
    def save_file(self):
        file_path = filedialog.asksaveasfilename(
            defaultextension=".txt",
            filetypes=[("Text files", "*.txt"), ("All files", "*.*")]
        )
        if file_path:
            try:
                content = self.text_area.get(1.0, tk.END)
                with open(file_path, 'w') as file:
                    file.write(content)
                self.status_var.set(f"Saved: {file_path}")
            except Exception as e:
                messagebox.showerror("Error", f"Could not save file: {e}")

def main():
    root = tk.Tk()
    
    # Create notebook for multiple tabs
    notebook = ttk.Notebook(root)
    notebook.pack(fill="both", expand=True)
    
    # Calculator tab
    calc_frame = ttk.Frame(notebook)
    notebook.add(calc_frame, text="Calculator")
    calculator = SimpleCalculator(calc_frame)
    
    # File Manager tab
    file_frame = ttk.Frame(notebook)
    notebook.add(file_frame, text="File Manager")
    file_manager = FileManager(file_frame)
    
    root.mainloop()

if __name__ == "__main__":
    main()
'''
    
    with open("03_Packages_Modules_Libraries_Tools/Examples/tkinter_example.py", "w") as f:
        f.write(tkinter_example)
    
    print("Created GUI example:")
    print("- tkinter_example.py")

create_gui_examples()

# 7. TESTING FRAMEWORKS
print("\n" + "=" * 60)
print("7. TESTING FRAMEWORKS")
print("=" * 60)

def create_testing_examples():
    """Create examples of testing framework usage"""
    
    # Pytest example
    pytest_example = '''"""
Pytest Testing Framework Example
"""

import pytest
import math
from typing import List, Dict, Any

# Functions to test
def add(a: float, b: float) -> float:
    """Add two numbers"""
    return a + b

def multiply(a: float, b: float) -> float:
    """Multiply two numbers"""
    return a * b

def divide(a: float, b: float) -> float:
    """Divide a by b"""
    if b == 0:
        raise ValueError("Cannot divide by zero")
    return a / b

def is_prime(n: int) -> bool:
    """Check if a number is prime"""
    if n < 2:
        return False
    for i in range(2, int(math.sqrt(n)) + 1):
        if n % i == 0:
            return False
    return True

def reverse_string(s: str) -> str:
    """Reverse a string"""
    return s[::-1]

def count_vowels(s: str) -> int:
    """Count vowels in a string"""
    vowels = 'aeiouAEIOU'
    return sum(1 for char in s if char in vowels)

def find_max(numbers: List[float]) -> float:
    """Find maximum value in a list"""
    if not numbers:
        raise ValueError("Cannot find maximum of empty list")
    return max(numbers)

def sort_list(numbers: List[float]) -> List[float]:
    """Sort a list of numbers"""
    return sorted(numbers)

# Test classes
class TestMathOperations:
    """Test mathematical operations"""
    
    def test_add(self):
        """Test addition function"""
        assert add(2, 3) == 5
        assert add(-1, 1) == 0
        assert add(0, 0) == 0
        assert add(3.5, 2.5) == 6.0
    
    def test_multiply(self):
        """Test multiplication function"""
        assert multiply(2, 3) == 6
        assert multiply(-2, 3) == -6
        assert multiply(0, 5) == 0
        assert multiply(2.5, 2) == 5.0
    
    def test_divide(self):
        """Test division function"""
        assert divide(6, 2) == 3
        assert divide(5, 2) == 2.5
        assert divide(0, 5) == 0
    
    def test_divide_by_zero(self):
        """Test division by zero raises error"""
        with pytest.raises(ValueError, match="Cannot divide by zero"):
            divide(5, 0)

class TestStringOperations:
    """Test string operations"""
    
    def test_reverse_string(self):
        """Test string reversal"""
        assert reverse_string("hello") == "olleh"
        assert reverse_string("") == ""
        assert reverse_string("a") == "a"
        assert reverse_string("12345") == "54321"
    
    def test_count_vowels(self):
        """Test vowel counting"""
        assert count_vowels("hello") == 2
        assert count_vowels("world") == 1
        assert count_vowels("aeiou") == 5
        assert count_vowels("bcdfg") == 0
        assert count_vowels("") == 0

class TestListOperations:
    """Test list operations"""
    
    def test_find_max(self):
        """Test finding maximum value"""
        assert find_max([1, 2, 3, 4, 5]) == 5
        assert find_max([-1, -2, -3]) == -1
        assert find_max([0]) == 0
        assert find_max([3.14, 2.71, 1.41]) == 3.14
    
    def test_find_max_empty_list(self):
        """Test finding maximum of empty list raises error"""
        with pytest.raises(ValueError, match="Cannot find maximum of empty list"):
            find_max([])
    
    def test_sort_list(self):
        """Test list sorting"""
        assert sort_list([3, 1, 4, 1, 5]) == [1, 1, 3, 4, 5]
        assert sort_list([5, 4, 3, 2, 1]) == [1, 2, 3, 4, 5]
        assert sort_list([]) == []
        assert sort_list([1]) == [1]

class TestPrimeNumbers:
    """Test prime number detection"""
    
    @pytest.mark.parametrize("number,expected", [
        (2, True),
        (3, True),
        (4, False),
        (5, True),
        (6, False),
        (7, True),
        (8, False),
        (9, False),
        (10, False),
        (11, True),
        (1, False),
        (0, False),
        (-1, False),
    ])
    def test_is_prime(self, number, expected):
        """Test prime number detection with various inputs"""
        assert is_prime(number) == expected

# Fixtures
@pytest.fixture
def sample_numbers():
    """Fixture providing sample numbers"""
    return [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]

@pytest.fixture
def sample_strings():
    """Fixture providing sample strings"""
    return ["hello", "world", "python", "testing", ""]

def test_with_fixtures(sample_numbers, sample_strings):
    """Test using fixtures"""
    assert len(sample_numbers) == 10
    assert len(sample_strings) == 5
    assert find_max(sample_numbers) == 10
    assert reverse_string(sample_strings[0]) == "olleh"

# Performance testing
@pytest.mark.slow
def test_performance():
    """Test performance of prime detection"""
    import time
    start_time = time.time()
    
    # Test prime detection for first 1000 numbers
    primes = [n for n in range(2, 1000) if is_prime(n)]
    
    end_time = time.time()
    execution_time = end_time - start_time
    
    assert len(primes) > 0
    assert execution_time < 1.0  # Should complete within 1 second

# Mock testing example
def test_with_mock(monkeypatch):
    """Test with mocked function"""
    def mock_math_sqrt(x):
        return 2.0  # Always return 2.0
    
    monkeypatch.setattr(math, 'sqrt', mock_math_sqrt)
    
    # Now is_prime will use our mocked sqrt function
    # This is useful for testing edge cases
    assert math.sqrt(16) == 2.0

# Configuration
def pytest_configure(config):
    """Configure pytest"""
    config.addinivalue_line(
        "markers", "slow: marks tests as slow (deselect with '-m \"not slow\"')"
    )

# Test discovery
if __name__ == "__main__":
    pytest.main([__file__, "-v"])
'''
    
    with open("03_Packages_Modules_Libraries_Tools/Examples/pytest_example.py", "w") as f:
        f.write(pytest_example)
    
    print("Created testing example:")
    print("- pytest_example.py")

create_testing_examples()

# 8. BEST PRACTICES FOR USING LIBRARIES
print("\n" + "=" * 60)
print("8. BEST PRACTICES FOR USING LIBRARIES")
print("=" * 60)

print("""
Best Practices for Using Python Libraries:

1. Library Selection:
   - Choose well-maintained libraries with active development
   - Check documentation quality and community support
   - Consider license compatibility
   - Evaluate performance and memory usage

2. Version Management:
   - Pin specific versions in requirements.txt
   - Use virtual environments for isolation
   - Test with different versions before upgrading
   - Keep dependencies up to date for security

3. Import Organization:
   - Group imports by type (standard, third-party, local)
   - Use specific imports when possible
   - Avoid 'from module import *'
   - Use aliases for long module names

4. Error Handling:
   - Handle library-specific exceptions
   - Provide fallback behavior when possible
   - Log errors appropriately
   - Test error conditions

5. Performance:
   - Profile code to identify bottlenecks
   - Use appropriate data structures
   - Consider lazy loading for heavy libraries
   - Cache expensive operations

6. Security:
   - Validate input data
   - Use parameterized queries for databases
   - Sanitize user input
   - Keep libraries updated

7. Testing:
   - Mock external library calls
   - Test with different library versions
   - Use dependency injection for testability
   - Test error conditions

8. Documentation:
   - Document library dependencies
   - Include usage examples
   - Specify version requirements
   - Document configuration options
""")

# 9. LIBRARY COMPARISON AND SELECTION
print("\n" + "=" * 60)
print("9. LIBRARY COMPARISON AND SELECTION")
print("=" * 60)

def create_library_comparison():
    """Create a library comparison guide"""
    
    comparison_content = '''"""
Python Library Comparison Guide
==============================

This guide helps you choose the right library for your needs.
"""

# Web Frameworks Comparison
web_frameworks = {
    "Flask": {
        "type": "Micro-framework",
        "learning_curve": "Easy",
        "flexibility": "High",
        "built_in_features": "Minimal",
        "best_for": ["APIs", "Small applications", "Prototyping"],
        "pros": ["Lightweight", "Flexible", "Easy to learn"],
        "cons": ["Few built-in features", "More boilerplate code"]
    },
    "Django": {
        "type": "Full-stack framework",
        "learning_curve": "Moderate",
        "flexibility": "Medium",
        "built_in_features": "Comprehensive",
        "best_for": ["Large applications", "Admin interfaces", "Rapid development"],
        "pros": ["Batteries included", "Admin interface", "ORM", "Security"],
        "cons": ["Heavy", "Less flexible", "Steeper learning curve"]
    },
    "FastAPI": {
        "type": "Modern API framework",
        "learning_curve": "Easy",
        "flexibility": "High",
        "built_in_features": "API-focused",
        "best_for": ["APIs", "Microservices", "High-performance apps"],
        "pros": ["Fast", "Auto-documentation", "Type hints", "Async support"],
        "cons": ["Newer", "Smaller ecosystem", "Less mature"]
    }
}

# Data Science Libraries Comparison
data_science_libs = {
    "NumPy": {
        "purpose": "Numerical computing",
        "strengths": ["Array operations", "Mathematical functions", "Performance"],
        "weaknesses": ["Limited data structures", "No built-in plotting"],
        "when_to_use": ["Mathematical computations", "Array operations", "Performance-critical code"]
    },
    "Pandas": {
        "purpose": "Data manipulation and analysis",
        "strengths": ["DataFrame operations", "Data cleaning", "Time series"],
        "weaknesses": ["Memory usage", "Learning curve", "Performance for large data"],
        "when_to_use": ["Data analysis", "Data cleaning", "Time series analysis"]
    },
    "Matplotlib": {
        "purpose": "Plotting and visualization",
        "strengths": ["Flexible", "Publication quality", "Wide range of plots"],
        "weaknesses": ["Verbose syntax", "Not interactive by default"],
        "when_to_use": ["Static plots", "Publication figures", "Custom visualizations"]
    }
}

# Machine Learning Libraries Comparison
ml_libs = {
    "Scikit-learn": {
        "type": "Traditional ML",
        "strengths": ["Comprehensive", "Well-documented", "Easy to use"],
        "weaknesses": ["No deep learning", "Limited to traditional ML"],
        "best_for": ["Classification", "Regression", "Clustering", "Feature selection"]
    },
    "TensorFlow": {
        "type": "Deep learning",
        "strengths": ["Production-ready", "Large ecosystem", "Good documentation"],
        "weaknesses": ["Steep learning curve", "Verbose syntax"],
        "best_for": ["Deep learning", "Production deployment", "Large-scale models"]
    },
    "PyTorch": {
        "type": "Deep learning",
        "strengths": ["Pythonic", "Dynamic computation", "Research-friendly"],
        "weaknesses": ["Smaller ecosystem", "Less production-ready"],
        "best_for": ["Research", "Prototyping", "Dynamic models"]
    }
}

def print_comparison(data, title):
    """Print library comparison in a formatted way"""
    print(f"\\n{title}")
    print("=" * 50)
    
    for lib_name, details in data.items():
        print(f"\\n{lib_name}:")
        for key, value in details.items():
            if isinstance(value, list):
                print(f"  {key}: {', '.join(value)}")
            else:
                print(f"  {key}: {value}")

# Print comparisons
if __name__ == "__main__":
    print_comparison(web_frameworks, "Web Frameworks Comparison")
    print_comparison(data_science_libs, "Data Science Libraries Comparison")
    print_comparison(ml_libs, "Machine Learning Libraries Comparison")
'''
    
    with open("03_Packages_Modules_Libraries_Tools/Examples/library_comparison.py", "w") as f:
        f.write(comparison_content)
    
    print("Created library comparison guide:")
    print("- library_comparison.py")

create_library_comparison()

# 10. EXERCISES
print("\n" + "=" * 60)
print("10. EXERCISES")
print("=" * 60)

print("""
Exercises to practice using Python libraries:

1. Web Development:
   - Create a simple Flask web application with multiple routes
   - Build a REST API using FastAPI
   - Create a web form with validation
   - Implement user authentication

2. Data Science:
   - Load and analyze a dataset using Pandas
   - Create visualizations with Matplotlib/Seaborn
   - Perform statistical analysis
   - Clean and preprocess data

3. Machine Learning:
   - Train a classification model with Scikit-learn
   - Perform cross-validation
   - Evaluate model performance
   - Save and load trained models

4. GUI Development:
   - Create a simple calculator with Tkinter
   - Build a file browser application
   - Create a data entry form
   - Implement a simple game

5. Testing:
   - Write unit tests for your functions
   - Use pytest fixtures and parametrization
   - Test error conditions
   - Measure test coverage

6. Library Integration:
   - Combine multiple libraries in one project
   - Handle library dependencies
   - Create a requirements file
   - Document library usage

7. Performance:
   - Profile your code
   - Optimize slow operations
   - Compare different libraries
   - Use appropriate data structures

8. Best Practices:
   - Follow library-specific conventions
   - Handle errors gracefully
   - Write clean, maintainable code
   - Document your code
""")

if __name__ == "__main__":
    print("\n" + "=" * 60)
    print("LIBRARIES AND FRAMEWORKS TUTORIAL COMPLETED!")
    print("=" * 60)
    print("Check the Examples folder for sample code created during this tutorial.") 