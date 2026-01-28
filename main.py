import sys

def analyze_log(file_path):
    try:
        with open(file_path, 'r') as file:
            lines = file.readlines()
        
        error_count = 0
        error_messages = []

        for line in lines:
            if "[ERROR]" in line:
                error_count += 1
                # Message ko extract karne ke liye logic
                parts = line.split("[ERROR]")
                if len(parts) > 1:
                    error_messages.append(parts[1].strip())

        # Report Print karna
        print("---------- LOG ANALYSIS REPORT ----------")
        print(f"Total Errors Found: {error_count}")
        print("-----------------------------------------")
        print("Detailed Error Messages:")
        for i, msg in enumerate(error_messages, 1):
            print(f"{i}. {msg}")
        print("-----------------------------------------")

    except FileNotFoundError:
        print("Error: File nahi mili! Sahi path check karein.")

if __name__ == "__main__":
    if len(sys.argv) < 2:
        print("Usage: python main.py server.log")
    else:
        analyze_log(sys.argv[1])