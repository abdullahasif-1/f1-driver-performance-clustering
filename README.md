# 🏎️ F1 Driver Performance Clustering

This project uses the **[FastF1 API](https://theoehrly.github.io/Fast-F1/)** and **machine learning (K-Means)** to analyze Formula 1 race data and cluster drivers based on their **lap performance and strategy**.  

The tool automatically downloads race telemetry, computes driver statistics, and groups drivers into meaningful categories like **Front-Runners 🏆, Midfield 🚗, and Backmarkers 🐢**.  

---

## 🔧 Features
- Fetch race data from **FastF1** with caching.  
- Compute driver performance metrics:
  - Average lap time  
  - Consistency (lap time standard deviation)  
  - Stint count  
  - Tire compound usage (Soft, Medium, Hard %)  
- Perform **K-Means clustering** on drivers.  
- Auto-label clusters with intuitive names:
  - 🏆 Front-Runners (fastest average lap times)  
  - 🚗 Midfield (competitive but less consistent)  
  - 🐢 Backmarkers (slower average pace)  
- Interactive prediction:
  - Enter a driver’s name/code (e.g., `VER`, `Verstappen`, `Max`)  
  - See which cluster they belong to (with full name in output).  
- Visualization:
  - Scatter plot of **Average Lap Time vs Consistency**, with clusters highlighted.  

---

## 📊 Example
📊 Driver Stats - 2023 Abu Dhabi GP
Driver AvgLap LapStd StintCount Soft% Medium% Hard%
VER 87.21 0.35 2 0.6 0.4 0.0
HAM 88.15 0.41 3 0.5 0.5 0.0
...

🏎️ Clustering Results - 2023 Abu Dhabi GP
Driver ClusterName
VER Front-Runners 🏆
HAM Midfield 🚗
LEC Front-Runners 🏆
STR Backmarkers 🐢
...

🔮 Prediction: Max Verstappen (VER) belongs to 'Front-Runners 🏆'
