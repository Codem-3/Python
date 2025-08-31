"""
File Operations Module
=====================

A collection of useful file handling functions.
"""

import os
import json
import shutil
import zipfile
import tempfile
from pathlib import Path
from typing import List, Dict, Any, Optional, Union
import logging

# Configure logging
logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)


def read_file_safely(file_path: str, encoding: str = "utf-8") -> str:
    """
    Safely read a text file with error handling.

    Args:
        file_path: Path to the file to read
        encoding: File encoding (default: utf-8)

    Returns:
        File contents as string

    Raises:
        FileNotFoundError: If file doesn't exist
        PermissionError: If file can't be read
        UnicodeDecodeError: If encoding is wrong
    """
    try:
        with open(file_path, "r", encoding=encoding) as file:
            content = file.read()
        logger.info(f"Successfully read file: {file_path}")
        return content
    except FileNotFoundError:
        logger.error(f"File not found: {file_path}")
        raise
    except PermissionError:
        logger.error(f"Permission denied reading file: {file_path}")
        raise
    except UnicodeDecodeError as e:
        logger.error(f"Encoding error reading file {file_path}: {e}")
        raise


def write_json(data: Any, file_path: str, indent: int = 2) -> None:
    """
    Write data to a JSON file.

    Args:
        data: Data to write (must be JSON serializable)
        file_path: Path to the JSON file
        indent: Number of spaces for indentation

    Raises:
        TypeError: If data is not JSON serializable
        PermissionError: If file can't be written
    """
    try:
        with open(file_path, "w", encoding="utf-8") as file:
            json.dump(data, file, indent=indent, ensure_ascii=False)
        logger.info(f"Successfully wrote JSON file: {file_path}")
    except TypeError as e:
        logger.error(f"Data not JSON serializable: {e}")
        raise
    except PermissionError:
        logger.error(f"Permission denied writing file: {file_path}")
        raise


def read_json(file_path: str) -> Any:
    """
    Read data from a JSON file.

    Args:
        file_path: Path to the JSON file

    Returns:
        Parsed JSON data

    Raises:
        FileNotFoundError: If file doesn't exist
        json.JSONDecodeError: If file is not valid JSON
    """
    try:
        with open(file_path, "r", encoding="utf-8") as file:
            data = json.load(file)
        logger.info(f"Successfully read JSON file: {file_path}")
        return data
    except FileNotFoundError:
        logger.error(f"JSON file not found: {file_path}")
        raise
    except json.JSONDecodeError as e:
        logger.error(f"Invalid JSON in file {file_path}: {e}")
        raise


def backup_file(file_path: str, backup_dir: Optional[str] = None) -> str:
    """
    Create a backup of a file.

    Args:
        file_path: Path to the file to backup
        backup_dir: Directory for backup (default: same directory)

    Returns:
        Path to the backup file

    Raises:
        FileNotFoundError: If source file doesn't exist
        PermissionError: If backup can't be created
    """
    if not os.path.exists(file_path):
        raise FileNotFoundError(f"Source file not found: {file_path}")

    # Create backup directory if not specified
    if backup_dir is None:
        backup_dir = os.path.dirname(file_path)

    # Create backup directory if it doesn't exist
    os.makedirs(backup_dir, exist_ok=True)

    # Generate backup filename with timestamp
    from datetime import datetime

    timestamp = datetime.now().strftime("%Y%m%d_%H%M%S")
    filename = os.path.basename(file_path)
    name, ext = os.path.splitext(filename)
    backup_filename = f"{name}_backup_{timestamp}{ext}"
    backup_path = os.path.join(backup_dir, backup_filename)

    try:
        shutil.copy2(file_path, backup_path)
        logger.info(f"Created backup: {backup_path}")
        return backup_path
    except PermissionError:
        logger.error(f"Permission denied creating backup: {backup_path}")
        raise


def find_files_by_extension(directory: str, extension: str) -> List[str]:
    """
    Find all files with a specific extension in a directory.

    Args:
        directory: Directory to search in
        extension: File extension (with or without dot)

    Returns:
        List of file paths matching the extension

    Raises:
        FileNotFoundError: If directory doesn't exist
    """
    if not os.path.exists(directory):
        raise FileNotFoundError(f"Directory not found: {directory}")

    # Ensure extension starts with dot
    if not extension.startswith("."):
        extension = "." + extension

    matching_files = []

    try:
        for root, dirs, files in os.walk(directory):
            for file in files:
                if file.endswith(extension):
                    file_path = os.path.join(root, file)
                    matching_files.append(file_path)

        logger.info(f"Found {len(matching_files)} files with extension {extension}")
        return matching_files
    except PermissionError:
        logger.error(f"Permission denied accessing directory: {directory}")
        raise


def get_file_info(file_path: str) -> Dict[str, Any]:
    """
    Get detailed information about a file.

    Args:
        file_path: Path to the file

    Returns:
        Dictionary with file information

    Raises:
        FileNotFoundError: If file doesn't exist
    """
    if not os.path.exists(file_path):
        raise FileNotFoundError(f"File not found: {file_path}")

    stat = os.stat(file_path)

    info = {
        "path": file_path,
        "name": os.path.basename(file_path),
        "size": stat.st_size,
        "created": stat.st_ctime,
        "modified": stat.st_mtime,
        "accessed": stat.st_atime,
        "is_file": os.path.isfile(file_path),
        "is_directory": os.path.isdir(file_path),
        "extension": os.path.splitext(file_path)[1],
        "readable": os.access(file_path, os.R_OK),
        "writable": os.access(file_path, os.W_OK),
        "executable": os.access(file_path, os.X_OK),
    }

    return info


