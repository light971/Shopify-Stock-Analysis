📊 Shopify Stock Data Analytics Project — End-to-End (Python • SQL • Power BI)

⭐ Project Overview

This project is a complete Data Analyst case study, based on the Kaggle dataset Shopify Stock Data 2025. It demonstrates a full end-to-end analytics workflow, from raw data to interactive dashboard.

🎯 Goal: Build a clean, simple, and professional pipeline suitable for a data analytics portfolio.

➡️ Skills demonstrated:
	•	Data cleaning & preparation (Python)
	•	Financial KPI creation (Python & DAX)
	•	Analytical SQL queries
	•	Power BI dashboard design (Z-pattern, BI UX best practices)
	•	Business storytelling & insights

⸻

🏷️ Badges


⸻

📚 Table of Contents
	1.	Context & Objectives￼
	2.	Project Structure￼
	3.	Full Pipeline￼
	4.	KPIs & Analysis￼
	5.	Power BI Dashboard￼
	6.	Key Business Insights￼
	7.	Installation & Execution￼
	8.	Tech Stack￼
	9.	Author￼

⸻

🎯 Context & Objectives

Shopify is a publicly traded company whose stock fluctuates depending on market conditions. The purpose of this project is to:
	•	Analyze stock price movements across 2025.
	•	Identify trends and volatility.
	•	Highlight short-term market signals (daily change, moving averages, etc.).
	•	Produce a simple, educational dashboard for investors.

⸻

📂 Project Structure
```
│
├── data/
│   ├── raw/             # Raw data
│   ├── processed/       # Cleaned data
│   └── external/        # External datasets
│
├── notebooks/
│   ├── 0.0-data-cleaning.ipynb
│   ├── 1.0-data-analysis.ipynb
│   
│
├── reports/
│   ├── dashborads/
│   ├── figures/
│   └── summary/
│
├── src/
│   ├── data_cleaning.py
│   ├── data_analysis.py
│   └── data_visualization.py
│
├── config.py
├── requirements.txt
└── README.md
```

⸻

🔄 Full Pipeline

1️⃣ Data Cleaning (Python)
	•	Date parsing and formatting
	•	Duplicate removal
	•	Numeric column validation
	•	Export to tidy CSV → data/processed/

2️⃣ Analysis & KPIs (Python + SQL)

Financial KPIs built:
	•	Daily Change %
	•	7-Day Trend %
	•	Volatility (STD)
	•	High/Low Range
	•	Moving Average (Close)

SQL queries included:
	•	Monthly volatility
	•	Top gain/loss days
	•	Statistical summaries

3️⃣ Visualization (Power BI)

Dashboard designed following:
	•	Z-pattern visual reading
	•	Clear KPI hierarchy
	•	Consistent color logic (green = gain, red = loss)

⸻

📈 Power BI Dashboard

Top section — KPIs (instant reading)
	•	Close Price
	•	Daily Change %
	•	7D Trend %
	•	Volatility

Middle section — Time-series analysis
	•	Close Price Over Time (line chart)
	•	Daily % Change (column chart)

Bottom section — Additional metrics
	•	Trading Volume
	•	High vs Low

Color palette (optimized for finance):
	•	Green: #27AE60
	•	Red: #EB5757
	•	Blue: #2F80ED
	•	Grey: #BDBDBD

⸻

💡 Key Business Insights

The dashboard highlights the following takeaways:
	•	📉 High volatility observed during specific periods → indicates increased speculative activity.
	•	🔄 Strong alternation between positive and negative days → market highly reactive to news.
	•	📈 7-day trend reveals micro-cycles useful for short-term traders.
	•	🟦 High/Low price range shows market pressure from buyers vs sellers.

These insights help track key stock dynamics in a simplified format.

⸻

🛠 Installation & Execution

pip install -r requirements.txt

	1.	Add raw data to data/raw/
	2.	Run 0.0-data-cleaning.ipynb
	3.	Run 1.0-data-analysis.ipynb
	4.	Import processed CSVs into Power BI

⸻

🧰 Tech Stack
	•	Python (Pandas / Numpy / Matplotlib)
	•	SQL (SQLite / DuckDB)
	•	Power BI
	•	Jupyter Notebook
	•	Git & GitHub

⸻

👤 Author

Project created by Malcom, Marketing Data Analyst.
