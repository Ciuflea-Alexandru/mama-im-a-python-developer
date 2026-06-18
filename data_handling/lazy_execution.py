# load data, perform lazy transformations, and execute complex aggregations

import polars as pl

# 1. Create a sample DataFrame
data = {
    "employee": ["Alice", "Bob", "Charlie", "David", "Eve"],
    "department": ["IT", "HR", "IT", "Sales", "HR"],
    "salary": [85000, 60000, 95000, 70000, 62000],
    "years_exp": [5, 2, 8, 3, 4]
}

df = pl.DataFrame(data)

# 2. Lazy Evaluation (Efficient Querying)
# We chain operations, and Polars optimizes the execution plan before running it.
result = (
    df.lazy()
    .filter(pl.col("salary") > 60000)
    .group_by("department")
    .agg([
        pl.col("salary").mean().alias("avg_salary"),
        pl.col("employee").count().alias("num_employees")
    ])
    .sort("avg_salary", descending=True)
    .collect() # The query is executed here
)

print("Aggregated Results:")
print(result)

# 3. Handling missing data or complex transformations
# Example: Adding a bonus column
df_with_bonus = df.with_columns(
    (pl.col("salary") * 0.1).alias("bonus")
)

print("\nData with Bonus calculation:")
print(df_with_bonus)