def create_directory_structure(base_path: str, structure: Dict[str, Any]) -> None:
    """
    Create a directory structure from a dictionary.

    Args:
        base_path: Base directory path
        structure: Dictionary defining the structure

    Example:
        structure = {
            'src': {
                'main.py': None,
                'utils': {
                    'helper.py': None
                }
            },
            'tests': {
                'test_main.py': None
            }
        }
    """

    def create_structure_recursive(path: str, struct: Dict[str, Any]) -> None:
        for name, content in struct.items():
            item_path = os.path.join(path, name)

            if content is None:
                # Create empty file
                with open(item_path, "w") as f:
                    pass
                logger.info(f"Created file: {item_path}")
            elif isinstance(content, dict):
                # Create directory
                os.makedirs(item_path, exist_ok=True)
                logger.info(f"Created directory: {item_path}")
                create_structure_recursive(item_path, content)
            else:
                # Create file with content
                with open(item_path, "w", encoding="utf-8") as f:
                    f.write(str(content))
                logger.info(f"Created file with content: {item_path}")

    os.makedirs(base_path, exist_ok=True)
    create_structure_recursive(base_path, structure)


def zip_directory(source_dir: str, zip_path: str) -> None:
    """
    Create a ZIP archive of a directory.

    Args:
        source_dir: Directory to zip
        zip_path: Path for the ZIP file

    Raises:
        FileNotFoundError: If source directory doesn't exist
        PermissionError: If ZIP can't be created
    """
    if not os.path.exists(source_dir):
        raise FileNotFoundError(f"Source directory not found: {source_dir}")

    try:
        with zipfile.ZipFile(zip_path, "w", zipfile.ZIP_DEFLATED) as zipf:
            for root, dirs, files in os.walk(source_dir):
                for file in files:
                    file_path = os.path.join(root, file)
                    arcname = os.path.relpath(file_path, source_dir)
                    zipf.write(file_path, arcname)

        logger.info(f"Created ZIP archive: {zip_path}")
    except PermissionError:
        logger.error(f"Permission denied creating ZIP: {zip_path}")
        raise


def extract_zip(zip_path: str, extract_dir: str) -> None:
    """
    Extract a ZIP archive to a directory.

    Args:
        zip_path: Path to the ZIP file
        extract_dir: Directory to extract to

    Raises:
        FileNotFoundError: If ZIP file doesn't exist
        zipfile.BadZipFile: If ZIP file is corrupted
    """
    if not os.path.exists(zip_path):
        raise FileNotFoundError(f"ZIP file not found: {zip_path}")

    os.makedirs(extract_dir, exist_ok=True)

    try:
        with zipfile.ZipFile(zip_path, "r") as zipf:
            zipf.extractall(extract_dir)
        logger.info(f"Extracted ZIP to: {extract_dir}")
    except zipfile.BadZipFile as e:
        logger.error(f"Corrupted ZIP file {zip_path}: {e}")
        raise


def safe_delete_file(file_path: str, backup: bool = True) -> bool:
    """
    Safely delete a file with optional backup.

    Args:
        file_path: Path to the file to delete
        backup: Whether to create a backup before deletion

    Returns:
        True if deletion was successful, False otherwise
    """
    if not os.path.exists(file_path):
        logger.warning(f"File not found for deletion: {file_path}")
        return False

    try:
        if backup:
            backup_file(file_path)

        os.remove(file_path)
        logger.info(f"Successfully deleted file: {file_path}")
        return True
    except PermissionError:
        logger.error(f"Permission denied deleting file: {file_path}")
        return False
    except Exception as e:
        logger.error(f"Error deleting file {file_path}: {e}")
        return False


def get_directory_size(directory: str) -> int:
    """
    Calculate the total size of a directory in bytes.

    Args:
        directory: Directory path

    Returns:
        Total size in bytes

    Raises:
        FileNotFoundError: If directory doesn't exist
    """
    if not os.path.exists(directory):
        raise FileNotFoundError(f"Directory not found: {directory}")

    total_size = 0

    try:
        for root, dirs, files in os.walk(directory):
            for file in files:
                file_path = os.path.join(root, file)
                if os.path.exists(file_path):
                    total_size += os.path.getsize(file_path)

        logger.info(f"Directory size: {total_size} bytes")
        return total_size
    except PermissionError:
        logger.error(f"Permission denied accessing directory: {directory}")
        raise


def format_file_size(size_bytes: int) -> str:
    """
    Format file size in human-readable format.

    Args:
        size_bytes: Size in bytes

    Returns:
        Formatted size string
    """
    for unit in ["B", "KB", "MB", "GB", "TB"]:
        if size_bytes < 1024.0:
            return f"{size_bytes:.1f} {unit}"
        size_bytes /= 1024.0
    return f"{size_bytes:.1f} PB"


if __name__ == "__main__":
    # Test the functions
    print("Testing file utilities...")

    # Create a test file
    test_file = "test_file.txt"
    test_content = "Hello, World!"

    with open(test_file, "w") as f:
        f.write(test_content)

    # Test read_file_safely
    content = read_file_safely(test_file)
    assert content == test_content

    # Test file info
    info = get_file_info(test_file)
    assert info["name"] == "test_file.txt"
    assert info["size"] == len(test_content)

    # Test backup
    backup_path = backup_file(test_file)
    assert os.path.exists(backup_path)

    # Clean up
    os.remove(test_file)
    os.remove(backup_path)

    print("All tests passed!")
