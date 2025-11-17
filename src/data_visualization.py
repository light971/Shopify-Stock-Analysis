"""
data_visualization.py
----------------------

This script provides reusable functions for data visualization
in Data Analyst projects.

It includes plots for:
- Data overview (distributions, missing values)
- Comparison between variables
- Correlation analysis
- Time series trends
- Categorical vs numerical relationships
- Custom visual reports
"""

import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
import os

# === STYLE CONFIGURATION ===
sns.set(style="whitegrid", palette="pastel")
plt.rcParams["figure.figsize"] = (10, 6)
plt.rcParams["axes.titlesize"] = 14
plt.rcParams["axes.labelsize"] = 12


# === 1. DISTRIBUTIONS ===
def plot_numeric_distribution(df: pd.DataFrame, column: str, output_path="../reports/figures/numeric_distribution.png"):
    """Plot the distribution and histogram of a numerical variable."""
    plt.figure()
    sns.histplot(df[column].dropna(), kde=True, bins=30)
    plt.title(f"Distribution of {column}")
    plt.xlabel(column)
    plt.ylabel("Frequency")
    plt.show()
    # --- Sauvegarde automatique ---
    os.makedirs(os.path.dirname(output_path), exist_ok=True)
    plt.savefig(output_path, bbox_inches="tight")
    plt.close()


def plot_categorical_distribution(df: pd.DataFrame, column: str, output_path="../reports/figures/categorical_distribution.png"):
    """Plot the distribution of a categorical variable."""
    plt.figure()
    order = df[column].value_counts().index
    sns.countplot(x=column, data=df, order=order)
    plt.title(f"Distribution of {column}")
    plt.xticks(rotation=45)
    plt.xlabel(column)
    plt.ylabel("Count")
    plt.show()
    # --- Sauvegarde automatique ---
    os.makedirs(os.path.dirname(output_path), exist_ok=True)
    plt.savefig(output_path, bbox_inches="tight")
    plt.close()


# === 2. MISSING VALUES ===
def plot_missing_values(df: pd.DataFrame, output_path="../reports/figures/missing_values.png"):
    """Visualize missing values in the dataset."""
    missing = df.isnull().mean().sort_values(ascending=False)
    missing = missing[missing > 0]
    if missing.empty:
        print("✅ No missing values found.")
        return
    plt.figure()
    sns.barplot(x=missing.values, y=missing.index)
    plt.title("Missing Values per Column")
    plt.xlabel("Percentage of Missing Values")
    plt.ylabel("Columns")
    plt.show()
    # --- Sauvegarde automatique ---
    os.makedirs(os.path.dirname(output_path), exist_ok=True)
    plt.savefig(output_path, bbox_inches="tight")
    plt.close()


# === 3. CORRELATION ===
def plot_correlation_matrix(df: pd.DataFrame, method="pearson", output_path="../reports/figures/orrelation_matrix.png"):
    """Plot a heatmap showing the correlation between numerical features."""
    corr = df.corr(method=method)
    plt.figure(figsize=(10, 8))
    sns.heatmap(corr, cmap="coolwarm", annot=True, fmt=".2f", linewidths=0.5)
    plt.title(f"Correlation Matrix ({method.title()} method)")
    plt.show()
    # --- Sauvegarde automatique ---
    os.makedirs(os.path.dirname(output_path), exist_ok=True)
    plt.savefig(output_path, bbox_inches="tight")
    plt.close()


# === 4. COMPARISONS ===
def plot_box_by_category(df: pd.DataFrame, category: str, numeric: str, output_path="../reports/figures/box_by_category.png"):
    """Compare distributions of a numeric variable across categories."""
    plt.figure()
    sns.boxplot(x=category, y=numeric, data=df)
    plt.title(f"{numeric} by {category}")
    plt.xticks(rotation=45)
    plt.show()
    # --- Sauvegarde automatique ---
    os.makedirs(os.path.dirname(output_path), exist_ok=True)
    plt.savefig(output_path, bbox_inches="tight")
    plt.close()


def plot_violin_by_category(df: pd.DataFrame, category: str, numeric: str, output_path="../reports/figures/violin_by_category.png"):
    """Visualize the spread of data per category with a violin plot."""
    plt.figure()
    sns.violinplot(x=category, y=numeric, data=df, inner="quartile")
    plt.title(f"{numeric} Distribution by {category}")
    plt.xticks(rotation=45)
    plt.show()
    # --- Sauvegarde automatique ---
    os.makedirs(os.path.dirname(output_path), exist_ok=True)
    plt.savefig(output_path, bbox_inches="tight")
    plt.close()


# === 5. TIME SERIES ===
def plot_time_series(df: pd.DataFrame, date_col: str, value_col: str, freq="D", output_path="../reports/figures/time_series.png"):
    """Plot time series trends."""
    ts = df.set_index(date_col)[value_col].resample(freq).mean()
    plt.figure()
    ts.plot(marker="o")
    plt.title(f"Trend of {value_col} over time")
    plt.xlabel("Date")
    plt.ylabel(value_col)
    plt.show()
    # --- Sauvegarde automatique ---
    os.makedirs(os.path.dirname(output_path), exist_ok=True)
    plt.savefig(output_path, bbox_inches="tight")
    plt.close()


# === 6. OUTLIERS ===
def plot_outliers(df: pd.DataFrame, numeric_col: str, output_path="../reports/figures/outliers.png"):
    """Show outliers of a numeric column using a boxplot."""
    plt.figure()
    sns.boxplot(x=df[numeric_col])
    plt.title(f"Outliers in {numeric_col}")
    plt.xlabel(numeric_col)
    plt.show()
    # --- Sauvegarde automatique ---
    os.makedirs(os.path.dirname(output_path), exist_ok=True)
    plt.savefig(output_path, bbox_inches="tight")
    plt.close()


# === 7. PAIRPLOT ===
def plot_pairwise_relationships(df: pd.DataFrame, vars=None, hue=None, output_path="../reports/figures/pairwise_relationships.png"):
    """Show pairwise relationships between numerical features."""
    sns.pairplot(df, vars=vars, hue=hue, diag_kind="kde")
    plt.suptitle("Pairwise Relationships", y=1.02)
    plt.show()
    # --- Sauvegarde automatique ---
    os.makedirs(os.path.dirname(output_path), exist_ok=True)
    plt.savefig(output_path, bbox_inches="tight")
    plt.close()


# === 8. BAR CHARTS ===
def plot_top_categories(df: pd.DataFrame, column: str, top_n=10, output_path="../reports/figures/top_categories.png"):
    """Show the most frequent categories in a column."""
    plt.figure()
    df[column].value_counts().head(top_n).plot(kind="bar")
    plt.title(f"Top {top_n} categories in {column}")
    plt.ylabel("Count")
    plt.show()
    # --- Sauvegarde automatique ---
    os.makedirs(os.path.dirname(output_path), exist_ok=True)
    plt.savefig(output_path, bbox_inches="tight")
    plt.close()


# === 9. CUSTOM DASHBOARD-LIKE VIEW ===
def overview_dashboard(df: pd.DataFrame):
    """Display an overview of dataset distributions for quick EDA."""
    numeric_cols = df.select_dtypes(include=["int64", "float64"]).columns
    cat_cols = df.select_dtypes(include=["object", "category"]).columns

    print("=== Dataset Overview ===")
    print(df.describe())
    print("\n=== Missing Values ===")
    print(df.isnull().sum())

    for col in numeric_cols[:3]:
        plot_numeric_distribution(df, col)

    for col in cat_cols[:2]:
        plot_categorical_distribution(df, col)