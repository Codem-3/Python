# ============================================
# PYTHON FILE HANDLING TUTORIAL
# ============================================
# This file covers comprehensive file handling in Python
# with examples, best practices, and real-world scenarios

print("=" * 60)
print("PYTHON FILE HANDLING TUTORIAL")
print("=" * 60)

# ============================================
# SECTION 1: INTRODUCTION TO FILE HANDLING
# ============================================
print("\n" + "=" * 60)
print("SECTION 1: INTRODUCTION TO FILE HANDLING")
print("=" * 60)

print("\n1.1 What is File Handling?")
print("-" * 30)
print(
    """
File handling in Python allows you to:
- Read data from files
- Write data to files
- Create new files
- Modify existing files
- Delete files
- Work with different file formats (text, binary, CSV, JSON, etc.)

Common use cases:
- Reading configuration files
- Processing data files
- Logging information
- Storing user data
- Working with databases
- File system operations
"""
)

print("\n1.2 File Modes")
print("-" * 30)
print(
    """
'r'  - Read mode (default)
'w'  - Write mode (overwrites existing content)
'a'  - Append mode (adds to existing content)
'x'  - Exclusive creation (fails if file exists)
'b'  - Binary mode
't'  - Text mode (default)
'+'  - Read and write mode

Combinations:
'r+' - Read and write
'w+' - Write and read (truncates file)
'a+' - Append and read
'rb' - Read binary
'wb' - Write binary
'ab' - Append binary
"""
)

# ============================================
# SECTION 2: BASIC FILE OPERATIONS
# ============================================
print("\n" + "=" * 60)
print("SECTION 2: BASIC FILE OPERATIONS")
print("=" * 60)

print("\n2.1 Opening and Closing Files")
print("-" * 30)

# Method 1: Traditional approach
print("Method 1: Traditional open/close")
try:
    file = open("sample.txt", "w")
    file.write("Hello, this is a sample file!\n")
    file.write("This is the second line.\n")
    file.close()
    print("File created and written successfully")
except Exception as e:
    print(f"Error: {e}")

# Method 2: Using with statement (recommended)
print("\nMethod 2: Using 'with' statement (recommended)")
try:
    with open("sample.txt", "w") as file:
        file.write("Hello, this is a sample file!\n")
        file.write("This is the second line.\n")
    print("File created and written successfully (with statement)")
except Exception as e:
    print(f"Error: {e}")

print("\n2.2 Reading Files")
print("-" * 30)

# Reading entire file
print("Reading entire file:")
try:
    with open("sample.txt", "r") as file:
        content = file.read()
        print(f"File content:\n{content}")
except FileNotFoundError:
    print("File not found")

# Reading line by line
print("\nReading line by line:")
try:
    with open("sample.txt", "r") as file:
        for line_num, line in enumerate(file, 1):
            print(f"Line {line_num}: {line.strip()}")
except FileNotFoundError:
    print("File not found")

# Reading all lines into a list
print("\nReading all lines into a list:")
try:
    with open("sample.txt", "r") as file:
        lines = file.readlines()
        print(f"All lines: {lines}")
except FileNotFoundError:
    print("File not found")

print("\n2.3 Writing to Files")
print("-" * 30)

# Writing text
print("Writing text to file:")
try:
    with open("output.txt", "w") as file:
        file.write("This is line 1\n")
        file.write("This is line 2\n")
        file.write("This is line 3\n")
    print("Text written successfully")
except Exception as e:
    print(f"Error: {e}")

# Writing multiple lines
print("\nWriting multiple lines:")
lines_to_write = [
    "First line of the file",
    "Second line of the file",
    "Third line of the file",
    "Fourth line of the file",
]

try:
    with open("multiple_lines.txt", "w") as file:
        file.writelines(line + "\n" for line in lines_to_write)
    print("Multiple lines written successfully")
except Exception as e:
    print(f"Error: {e}")

print("\n2.4 Appending to Files")
print("-" * 30)

try:
    with open("sample.txt", "a") as file:
        file.write("This line was appended.\n")
        file.write("Another appended line.\n")
    print("Content appended successfully")
except Exception as e:
    print(f"Error: {e}")

# ============================================
# SECTION 3: FILE POSITIONING AND SEEKING
# ============================================
print("\n" + "=" * 60)
print("SECTION 3: FILE POSITIONING AND SEEKING")
print("=" * 60)

