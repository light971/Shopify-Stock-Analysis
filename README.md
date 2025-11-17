# 🧠 Data Analyst Project Template

<a target="_blank" href="https://datalumina.com/">
    <img src="https://img.shields.io/badge/Datalumina-Data%20Analyst%20Template-2856f7" alt="Datalumina Data Analyst Project" />
</a>

[![Python](https://img.shields.io/badge/Python-3.11-blue?logo=python)](https://www.python.org/)
[![Jupyter](https://img.shields.io/badge/Jupyter-Notebook-orange?logo=jupyter)](https://jupyter.org/)
[![SQL](https://img.shields.io/badge/SQL-database-lightgrey?logo=postgresql)](https://www.postgresql.org/)
[![Power BI](https://img.shields.io/badge/Power%20BI-reporting-yellow?logo=power-bi)](https://powerbi.microsoft.com/)

## Overview
Clean and organized structure for **data analysis projects**, including notebooks, scripts, SQL queries, and reports.

## Setup
1. Copy `.env.example` → `.env`
2. Install dependencies: `pip install -r requirements.txt`

## Project Structure
```
│
├── data/
│   ├── raw/             # Données brutes (non modifiées)
│   ├── processed/       # Données nettoyées et prêtes à l’analyse
│   └── external/        # Données externes (API, sources publiques, etc.)
│
├── notebooks/
│   ├── 0.0-data-cleaning.ipynb      # Chargement et nettoyage des données
│   ├── 1.0-data-analysis.ipynb      # Analyses statistiques et KPIs
│   └── 2.0-data-visualization.ipynb # Visualisations et graphiques
│
├── reports/
│   ├── figures/         # Graphiques exportés (.png, .jpg)
│   └── summary/         # Tableaux ou synthèses d’analyse (.csv)
│
├── src/
│   ├── init.py
│   ├── data_cleaning.py     # Fonctions de nettoyage des données
│   ├── data_analysis.py     # Fonctions d’analyse et de calculs de KPIs
│   └── data_visualization.py# Fonctions de visualisation
│
├── config.py # Paramètres globaux du projet (chemins, constantes, etc.)
│
├── requirements.txt
├── README.md
└── .gitignore
```

## Workflow
1. Data collection (CSV, SQL, API)  
2. Data cleaning & preprocessing  
3. EDA & visualization  
4. Reporting & dashboards  
5. Documentation in `reports/summary`
# Template-data-analyst
