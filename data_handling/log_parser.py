# assume a common log format where each line includes a date, a log level (INFO, WARNING, ERROR), and a message

import re
import os

# 1. Create a dummy log file for demonstration
def create_dummy_log(filename):
    logs = [
        "2026-06-22 10:00:01 INFO System started",
        "2026-06-22 10:05:20 ERROR Database connection failed",
        "2026-06-22 10:10:45 INFO User login successful",
        "2026-06-22 10:15:10 ERROR Disk space critical",
        "2026-06-22 10:20:00 WARNING High memory usage"
    ]
    with open(filename, 'w') as f:
        f.write("\n".join(logs))
    print(f"File '{filename}' created successfully.")

# 2. Parse the log file
def parse_logs(input_file, log_level="ERROR"):
    extracted_errors = []
    # Regex to find lines containing the specified log level
    pattern = re.compile(rf".* {log_level} .*")
    
    try:
        with open(input_file, 'r') as f:
            for line in f:
                if pattern.match(line):
                    extracted_errors.append(line.strip())
        return extracted_errors
    except FileNotFoundError:
        print("Error: The log file was not found.")
        return []

if __name__ == "__main__":
    log_filename = "server.log"
    
    # Create the file
    create_dummy_log(log_filename)
    
    # Parse the file
    print(f"\nExtracting entries with level 'ERROR':")
    errors = parse_logs(log_filename, "ERROR")
    
    for entry in errors:
        print(f"Found: {entry}")