print("\n3.1 File Position")
print("-" * 30)

try:
    with open("sample.txt", "r") as file:
        print(f"Initial position: {file.tell()}")

        # Read first 10 characters
        content = file.read(10)
        print(f"Read: '{content}'")
        print(f"Position after read: {file.tell()}")

        # Seek to beginning
        file.seek(0)
        print(f"Position after seek(0): {file.tell()}")

        # Seek to specific position
        file.seek(5)
        print(f"Position after seek(5): {file.tell()}")
        content = file.read(5)
        print(f"Read from position 5: '{content}'")

except FileNotFoundError:
    print("File not found")

print("\n3.2 Seek Modes")
print("-" * 30)
print(
    """
seek(offset, whence):
- whence=0: From beginning of file (default)
- whence=1: From current position
- whence=2: From end of file
"""
)

try:
    with open("sample.txt", "r") as file:
        # Read last 10 characters
        file.seek(0, 2)  # Go to end
        end_pos = file.tell()
        file.seek(max(0, end_pos - 10))  # Go back 10 characters
        last_content = file.read()
        print(f"Last 10 characters: '{last_content}'")

except FileNotFoundError:
    print("File not found")

# ============================================
# SECTION 4: WORKING WITH DIFFERENT FILE TYPES
# ============================================
print("\n" + "=" * 60)
print("SECTION 4: WORKING WITH DIFFERENT FILE TYPES")
print("=" * 60)

print("\n4.1 CSV Files")
print("-" * 30)
import csv

# Writing CSV
print("Writing CSV file:")
data = [
    ["Name", "Age", "City"],
    ["John", 25, "New York"],
    ["Alice", 30, "Boston"],
    ["Bob", 35, "Chicago"],
]

try:
    with open("people.csv", "w", newline="") as file:
        writer = csv.writer(file)
        writer.writerows(data)
    print("CSV file created successfully")
except Exception as e:
    print(f"Error: {e}")

# Reading CSV
print("\nReading CSV file:")
try:
    with open("people.csv", "r") as file:
        reader = csv.reader(file)
        for row in reader:
            print(f"Row: {row}")
except FileNotFoundError:
    print("CSV file not found")

print("\n4.2 JSON Files")
print("-" * 30)
import json

# Writing JSON
print("Writing JSON file:")
data = {
    "name": "John Doe",
    "age": 30,
    "city": "New York",
    "hobbies": ["reading", "swimming", "coding"],
    "active": True,
}

try:
    with open("data.json", "w") as file:
        json.dump(data, file, indent=4)
    print("JSON file created successfully")
except Exception as e:
    print(f"Error: {e}")

# Reading JSON
print("\nReading JSON file:")
try:
    with open("data.json", "r") as file:
        loaded_data = json.load(file)
        print(f"Loaded data: {loaded_data}")
        print(f"Name: {loaded_data['name']}")
        print(f"Hobbies: {loaded_data['hobbies']}")
except FileNotFoundError:
    print("JSON file not found")

print("\n4.3 Binary Files")
print("-" * 30)

# Writing binary data
print("Writing binary file:")
binary_data = bytes([65, 66, 67, 68, 69, 70])  # ABCDEF

try:
    with open("binary_data.bin", "wb") as file:
        file.write(binary_data)
    print("Binary file created successfully")
except Exception as e:
    print(f"Error: {e}")

# Reading binary data
print("\nReading binary file:")
try:
    with open("binary_data.bin", "rb") as file:
        data = file.read()
        print(f"Binary data: {data}")
        print(f"As string: {data.decode('utf-8')}")
except FileNotFoundError:
    print("Binary file not found")

# ============================================
# SECTION 5: FILE SYSTEM OPERATIONS
# ============================================
print("\n" + "=" * 60)
print("SECTION 5: FILE SYSTEM OPERATIONS")
print("=" * 60)

print("\n5.1 File Information")
print("-" * 30)
import os

# Check if file exists
print("Checking file existence:")
files_to_check = ["sample.txt", "nonexistent.txt", "output.txt"]

for file_name in files_to_check:
    if os.path.exists(file_name):
        print(f"✓ {file_name} exists")

        # Get file size
        size = os.path.getsize(file_name)
        print(f"  Size: {size} bytes")

        # Get file modification time
        mtime = os.path.getmtime(file_name)
        print(f"  Modified: {mtime}")
    else:
        print(f"✗ {file_name} does not exist")

