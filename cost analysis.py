import pandas as pd
import plotly.graph_objects as go

# Sample Data
data = {
    'Week': list(range(1, 53)),
    'Total Tires Produce': [1000]*52,
    'Defect Rate (%)': [2]*52,
    'Machine Downtime (hrs)': [0]*52,
    'Products on Efficiency (%)': [95]*52,
    'Labor Hours': [160]*52,
    'Material Cost (INR)': [50000 + i*1000 for i in range(52)],
    'Labor Cost (INR)': [20000]*52,
    'Total Cost (INR)': [70000 + i*1000 for i in range(52)],
    'Revenue (INR)': [100000]*52,
}

df = pd.DataFrame(data)

# 1. Calculate Cost per Tire
df['Cost per Tire (INR)'] = df['Total Cost (INR)'] / df['Total Tires Produce']

# 2. Analyze Material vs. Labor Costs
df['Material Cost Proportion (%)'] = (df['Material Cost (INR)'] / df['Total Cost (INR)']) * 100
df['Labor Cost Proportion (%)'] = (df['Labor Cost (INR)'] / df['Total Cost (INR)']) * 100

# 3. Cost Trends Visualization
fig1 = go.Figure()
fig1.add_trace(go.Scatter(x=df['Week'], y=df['Total Cost (INR)'], mode='lines+markers', name='Total Cost (INR)'))
fig1.add_trace(go.Scatter(x=df['Week'], y=df['Cost per Tire (INR)'], mode='lines+markers', name='Cost per Tire (INR)'))
fig1.update_layout(title='Cost Trends Over the Year', xaxis_title='Week', yaxis_title='Cost (INR)')

# 4. Material vs Labor Costs Proportion Visualization
fig2 = go.Figure()
fig2.add_trace(go.Scatter(x=df['Week'], y=df['Material Cost Proportion (%)'], mode='lines+markers', name='Material Cost Proportion (%)'))
fig2.add_trace(go.Scatter(x=df['Week'], y=df['Labor Cost Proportion (%)'], mode='lines+markers', name='Labor Cost Proportion (%)'))
fig2.update_layout(title='Material vs Labor Cost Proportion', xaxis_title='Week', yaxis_title='Proportion (%)')

# Show the figures
fig1.show()
fig2.show()
