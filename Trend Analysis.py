import pandas as pd
import plotly.graph_objects as go
from plotly.subplots import make_subplots

# Sample DataFrame creation (you will replace this with loading your actual data)
data = {
    'Week': [i for i in range(1, 53)],
    'Total Tires Produced': [1000 + (i % 10 * 100) - (i % 15 * 50) for i in range(52)],  # Sample data
    'Defect Rate (%)': [2 + (i % 5) for i in range(52)],  # Sample data
    'Machine Downtime (Hrs)': [1 + (i % 6) for i in range(52)],  # Sample data
}
df = pd.DataFrame(data)

# Create subplots
fig = make_subplots(rows=3, cols=1, 
                    subplot_titles=("Weekly Production Trends", "Defect Rate Trends", "Machine Downtime Trends"))

# Add Production Trends
fig.add_trace(go.Scatter(x=df['Week'], 
                         y=df['Total Tires Produced'], 
                         mode='lines+markers', 
                         name='Total Tires Produced',
                         line=dict(color='blue', width=2),
                         marker=dict(size=8)), 
              row=1, col=1)

# Add Defect Rate Trends
fig.add_trace(go.Scatter(x=df['Week'], 
                         y=df['Defect Rate (%)'], 
                         mode='lines+markers', 
                         name='Defect Rate (%)',
                         line=dict(color='red', width=2),
                         marker=dict(size=8)), 
              row=2, col=1)

# Add Machine Downtime Trends
fig.add_trace(go.Scatter(x=df['Week'], 
                         y=df['Machine Downtime (Hrs)'], 
                         mode='lines+markers', 
                         name='Machine Downtime (Hrs)',
                         line=dict(color='green', width=2),
                         marker=dict(size=8)), 
              row=3, col=1)

# Update layout
fig.update_layout(title='Weekly Production Analysis', 
                  xaxis_title='Week',
                  yaxis_title='Output',
                  height=800)

# Show the figure
fig.show()
