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
