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
​Initializing the project fol<img width="1920" height="1004" alt="start with folder" src="https://github.com/user-attachments/assets/727c0f6b-9912-4ee3-8759-cd6567d8ba77" />
der and organizing all required files.
​2. Python Source Code
<img width="1895" height="766" alt="python main" src="https://github.com/user-attachments/assets/d6879530-18ac-45f7-8ca4-b14c102d5a77" />
​The core logic of the application written in main.py.
​3. Input Data (server.log)
<img width="1794" height="1003" alt="serverlog" src="https://github.com/user-attachments/assets/d21cbdd5-ab71-45f9-8a37-7188e5c7996c" />
​A view of the raw log file containing info and error tags.
​4. Project Documentation
<img width="1801" height="783" alt="README" src="https://github.com/user-attachments/assets/d5956cf5-ccdb-48cd-956a-d24c260564fa" />
​Finalizing the documentation and verification of the README.
​5. Command Execution
<img width="1806" height="1009" alt="output" src="https://github.com/user-attachments/assets/d6a597d1-9070-4ee7-bf2d-ec62deb972a8" />
Running the script via terminal using the CLI command.
​6. Final Analysis Output
img width="1801" height="783" alt="terminal" src="https://github.com/user-attachments/assets/1d55b7f2-00a4-4be9-925c-b93ef24a3c96" />
​The successful final result showing error counts and messages.


​5. Future Improvements
​Add support for exporting the report to a .txt or .csv file.
​Implement color-coded output for better readability in the terminal.
​<!-- end list -->