print("\n5.2 Directory Operations")
print("-" * 30)

# List files in current directory
print("Files in current directory:")
try:
    files = os.listdir(".")
    for file in files:
        if os.path.isfile(file):
            print(f"  File: {file}")
        elif os.path.isdir(file):
            print(f"  Directory: {file}")
except Exception as e:
    print(f"Error: {e}")

# Create directory
print("\nCreating directory:")
try:
    os.makedirs("test_folder", exist_ok=True)
    print("Directory created successfully")
except Exception as e:
    print(f"Error: {e}")

print("\n5.3 File Operations")
print("-" * 30)

# Copy file
import shutil

print("Copying file:")
try:
    shutil.copy("sample.txt", "sample_copy.txt")
    print("File copied successfully")
except Exception as e:
    print(f"Error: {e}")

# Rename file
print("\nRenaming file:")
try:
    os.rename("sample_copy.txt", "sample_renamed.txt")
    print("File renamed successfully")
except Exception as e:
    print(f"Error: {e}")

# Delete file
print("\nDeleting file:")
try:
    os.remove("sample_renamed.txt")
    print("File deleted successfully")
except Exception as e:
    print(f"Error: {e}")

# ============================================
# SECTION 6: ERROR HANDLING AND BEST PRACTICES
# ============================================
print("\n" + "=" * 60)
print("SECTION 6: ERROR HANDLING AND BEST PRACTICES")
print("=" * 60)

print("\n6.1 Comprehensive Error Handling")
print("-" * 30)


def safe_file_operation(filename, operation="read"):
    """Safely perform file operations with comprehensive error handling"""
    try:
        if operation == "read":
            with open(filename, "r") as file:
                return file.read()
        elif operation == "write":
            with open(filename, "w") as file:
                file.write("Test content")
                return "File written successfully"
    except FileNotFoundError:
        return f"Error: File '{filename}' not found"
    except PermissionError:
        return f"Error: No permission to access '{filename}'"
    except UnicodeDecodeError:
        return f"Error: Cannot decode file '{filename}'"
    except Exception as e:
        return f"Unexpected error: {e}"


# Test safe file operations
print("Testing safe file operations:")
print(safe_file_operation("sample.txt", "read"))
print(safe_file_operation("nonexistent.txt", "read"))
print(safe_file_operation("test_output.txt", "write"))

print("\n6.2 File Context Managers")
print("-" * 30)


class FileManager:
    """Custom file manager with context management"""

    def __init__(self, filename, mode="r"):
        self.filename = filename
        self.mode = mode
        self.file = None

    def __enter__(self):
        self.file = open(self.filename, self.mode)
        return self.file

    def __exit__(self, exc_type, exc_val, exc_tb):
        if self.file:
            self.file.close()
        if exc_type:
            print(f"Exception occurred: {exc_val}")
        return False  # Don't suppress exceptions


# Using custom file manager
print("Using custom file manager:")
try:
    with FileManager("sample.txt", "r") as file:
        content = file.read()
        print(f"Content: {content[:50]}...")
except Exception as e:
    print(f"Error: {e}")

print("\n6.3 Best Practices")
print("-" * 30)
print(
    """
1. Always use 'with' statements for file operations
   Good: with open('file.txt', 'r') as f: content = f.read()
   Bad:  f = open('file.txt', 'r'); content = f.read(); f.close()

2. Handle specific exceptions
   Good: except FileNotFoundError: handle missing file
   Bad:  except: pass

3. Use appropriate file modes
   - 'r' for reading
   - 'w' for writing (overwrites)
   - 'a' for appending
   - 'x' for exclusive creation

4. Close files properly
   - 'with' statements handle this automatically
   - Always close files manually if not using 'with'

5. Check file existence before operations
   - Use os.path.exists() or try/except
   - Don't assume files exist

6. Use absolute paths for important files
   - Relative paths can be unreliable
   - Consider using pathlib for modern path handling

7. Handle encoding explicitly
   - Specify encoding for text files
   - Use 'utf-8' as default
"""
)

# ============================================
# SECTION 7: REAL-WORLD EXAMPLES
# ============================================
print("\n" + "=" * 60)
print("SECTION 7: REAL-WORLD EXAMPLES")
print("=" * 60)

