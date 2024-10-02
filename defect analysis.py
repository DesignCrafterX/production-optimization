import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

# Data
weeks = np.arange(1, 53)
total_tires_produced = np.array([1000]*52)
defect_rate = np.array([2, 1, 3, 2, 4, 1, 3, 0, 2, 3, 2, 1, 2, 4, 2, 3, 2, 1, 3, 2, 0, 2, 3, 2, 4, 1, 3, 2, 0, 2, 3, 2, 1, 4, 2, 3, 1, 2, 3, 2, 1, 3, 2, 4, 2, 1, 2, 3, 2, 4, 1, 3])
material_cost = np.array([50000, 52000, 48000, 51000, 49500, 53000, 48000, 54000, 51000, 49000, 52000, 52500, 51500, 49000, 50500, 48000, 50000, 52000, 49500, 53000, 54000, 52000, 49000, 51000, 48000, 53000, 49500, 52000, 54000, 51000, 49500, 51000, 53000, 48000, 52000, 49000, 52500, 51500, 49500, 51000, 52000, 49000, 50500, 48000, 53000, 54000, 52000, 49000, 51000, 48000, 53000, 49500])
labor_cost = np.array([20000]*52)
total_cost = material_cost + labor_cost

# Root Cause Analysis: Highlighting weeks with high defect rates
high_defect_weeks = np.where(defect_rate > 3)[0] + 1

# Plot Defect Rate Over Time
plt.figure(figsize=(10, 6))
plt.plot(weeks, defect_rate, marker='o', label='Defect Rate (%)', color='orange')
plt.scatter(high_defect_weeks, defect_rate[high_defect_weeks - 1], color='red', label='High Defect Weeks', zorder=5)
plt.title('Defect Rate Over Time')
plt.xlabel('Weeks')
plt.ylabel('Defect Rate (%)')
plt.legend()
plt.grid(True)

# Plot Total Cost Over Time
plt.figure(figsize=(10, 6))
plt.plot(weeks, total_cost, marker='o', label='Total Production Cost (INR)', color='green')
plt.title('Total Production Cost Over Time')
plt.xlabel('Weeks')
plt.ylabel('Cost (INR)')
plt.legend()
plt.grid(True)

# Cost of Quality Analysis
rework_cost_per_defect = 100  # Assumed cost for reworking one defective tire
total_defects = (defect_rate / 100) * total_tires_produced
cost_of_quality = total_defects * rework_cost_per_defect

# Plot Cost of Quality Over Time
plt.figure(figsize=(10, 6))
plt.plot(weeks, cost_of_quality, marker='o', label='Cost of Quality (INR)', color='red')
plt.title('Cost of Quality Over Time')
plt.xlabel('Weeks')
plt.ylabel('Cost of Quality (INR)')
plt.legend()
plt.grid(True)

plt.tight_layout()
plt.show()

# Print Analysis Results
print(f"High Defect Weeks: {high_defect_weeks}")
print(f"Total Defects per Week: {total_defects}")
print(f"Cost of Quality per Week (INR): {cost_of_quality}")
