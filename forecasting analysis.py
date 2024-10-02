import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LinearRegression
import numpy as np
import matplotlib.pyplot as plt

# Historical data
data = {
    "Week": np.arange(1, 53),
    "Total_Tires_Produced": [1000] * 52,
    "Defect_Rate": [2, 1, 3, 2, 4, 1, 3, 0, 2, 3, 2, 1, 2, 4, 2, 3, 2, 1, 3, 2, 0, 2, 3, 2, 4, 1, 3, 2, 0, 2, 3, 2, 1, 4, 2, 3, 1, 2, 3, 1, 2, 3, 1, 3, 2, 4, 1, 2, 3, 4, 1, 3],
    "Machine_Downtime": [5, 4, 6, 3, 7, 2, 8, 1, 4, 5, 3, 4, 2, 6, 5, 7, 3, 4, 6, 2, 1, 4, 5, 3, 8, 2, 6, 3, 1, 4, 5, 3, 2, 6, 3, 5, 4, 2, 6, 3, 4, 5, 4, 5, 7, 1, 4, 5, 3, 8, 2, 5],
    "Production_Efficiency": [90, 92, 85, 88, 82, 95, 80, 98, 91, 87, 89, 92, 93, 81, 90, 83, 88, 92, 85, 94, 98, 90, 86, 89, 80, 95, 84, 90, 97, 91, 86, 88, 95, 82, 89, 92, 93, 84, 88, 92, 86, 90, 81, 94, 97, 90, 85, 89, 80, 95, 86, 86]
}

# Create DataFrame
df = pd.DataFrame(data)

# Features and target variable
X = df[["Defect_Rate", "Machine_Downtime", "Production_Efficiency"]]
y = df["Total_Tires_Produced"]

# Split the data into training and testing sets
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

# Create and train the model
model = LinearRegression()
model.fit(X_train, y_train)

# Make predictions for the next 10 weeks
future_weeks = pd.DataFrame({
    "Defect_Rate": [1, 2, 1, 3, 2, 1, 2, 3, 2, 1],  # Example future defect rates
    "Machine_Downtime": [2, 3, 2, 4, 3, 2, 2, 3, 2, 2],  # Example future downtimes
    "Production_Efficiency": [95, 90, 92, 91, 93, 94, 90, 92, 91, 90]  # Example future efficiencies
})

predictions = model.predict(future_weeks)

# Combine historical and predicted data for visualization
predicted_weeks = np.arange(53, 63)
predicted_df = pd.DataFrame({
    "Week": predicted_weeks,
    "Total_Tires_Produced": predictions
})

# Plotting
plt.figure(figsize=(12, 6))

# Historical data
plt.plot(df["Week"], df["Total_Tires_Produced"], label='Historical Production', marker='o')

# Predicted data
plt.plot(predicted_df["Week"], predicted_df["Total_Tires_Produced"], label='Predicted Production', marker='o', linestyle='--', color='orange')

# Adding titles and labels
plt.title('Tire Production Forecast')
plt.xlabel('Week')
plt.ylabel('Total Tires Produced')
plt.xticks(np.arange(1, 64, 2))  # Show ticks for each week
plt.axhline(y=1000, color='r', linestyle='--', label='Target Production Level')
plt.legend()
plt.grid()
plt.show()

# Output predictions
for week, prediction in zip(predicted_weeks, predictions):
    print(f"Week {week}: Predicted Total Tires Produced = {prediction:.2f}")
