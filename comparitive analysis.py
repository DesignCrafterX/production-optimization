import pandas as pd
import plotly.graph_objects as go
from plotly.subplots import make_subplots

# Data provided
data = {
    'Week': list(range(1, 53)),
    'Total Tires Produced': [1000] * 52,
    'Defect Rate (%)': [2, 1, 3, 2, 4, 1, 3, 0, 2, 3, 2, 1, 2, 4, 2, 3, 2, 1, 3, 2, 0, 2, 3, 2, 4, 1, 3, 2, 0, 2, 3, 2, 1, 4, 2, 3, 1, 2, 3, 2, 1, 3, 2, 4, 2, 1, 2, 3, 4, 1, 3, 2],
    'Machine Downtime (hrs)': [5, 4, 6, 3, 7, 2, 8, 1, 4, 5, 3, 4, 2, 6, 5, 7, 3, 4, 6, 2, 1, 4, 5, 3, 8, 2, 6, 3, 1, 4, 5, 3, 2, 6, 3, 5, 4, 2, 6, 3, 4, 5, 3, 6, 2, 1, 4, 5, 8, 2, 4, 5],
    'Production Efficiency (%)': [90, 92, 85, 88, 82, 95, 80, 98, 91, 87, 89, 92, 93, 81, 90, 83, 88, 92, 85, 94, 98, 90, 86, 89, 80, 95, 84, 90, 97, 91, 86, 88, 95, 82, 89, 87, 92, 93, 84, 88, 92, 86, 90, 81, 94, 97, 90, 85, 89, 80, 95, 86],
    'Labor Hours': [160] * 52,
    'Material Cost (INR)': [50000, 52000, 48000, 51000, 49500, 53000, 48000, 54000, 51000, 49000, 52000, 52500, 51500, 49000, 50500, 48000, 50000, 52000, 49500, 53000, 54000, 52000, 49000, 51000, 48000, 53000, 49500, 52000, 54000, 51000, 49500, 51000, 53000, 48000, 52000, 49000, 52500, 51500, 49500, 51000, 52000, 49000, 50500, 48000, 53000, 54000, 52000, 49000, 51000, 48000, 53000, 49500],
    'Labor Cost (INR)': [20000] * 52,
    'Total Cost (INR)': [70000, 72000, 68000, 71000, 69500, 73000, 68000, 74000, 71000, 69000, 72000, 72500, 71500, 69000, 70500, 68000, 70000, 72000, 69500, 73000, 74000, 72000, 69000, 71000, 68000, 73000, 69500, 72000, 74000, 71000, 69500, 71000, 73000, 68000, 72000, 69000, 72500, 71500, 69500, 71000, 72000, 69000, 70500, 68000, 73000, 74000, 72000, 69000, 71000, 68000, 73000, 69500],
    'Revenue (INR)': [100000] * 52
}

# Creating DataFrame
df = pd.DataFrame(data)

# Calculate averages for each metric
average_defect_rate = df['Defect Rate (%)'].mean()
average_machine_downtime = df['Machine Downtime (hrs)'].mean()
average_production_efficiency = df['Production Efficiency (%)'].mean()
average_total_cost = df['Total Cost (INR)'].mean()
average_revenue = df['Revenue (INR)'].mean()

# Identify best and worst weeks based on Total Tires Produced
best_week = df.loc[df['Total Tires Produced'].idxmax()]
worst_week = df.loc[df['Defect Rate (%)'].idxmax()]

# Output averages and best/worst weeks
print("Average Defect Rate (%):", average_defect_rate)
print("Average Machine Downtime (hrs):", average_machine_downtime)
print("Average Production Efficiency (%):", average_production_efficiency)
print("Average Total Cost (INR):", average_total_cost)
print("Average Revenue (INR):", average_revenue)
print("\nBest Week (Total Tires Produced):", best_week)
print("Worst Week (Defect Rate %):", worst_week)

# Visualizing the results
fig = make_subplots(rows=2, cols=2,
                    subplot_titles=("Defect Rate Analysis", "Production Efficiency Analysis", "Total Cost vs Revenue", "Machine Downtime Analysis"),
                    vertical_spacing=0.1)

# Subplot 1: Defect Rate Analysis
fig.add_trace(go.Scatter(x=df['Week'], y=df['Defect Rate (%)'], mode='lines+markers', name='Defect Rate (%)', line=dict(color='red')),
              row=1, col=1)
fig.update_yaxes(title_text="Defect Rate (%)", row=1, col=1)

# Subplot 2: Production Efficiency Analysis
fig.add_trace(go.Scatter(x=df['Week'], y=df['Production Efficiency (%)'], mode='lines+markers', name='Production Efficiency (%)', line=dict(color='green')),
              row=1, col=2)
fig.update_yaxes(title_text="Production Efficiency (%)", row=1, col=2)

# Subplot 3: Total Cost vs Revenue
fig.add_trace(go.Scatter(x=df['Week'], y=df['Total Cost (INR)'], mode='lines+markers', name='Total Cost (INR)', line=dict(color='orange')),
              row=2, col=1)
fig.add_trace(go.Scatter(x=df['Week'], y=df['Revenue (INR)'], mode='lines+markers', name='Revenue (INR)', line=dict(color='blue')),
              row=2, col=1)
fig.update_yaxes(title_text="Cost / Revenue (INR)", row=2, col=1)

# Subplot 4: Machine Downtime Analysis
fig.add_trace(go.Scatter(x=df['Week'], y=df['Machine Downtime (hrs)'], mode='lines+markers', name='Machine Downtime (hrs)', line=dict(color='purple')),
              row=2, col=2)
fig.update_yaxes(title_text="Machine Downtime (hrs)", row=2, col=2)

# Update x-axis titles
fig.update_xaxes(title_text="Weeks", row=1, col=1)
fig.update_xaxes(title_text="Weeks", row=1, col=2)
fig.update_xaxes(title_text="Weeks", row=2, col=1)
fig.update_xaxes(title_text="Weeks", row=2, col=2)

# Display the dashboard
fig.show()
