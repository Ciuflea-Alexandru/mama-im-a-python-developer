# calculate basic descriptive statistics from a list

import statistics

scores = [85, 92, 78, 90, 88, 76, 95, 89, 100, 82]

def calculate_stats(data):
    mean_val = statistics.mean(data)
    median_val = statistics.median(data)
    stdev_val = statistics.stdev(data)
    
    print(f"Dataset: {data}")
    print("-" * 20)
    print(f"Mean (Average):      {mean_val:.2f}")
    print(f"Median (Middle):     {median_val}")
    print(f"Standard Deviation:  {stdev_val:.2f}")

if __name__ == "__main__":
    calculate_stats(scores)