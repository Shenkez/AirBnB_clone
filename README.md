# ALX Python Command Interpreter

## Project Description

This project is a command-line interpreter built in Python, inspired by the Unix shell. The interpreter provides a simple and intuitive interface for users to interact with the underlying system, manage files, and perform various operations. It is designed as part of the ALX Software Engineering curriculum to help students understand the basics of command-line operations, parsing, and execution in Python.

## Features

- Command parsing and execution
- Built-in commands for navigation and file management
- Error handling and user feedback
- Extensible for additional commands

## Command Interpreter Description

The command interpreter reads commands from the user, parses them, and executes the corresponding actions. It supports basic commands such as `cd`, `ls`, `pwd`, and more. The interpreter runs in a loop, continuously awaiting user input until the `exit` command is issued.

## How to Start the Interpreter

1. **Clone the Repository:**
   ```sh
   git clone https://github.com/yourusername/alx-python-command-interpreter.git
   cd alx-python-command-interpreter
   ```

2. **Ensure Python is Installed:**
   Make sure you have Python 3.x installed on your system. You can check your Python version by running:
   ```sh
   python3 --version
   ```

3. **Run the Interpreter:**
   Start the command interpreter by executing the main Python file:
   ```sh
   python3 interpreter.py
   ```

## How to Use the Interpreter

Once the interpreter is running, you can start entering commands. Here are some basic commands and their usage:

- `help`: Displays a list of available commands.
- `exit`: Exits the interpreter.
- `pwd`: Prints the current working directory.
- `cd <directory>`: Changes the current working directory to the specified directory.
- `ls`: Lists the contents of the current directory.
- `mkdir <directory>`: Creates a new directory.
- `rm <file/directory>`: Removes a file or directory.

### Examples

1. **Navigating Directories:**
   ```sh
   $ cd /path/to/directory
   $ pwd
   /path/to/directory
   ```

2. **Listing Directory Contents:**
   ```sh
   $ ls
   file1.txt  file2.txt  directory1
   ```

3. **Creating and Removing Files/Directories:**
   ```sh
   $ mkdir new_directory
   $ ls
   file1.txt  file2.txt  directory1  new_directory
   $ rm new_directory
   $ ls
   file1.txt  file2.txt  directory1
   ```

4. **Getting Help:**
   ```sh
   $ help
   Available commands:
   cd <directory> - Change the current directory
   ls - List directory contents
   pwd - Print current working directory
   mkdir <directory> - Create a new directory
   rm <file/directory> - Remove a file or directory
   exit - Exit the interpreter
   ```

## Extending the Interpreter

The command interpreter is designed to be extensible. You can add new commands by modifying the `commands.py` file and updating the command dictionary in `interpreter.py`. Follow the existing structure to ensure consistency and proper integration.

---

This project provides a foundational understanding of building command-line applications in Python. Happy coding!
