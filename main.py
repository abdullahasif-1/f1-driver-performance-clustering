import fastf1
import os
import pandas as pd
from sklearn.preprocessing import StandardScaler
from sklearn.cluster import KMeans
import matplotlib.pyplot as plt

CACHE_DIR = "cache"
os.makedirs(CACHE_DIR, exist_ok=True)
fastf1.Cache.enable_cache(CACHE_DIR)

year = int(input("Enter year (e.g. 2023): "))
gp_name = input("Enter GP name (e.g. Monza, Silverstone, Abu Dhabi): ")

session = fastf1.get_session(year, gp_name, "R")
session.load()

laps = session.laps
laps = laps.pick_quicklaps()

drivers = laps["Driver"].unique()
data = []

for drv in drivers:
    drv_laps = laps.pick_driver(drv)
    if len(drv_laps) < 5:
        continue

    avg_lap = drv_laps["LapTime"].dt.total_seconds().mean()
    std_lap = drv_laps["LapTime"].dt.total_seconds().std()
    stint_count = drv_laps["Stint"].nunique()

    soft = (drv_laps["Compound"] == "SOFT").mean()
    medium = (drv_laps["Compound"] == "MEDIUM").mean()
    hard = (drv_laps["Compound"] == "HARD").mean()

    data.append([drv, avg_lap, std_lap, stint_count, soft, medium, hard])

df = pd.DataFrame(data, columns=["Driver", "AvgLap", "LapStd", "StintCount", "Soft%", "Medium%", "Hard%"])

X = df.drop("Driver", axis=1)
scaler = StandardScaler()
X_scaled = scaler.fit_transform(X)

kmeans = KMeans(n_clusters=3, random_state=42, n_init=10)
df["Cluster"] = kmeans.fit_predict(X_scaled)

cluster_means = df.groupby("Cluster")["AvgLap"].mean().sort_values()
cluster_names = {}

for i, cluster_id in enumerate(cluster_means.index):
    if i == 0:
        cluster_names[cluster_id] = "Front-Runners"
    elif i == 1:
        cluster_names[cluster_id] = "Midfield"
    else:
        cluster_names[cluster_id] = "Backmarkers"

df["ClusterName"] = df["Cluster"].map(cluster_names)

driver_input = input("Enter driver code (e.g. VER, HAM, LEC): ").upper()\

if driver_input in df["Driver"].values:
    cluster_name = df.loc[df["Driver"] == driver_input, "ClusterName"].values[0]
    print("Driver " + driver_input + " belongs to " + cluster_name)
else:
    print("Driver not found in this race.")

plt.figure(figsize=(8, 6))
for cname in df["ClusterName"].unique():
    cluster_data = df[df["ClusterName"] == cname]
    plt.scatter(cluster_data["AvgLap"], cluster_data["LapStd"], label=cname)

for i, row in df.iterrows():
    plt.text(row["AvgLap"], row["LapStd"], row["Driver"], fontsize=8)

plt.xlabel("Average Lap Time (s)")
plt.ylabel("Lap Time Consistency (Std Dev)")
plt.title("Driver Clustering " + str(year) + str(gp_name) + " GP")
plt.legend()
plt.show()
