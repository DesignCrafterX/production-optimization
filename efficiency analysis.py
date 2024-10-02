import numpy as np
import matplotlib.pyplot as plt
import pandas as pd

# Data
weeks = np.arange(1, 53)
total_tires_produced = 1000
defect_rate = np.array([2, 1, 3, 2, 4, 1, 3, 0, 2, 3, 2, 1, 2, 4, 2, 3, 2, 1, 3, 2, 0, 2, 3, 2, 4, 1, 3, 2, 0, 2, 3, 2, 1, 4, 2, 3, 1, 2, 3, 2, 1, 3, 2, 4, 2, 1, 2, 3, 2, 4, 1, 3])
machine_downtime = np.array([5, 4, 6, 3, 7, 2, 8, 1, 4, 5, 3, 4, 2, 6, 5, 7, 3, 4, 6, 2, 1, 4, 5, 3, 8, 2, 6, 3, 1, 4, 5, 3, 2, 6, 3, 5, 4, 2, 6, 3, 4, 5, 3, 7, 2, 1, 4, 5, 3, 8, 2, 5])
production_efficiency = np.array([90, 92, 85, 88, 82, 95, 80, 98, 91, 87, 89, 92, 93, 81, 90, 83, 88, 92, 85, 94, 98, 90, 86, 89, 80, 95, 84, 90, 97, 91, 86, 88, 95, 82, 89, 87, 92, 93, 84, 88, 92, 86, 90, 81, 94, 97, 90, 85, 89, 80, 95, 86])
labor_hours = 160
labor_cost = np.array([20000]*52)

# Average production efficiency
avg_efficiency = np.mean(production_efficiency)

# Labor productivity (output per labor hour)
labor_productivity = total_tires_produced / labor_hours

# Visualization
plt.figure(figsize=(14, 8))

# Production Efficiency Over Time
plt.subplot(2, 1, 1)
plt.plot(weeks, production_efficiency, marker='o', label='Production Efficiency (%)', color='blue')
plt.axhline(avg_efficiency, color='red', linestyle='--', label=f'Average Efficiency ({avg_efficiency:.2f}%)')
plt.title('Production Efficiency Over Time')
plt.xlabel('Weeks')
plt.ylabel('Production Efficiency (%)')
plt.legend()

# Machine Downtime and Defect Rate
plt.subplot(2, 1, 2)
plt.plot(weeks, machine_downtime, marker='o', label='Machine Downtime (hrs)', color='green')
plt.plot(weeks, defect_rate, marker='x', label='Defect Rate (%)', color='orange')
plt.title('Machine Downtime and Defect Rate Over Time')
plt.xlabel('Weeks')
plt.ylabel('Values')
plt.legend()

plt.tight_layout()
plt.show()

# Print Analysis Results
print(f"Average Production Efficiency: {avg_efficiency:.2f}%")
print(f"Labor Productivity: {labor_productivity:.2f} tires produced per labor hour")
