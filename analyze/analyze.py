import pandas as pd
import matplotlib.pyplot as plt

df = pd.read_csv("<FILE_PATH>.csv")

# Placeholder for the desired maximum time cutoff
threshold = 60000+945  # Example threshold; adjust to the time cutoff you want. Depends on factors explained in READ.md file

# Filter rows: Keep only those where time_ms <= threshold
df = df[df["time_ms"] <= threshold].copy()

# Convert columns to numeric (in case they are read as strings)
df["time_ms"] = pd.to_numeric(df["time_ms"], errors='coerce')
df["avg_fps"] = pd.to_numeric(df["avg_fps"], errors='coerce')

# Drop rows with null values
df.dropna(subset=["time_ms", "avg_fps"], inplace=True)

# Outliers
Q1 = df["avg_fps"].quantile(0.25)
Q3 = df["avg_fps"].quantile(0.75)
IQR = Q3 - Q1
lower_bound = Q1 - 1.5 * IQR
upper_bound = Q3 + 1.5 * IQR

outliers = df[(df["avg_fps"] < lower_bound) | (df["avg_fps"] > upper_bound)]
non_outliers = df[(df["avg_fps"] >= lower_bound) & (df["avg_fps"] <= upper_bound)]

# Calculate the mean average FPS
overall_mean_fps = df["avg_fps"].mean()

# Plotting
plt.figure(figsize=(10, 6))

# Scatter plot of non-outlier and outlier data. This way better visualize outlier points directly from the scatter plot diagram
plt.scatter(non_outliers["time_ms"], non_outliers["avg_fps"], 
            label="Data", color="blue", s=10)
plt.scatter(outliers["time_ms"], outliers["avg_fps"], 
            label="Outliers", color="red", s=10)

# Horizontal line for overall average FPS
plt.axhline(y=overall_mean_fps, color='green', linewidth=2, 
            linestyle='--', label=f"Mean FPS = {overall_mean_fps:.2f}")

# Force the x-axis to start at the earliest time in the filtered data
x_min = df["time_ms"].min()
x_max = df["time_ms"].max()
plt.xlim([x_min, x_max])

plt.title("Average FPS Over Time (Time <= 60945ms)")
plt.xlabel("Time (ms)")
plt.ylabel("Average FPS")
plt.legend()
plt.grid(True)
plt.show()
