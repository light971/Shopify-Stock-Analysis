# 📈 Shopify Stock Analysis  
**Data Cleaning • Exploratory Data Analysis • SQL • KPIs • Power BI Dashboard**

This project showcases a complete end-to-end data analysis workflow using real stock market data from Shopify (SHOP).  
It was designed to demonstrate strong skills in **data wrangling, statistical analysis, SQL querying, data visualization, and BI reporting**.

This repository is ideal for recruiters, hiring managers, or anyone evaluating my ability to deliver structured, clear, and business-oriented data insights.

---

## ⭐ Project Highlights

- ✔️ Cleaned and transformed raw stock market data  
- ✔️ Built KPIs such as **Daily Return**, **7-Day Trend**, **High/Low Price Range**, **Volatility**, and **Moving Averages**  
- ✔️ Performed SQL analysis for descriptive statistics and market behavior  
- ✔️ Designed a **professional Power BI dashboard** for clear storytelling  
- ✔️ Structured the entire project with a scalable and production-like folder architecture  

---

## 🎯 Objectives

The goal of this project is to:

1. Understand the short-term behavior of Shopify stock  
2. Identify volatility patterns and market signals  
3. Build a reusable data analysis pipeline  
4. Produce a dashboard that highlights financial insights in a business-friendly format  
5. Demonstrate data analyst skills through a clean and well-documented project  

---

## 🧠 Key Insights (Business + Data)

- Shopify’s stock price shows **frequent high volatility**, suggesting strong reactivity to market news  
- The **7-day trend metric** highlights several micro-cycles useful for short-term traders  
- **Daily return fluctuations** reveal clear periods of momentum vs. correction  
- The High–Low daily range provides visibility into market pressure and trader sentiment  
- Volatility analysis helps evaluate the level of investment risk  

These insights can support short-term decision-making for investors or portfolio managers.

---

## 🛠️ Tech Stack

**Languages & Tools:**  
- Python  
- SQL  
- Power BI  
- Jupyter Notebook  
- Git & GitHub  

**Python Libraries:**  
- Pandas  
- NumPy  
- Matplotlib / Seaborn (optional)  

**Concepts Used:**  
- Data cleaning  
- Exploratory Data Analysis (EDA)  
- Time-series metrics  
- Financial indicators  
- Dashboard design & storytelling  
- Project structuring and modularization  

---

## 📂 Project Structure
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

This architecture follows best practices for clarity, scalability, and reproducibility.

---

## 📊 Dashboard Overview (Power BI)

The Power BI dashboard is designed following data storytelling principles:

### **Top Section — KPIs**
- Current Closing Price  
- Daily Return  
- 7-Day Trend (%)  
- Volatility  
- High–Low Range  

### **Middle Section — Visuals**
- Stock Price over Time (Line Chart)  
- Daily Return (%) (Bar Chart)  

### **Bottom Section — Supporting Charts**
- High–Low Comparison  
- Volume Analysis (if included)  

Color palette:
- **Green** → Positive growth  
- **Red** → Negative variation  
- **Blue/Grey** → Neutral elements  

---

## ⚙️ How to Run the Project

### **1. Clone the repository**
```bash
git clone https://github.com/light971/Shopify-Stock-Analysis.git
cd Shopify-Stock-Analysis
```

2. Install dependencies
```bash   
pip install -r requirements.txt
```

3. Prepare the dataset

Place your raw file in data/raw/

5. Run the notebooks
   
   - 0.0-data-cleaning.ipynb → clean & preprocess the dataset
   - 1.0-data-analysis.ipynb → compute KPIs & generate visuals

6. Open the Power BI report

Import the processed data from data/processed/

## 🚀 Possible Improvements (Next Steps)

- Add predictive models (ARIMA, LSTM, Prophet)
- Integrate external data (news sentiment, macro indicators)
- Automate the pipeline with Airflow or Prefect
- Deploy an online dashboard using Streamlit / Dash
- Add unit tests for data transformation scripts
