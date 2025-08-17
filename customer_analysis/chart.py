# 22f3002903@ds.study.iitm.ac.in

import seaborn as sns
import matplotlib.pyplot as plt
import pandas as pd
import numpy as np

# -----------------------------
# 1. Generate Synthetic Data
# -----------------------------
np.random.seed(42)

# Create a range of months (24 months for 2 years)
months = pd.date_range(start="2023-01-01", periods=24, freq="M")

# Define customer segments
segments = ["New Customers", "Returning Customers", "Loyal Customers"]

# Create synthetic revenue data with some seasonality & growth patterns
data = []
for month in months:
    for segment in segments:
        base = 10000 if segment == "New Customers" else 20000 if segment == "Returning Customers" else 30000
        seasonal = 5000 * np.sin((month.month / 12) * 2 * np.pi)  # seasonal effect
        growth = (month.year - 2023) * 2000  # yearly growth
        noise = np.random.normal(0, 2000)  # randomness
        revenue = base + seasonal + growth + noise
        data.append([month, segment, max(0, revenue)])  # ensure non-negative

# Create DataFrame
df = pd.DataFrame(data, columns=["Month", "CustomerSegment", "Revenue"])

# -----------------------------
# 2. Visualization with Seaborn
# -----------------------------
sns.set_style("whitegrid")
sns.set_context("talk")

fig, ax = plt.subplots(figsize=(8, 8))  # ensures 8x8 inches

sns.lineplot(
    data=df,
    x="Month",
    y="Revenue",
    hue="CustomerSegment",
    palette="Set2",
    linewidth=2.5,
    ax=ax
)

# Add title and labels
ax.set_title("Monthly Revenue Trend by Customer Segment", fontsize=18, weight="bold")
ax.set_xlabel("Month", fontsize=14)
ax.set_ylabel("Revenue ($)", fontsize=14)
ax.legend(title="Customer Segment", loc="upper left")

# -----------------------------
# 3. Save Chart as PNG (512x512)
# -----------------------------
plt.savefig("chart.png", dpi=64)  # removed bbox_inches to keep 512x512 exact
plt.close()
