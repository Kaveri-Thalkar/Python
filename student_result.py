import pandas as pd

# Student Data
data = {
    "Name": ["Rahul", "Priya", "Amit", "Sneha", "Rohan"],
    "Maths": [85, 90, 78, 92, 88],
    "Science": [80, 95, 70, 89, 84],
    "English": [75, 88, 72, 94, 79]
}

# Create DataFrame
df = pd.DataFrame(data)

# Calculate Total
df["Total"] = df["Maths"] + df["Science"] + df["English"]

# Calculate Average
df["Average"] = df["Total"] / 3

# Grade Function
def grade(avg):
    if avg >= 90:
        return "A+"
    elif avg >= 80:
        return "A"
    elif avg >= 70:
        return "B"
    else:
        return "C"

# Apply Grade
df["Grade"] = df["Average"].apply(grade)

# Display Data
print("\nStudent Result Data:\n")
print(df)

# Save to CSV
df.to_csv("student_results.csv", index=False)

print("\nCSV File Saved Successfully!")