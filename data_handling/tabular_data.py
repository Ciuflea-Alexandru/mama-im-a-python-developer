import pandas as pd
import numpy as np

# 1. Create a sample dataset (Employee data)
data = {
    'Name': ['Alice', 'Bob', 'Charlie', 'David', 'Eva'],
    'Department': ['HR', 'Engineering', 'Engineering', 'Sales', 'HR'],
    'Salary': [50000, 85000, 92000, 45000, 52000],
    'Years_Experience': [2, 5, 7, 1, 3]
}

df = pd.DataFrame(data)

# 2. Basic Data Inspection
print("--- Full DataFrame ---")
print(df)

# 3. Filtering and Selecting
# Find all employees in Engineering with a salary over 90,000
high_paid_engineers = df[(df['Department'] == 'Engineering') & (df['Salary'] > 90000)]

# 4. Aggregation (Grouping)
# Calculate the average salary per department
avg_salary_by_dept = df.groupby('Department')['Salary'].mean()

# 5. Adding a new calculated column
# Give everyone a 10% bonus
df['Bonus'] = df['Salary'] * 0.10

print("\n--- Average Salary by Department ---")
print(avg_salary_by_dept)

print("\n--- DataFrame with Bonus Column ---")
print(df)