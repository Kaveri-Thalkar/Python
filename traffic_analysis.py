import pandas as pd
import os

# Get the directory where this script is located
base_path = os.path.dirname(__file__)

# Create full path to CSV file
file_path = os.path.join(base_path, "traffic_data.csv")

# Load dataset
df = pd.read_csv(file_path)

print("\n--- Traffic Data ---")
print(df)

# Find location with highest traffic
max_traffic = df.loc[df["Vehicle_Count"].idxmax()]
print("\nHighest Traffic Location:")
print(max_traffic)

# Average vehicle count per location
avg_traffic = df.groupby("Location")["Vehicle_Count"].mean()
print("\nAverage Traffic Per Location:")
print(avg_traffic)

# Detect congestion (Speed < 25 = High Traffic)
df["Congestion_Level"] = df["Average_Speed"].apply(
    lambda x: "High" if x < 25 else "Normal"
)

print("\nUpdated Data With Congestion Level:")
print(df)

# Save report in same folder
output_path = os.path.join(base_path, "report_output.csv")
df.to_csv(output_path, index=False)

print("\nReport Saved Successfully!")