print("\n7.1 Configuration File Handler")
print("-" * 30)


class ConfigManager:
    """Manages application configuration files"""

    def __init__(self, config_file="config.ini"):
        self.config_file = config_file
        self.config = {}

    def load_config(self):
        """Load configuration from file"""
        try:
            with open(self.config_file, "r") as file:
                for line in file:
                    line = line.strip()
                    if line and not line.startswith("#"):
                        key, value = line.split("=", 1)
                        self.config[key.strip()] = value.strip()
            return True
        except FileNotFoundError:
            print(f"Config file '{self.config_file}' not found, using defaults")
            return False
        except Exception as e:
            print(f"Error loading config: {e}")
            return False

    def save_config(self):
        """Save configuration to file"""
        try:
            with open(self.config_file, "w") as file:
                for key, value in self.config.items():
                    file.write(f"{key}={value}\n")
            return True
        except Exception as e:
            print(f"Error saving config: {e}")
            return False

    def get(self, key, default=None):
        """Get configuration value"""
        return self.config.get(key, default)

    def set(self, key, value):
        """Set configuration value"""
        self.config[key] = value


# Test configuration manager
print("Testing configuration manager:")
config = ConfigManager("app_config.ini")
config.set("database_url", "localhost:5432")
config.set("debug_mode", "true")
config.set("log_level", "INFO")

if config.save_config():
    print("Configuration saved successfully")

config2 = ConfigManager("app_config.ini")
if config2.load_config():
    print(f"Database URL: {config2.get('database_url')}")
    print(f"Debug Mode: {config2.get('debug_mode')}")

print("\n7.2 Log File Handler")
print("-" * 30)


class LogHandler:
    """Handles application logging to files"""

    def __init__(self, log_file="app.log"):
        self.log_file = log_file

    def log(self, message, level="INFO"):
        """Write log message to file"""
        import datetime

        timestamp = datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")
        log_entry = f"[{timestamp}] {level}: {message}\n"

        try:
            with open(self.log_file, "a") as file:
                file.write(log_entry)
        except Exception as e:
            print(f"Error writing to log: {e}")

    def read_logs(self, lines=10):
        """Read recent log entries"""
        try:
            with open(self.log_file, "r") as file:
                all_lines = file.readlines()
                return all_lines[-lines:] if len(all_lines) > lines else all_lines
        except FileNotFoundError:
            return []
        except Exception as e:
            print(f"Error reading logs: {e}")
            return []


# Test log handler
print("Testing log handler:")
logger = LogHandler("test.log")
logger.log("Application started", "INFO")
logger.log("Processing user request", "DEBUG")
logger.log("User authentication successful", "INFO")
logger.log("Database connection established", "INFO")

print("Recent log entries:")
recent_logs = logger.read_logs(5)
for log in recent_logs:
    print(f"  {log.strip()}")

print("\n7.3 Data File Processor")
print("-" * 30)


class DataProcessor:
    """Processes data files with error handling"""

    def __init__(self, input_file, output_file):
        self.input_file = input_file
        self.output_file = output_file

    def process_csv_data(self):
        """Process CSV data with validation"""
        try:
            processed_data = []

            with open(self.input_file, "r") as infile:
                reader = csv.reader(infile)
                header = next(reader)  # Skip header

                for row_num, row in enumerate(reader, 2):
                    try:
                        # Validate row data
                        if len(row) >= 3:
                            name = row[0].strip()
                            age = int(row[1])
                            city = row[2].strip()

                            if name and age > 0 and city:
                                processed_data.append([name, age, city])
                            else:
                                print(f"Invalid data in row {row_num}: {row}")
                        else:
                            print(f"Insufficient data in row {row_num}: {row}")

                    except ValueError:
                        print(f"Invalid age in row {row_num}: {row}")
                    except Exception as e:
                        print(f"Error processing row {row_num}: {e}")

            # Write processed data
            with open(self.output_file, "w", newline="") as outfile:
                writer = csv.writer(outfile)
                writer.writerow(["Name", "Age", "City"])
                writer.writerows(processed_data)

            return len(processed_data)

        except FileNotFoundError:
            print(f"Input file '{self.input_file}' not found")
            return 0
        except Exception as e:
            print(f"Error processing data: {e}")
            return 0


