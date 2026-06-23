# NYC Taxi Trips Dataset Cleaning & Preprocessing

## 📌 Project Overview
This project demonstrates **data cleaning and preprocessing** techniques on the NYC Taxi Trips dataset.  
The dataset contains GPS coordinate errors, fare discrepancies, and missing passenger counts.  
The goal is to transform raw trip data into a **clean, standardized format** suitable for analytics.

---

## 🛠 Steps Performed
1. **Data Ingestion** – Loaded dataset using Pandas.
2. **Deduplication** – Removed duplicate trip records.
3. **Missing Values** – Filled missing passenger counts, dropped rows with missing trip IDs.
4. **Date Standardization** – Converted pickup/dropoff datetime into proper format.
5. **GPS Coordinate Cleaning** – Validated latitude/longitude ranges.
6. **Fare Cleaning** – Removed negative, zero, and unrealistic fare values.
7. **Validation** – Ensured no duplicates or missing IDs remain.
8. **Export** – Saved cleaned dataset as `cleaned_nyc_taxi.csv`.

---

## 📂 Files in Repository
- `nyc_taxi.csv` → Raw dataset (sample for practice)  
- `nyc_taxi_cleaning.py` → Python script with cleaning workflow  
- `cleaned_nyc_taxi.csv` → Final cleaned dataset  
- `README.md` → Project documentation  

---

## 🎯 Outcome
The final dataset is **clean, consistent, and analysis-ready**, enabling reliable insights such as trip demand analysis, fare distribution, and passenger trends.

---

## 🚀 Skills Demonstrated
- Python (Pandas, NumPy)  
- Data cleaning & preprocessing  
- Handling missing values & duplicates  
- GPS coordinate validation  
- Outlier detection in fares  
- Professional project documentation
