# CLI Log Analyzer Project

### 1. Project Goal
This project is a Python-based Command Line Interface (CLI) tool that parses server log files. It identifies lines marked as `[ERROR]`, counts them, and displays a summary report of all found errors.

### 2. Setup Instructions
To run this project locally, follow these steps:
1. Clone the repository.
2. Open your terminal in the project folder.
3. Run the following command:
   ```bash
   python main.py server.log
   3. The Logic (How I thought)
​Approach: I used Python's file handling to read the log file line-by-line. This is memory efficient. I used string searching to find the [ERROR] keyword.
​Hardest Bug: Handling the file path when the script is run from a different directory. I resolved this by using relative paths and adding error handling to check if the file exists.
​4. Output Screenshots & Proof of Work
​1. Project Initiation
​Initializing the project folder and organizing all required files.
​2. Python Source Code
​The core logic of the application written in main.py.
​3. Input Data (server.log)
​A view of the raw log file containing info and error tags.
​4. Project Documentation
​Finalizing the documentation and verification of the README.
​5. Command Execution
​Running the script via terminal using the CLI command.
​6. Final Analysis Output
​The successful final result showing error counts and messages.
​5. Future Improvements
​Add support for exporting the report to a .txt or .csv file.
​Implement color-coded output for better readability in the terminal.
​<!-- end list -->