# Test data processor
print("Testing data processor:")
processor = DataProcessor("people.csv", "processed_people.csv")
processed_count = processor.process_csv_data()
print(f"Processed {processed_count} records successfully")

# ============================================
# SECTION 8: ADVANCED FILE HANDLING
# ============================================
print("\n" + "=" * 60)
print("SECTION 8: ADVANCED FILE HANDLING")
print("=" * 60)

print("\n8.1 Working with Large Files")
print("-" * 30)


def process_large_file(filename, chunk_size=1024):
    """Process large files in chunks to save memory"""
    try:
        with open(filename, "r") as file:
            chunk_num = 0
            while True:
                chunk = file.read(chunk_size)
                if not chunk:
                    break

                chunk_num += 1
                print(f"Processing chunk {chunk_num} ({len(chunk)} characters)")

                # Process the chunk (example: count characters)
                char_count = len(chunk)
                word_count = len(chunk.split())

                print(f"  Characters: {char_count}, Words: {word_count}")

        return True
    except FileNotFoundError:
        print(f"File '{filename}' not found")
        return False
    except Exception as e:
        print(f"Error processing file: {e}")
        return False


# Create a large file for testing
print("Creating large file for testing:")
try:
    with open("large_file.txt", "w") as file:
        for i in range(1000):
            file.write(f"This is line {i+1} of the large file. " * 5 + "\n")
    print("Large file created successfully")

    # Process the large file
    print("\nProcessing large file:")
    process_large_file("large_file.txt", 2048)

except Exception as e:
    print(f"Error: {e}")

print("\n8.2 File Compression")
print("-" * 30)
import gzip
import zipfile

# Gzip compression
print("Gzip compression:")
try:
    with open("sample.txt", "rb") as infile:
        with gzip.open("sample.txt.gz", "wb") as outfile:
            outfile.write(infile.read())
    print("File compressed with gzip successfully")
except Exception as e:
    print(f"Error: {e}")

# Reading gzipped file
print("\nReading gzipped file:")
try:
    with gzip.open("sample.txt.gz", "rb") as file:
        content = file.read().decode("utf-8")
        print(f"Decompressed content: {content[:100]}...")
except Exception as e:
    print(f"Error: {e}")

# ZIP file creation
print("\nZIP file creation:")
try:
    with zipfile.ZipFile("archive.zip", "w") as zipf:
        zipf.write("sample.txt")
        zipf.write("people.csv")
    print("ZIP archive created successfully")
except Exception as e:
    print(f"Error: {e}")

# List ZIP contents
print("\nZIP file contents:")
try:
    with zipfile.ZipFile("archive.zip", "r") as zipf:
        for file_info in zipf.infolist():
            print(f"  {file_info.filename} - {file_info.file_size} bytes")
except Exception as e:
    print(f"Error: {e}")

# ============================================
# SUMMARY
# ============================================
print("\n" + "=" * 60)
print("SUMMARY")
print("=" * 60)

print(
    """
🎯 WHAT YOU'VE LEARNED:

1. BASIC FILE OPERATIONS
   - Opening and closing files
   - Reading and writing text
   - File positioning and seeking
   - Different file modes

2. FILE TYPES AND FORMATS
   - Text files
   - CSV files with csv module
   - JSON files with json module
   - Binary files
   - Compressed files (gzip, zip)

3. FILE SYSTEM OPERATIONS
   - File existence checking
   - Directory operations
   - File copying, renaming, deletion
   - File information retrieval

4. ERROR HANDLING
   - Comprehensive exception handling
   - Custom file managers
   - Best practices for file operations
   - Safe file operations

5. REAL-WORLD APPLICATIONS
   - Configuration file management
   - Log file handling
   - Data file processing
   - Large file processing

6. ADVANCED TECHNIQUES
   - Memory-efficient file processing
   - File compression and archiving
   - Custom context managers
   - Batch file operations

🚀 KEY TAKEAWAYS:
- Always use 'with' statements for file operations
- Handle specific exceptions appropriately
- Choose the right file mode for your needs
- Use appropriate data formats (CSV, JSON, etc.)
- Process large files in chunks
- Implement proper error handling and logging
- Follow best practices for file management

To run this tutorial: python python_file_handling.py
"""
)

print("\nHappy coding with Python file handling! 🐍📁")
print("Remember: Proper file handling makes your applications more robust!")
