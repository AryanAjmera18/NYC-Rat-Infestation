
# 🪤 NYC Rodent Inspection Data Analytics and Dashboard

## 👥 Team Members
- **Aryan Ajmera** (`aa12904`)
- **Utkarsh Mittal** (`um2113`)
- **Rushabh Bhat** (`rb5726`)

**Semester Term:** Spring 2025  

---

## 📋 Table of Contents
1. [Executive Summary](#1-executive-summary)
2. [Code Execution Instructions](#2-code-execution-instructions)
3. [Technological Challenges](#3-technological-challenges)
4. [Changes in Technology](#4-changes-in-technology)
5. [Uncovered Aspects from Presentation](#5-uncovered-aspects-from-presentation)
6. [Lessons Learned](#6-lessons-learned)
7. [Future Improvements](#7-future-improvements)
8. [Data Sources and Results](#8-data-sources-and-results)

---

## 1️⃣ Executive Summary

**Project Name:** NYC Rodent Inspection Data Analytics and Dashboard  

### Brief Summary
This project involves designing and deploying an interactive dashboard to analyze rodent inspection data across New York City. The dashboard provides actionable insights on rodent inspections from **2009 to 2025**.

### Objectives
- Process large-scale rodent inspection data
- Build a real-time interactive dashboard for visualization
- Provide borough-level trends and patterns

### Technologies Used
- Apache Spark (PySpark)
- Streamlit
- Pandas
- Folium + Streamlit-Folium
- Matplotlib

---

## 2️⃣ Code Execution Instructions

### Repository  
[👉 Link to GitHub Repository (insert your link here)]  

### High-Level Code Logic
```bash
1. Preprocess raw CSV data:
   python src/etl/process_rodent_data.py           --input data/raw/rodent_inspections.csv           --output data/processed/rodent_inspections.parquet

2. Subset data for Tableau export:
   python dashboards/export.py

3. Launch the Streamlit dashboard:
   streamlit run src/app/streamlit_app.py
```

Refer to the full [README section in your repo](insert-link-here).

---

## 3️⃣ Technological Challenges

- **Windows Hadoop errors:** Resolved by disabling native Hadoop IO (`spark.hadoop.io.nativeio.enabled=false`)
- **Memory overload:** Limited dataset to 2009–2025; optimized Spark partitions
- **Slow map rendering:** Removed heavy clustering map for faster interactivity

---

## 4️⃣ Changes in Technology

We initially planned to use only Tableau.  
**Streamlit was added** to enable:
- Real-time filtering
- Better interactivity
- Lighter deployment without Tableau Server

This greatly improved usability and insights.

---

## 5️⃣ Uncovered Aspects from Presentation

Due to time constraints, we couldn’t demo:
- `dashboards/export.py` pipeline for Tableau export
- Streamlit + Folium maps (which enhanced map interactivity)

### 📸 Example Screenshots
*(Add your own images here)*  
`![Heatmap Example](path/to/image.png)`  
`![Dashboard Filters](path/to/image.png)`

---

## 6️⃣ Lessons Learned

### What Worked Well
- Combining Spark + Streamlit provided a scalable + interactive solution

### Challenges Faced
- Local memory limits on laptops
- Schema mismatches in raw data

### Solutions
- Filtering to 2009–2025 range
- Added schema validation and structured logging

---

## 7️⃣ Future Improvements

If we had more time, we would:
- Add Spark Structured Streaming for live data
- Deploy fully inside Docker on cloud
- Add advanced clustering & predictive ML models

---

## 8️⃣ Data Sources and Results

### 📊 Data Source
[NYC Open Data Rodent Inspection Dataset (2009–2025)](https://data.cityofnewyork.us/Health/Rodent-Inspection/p937-wjvj)

### 📈 Results
- Heatmap of rodent inspections by borough
- Monthly bar chart of inspections
- Yearly trend line chart
- Pie chart of inspection results

### 📋 Key Observations
- Brooklyn & Manhattan show highest rodent activity
- Peak rodent inspection activity in mid-2010s

### Repository
(https://github.com/AryanAjmera18/NYC-Rat-Infestation)

---

This README serves as the official documentation for the **NYC Rodent Inspection Data Analytics and Dashboard** project for Spring 2025 🎉
