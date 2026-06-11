# write data to a csv file and then read it back

import csv

# 1. Defining the data
data_to_write = [
    ['Name', 'Department', 'Salary'],
    ['Alice', 'Engineering', '95000'],
    ['Bob', 'Marketing', '70000'],
    ['Charlie', 'Design', '80000']
]

file_name = 'employees.csv'

# 2. Writing to a CSV file
with open(file_name, mode='w', newline='', encoding='utf-8') as file:
    writer = csv.writer(file)
    writer.writerows(data_to_write)
    print(f"Successfully wrote data to {file_name}")

# 3. Reading from the CSV file
print("\nReading data back from CSV:")
with open(file_name, mode='r', encoding='utf-8') as file:
    reader = csv.reader(file)
    for row in reader:
        # Each row is returned as a list of strings
        print(row)