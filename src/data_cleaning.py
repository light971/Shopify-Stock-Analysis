import pandas as pd
import numpy as np


def load_data(path: str) -> pd.DataFrame:
    return pd.read_csv(path)

# def clean_data(df: pd.DataFrame) -> pd.DataFrame:
#     df = df.drop_duplicates()
#     df.fillna(0, inplace=True)
#     return df

def save_data(df: pd.DataFrame, path: str):
    df.to_csv(path, index=False)
    
import pandas as pd
from IPython.display import display

def apercu_dataset(data: pd.DataFrame):
    """
    Affiche un aperçu global et des statistiques descriptives
    d'un DataFrame.

    Args:
        data (pd.DataFrame): Le DataFrame à analyser.
    """
    print("--- Aperçu global (data.info()) ---")
    data.info()
    
    print("\n--- Dimensions du dataset (Shape) ---")
    print("Shape :", data.shape)
    
    print("\n--- Statistiques descriptives ---")
    # Utilisation de display pour un affichage propre dans un environnement comme Jupyter/Colab
    display(data.describe(include="all"))

# --- Exemple d'utilisation (Décommentez pour tester) ---
# Si 'data' est votre DataFrame :
# apercu_dataset(data)

"""
data_cleaning.py
----------------
Utility functions for cleaning and preparing raw data
for analysis and visualization.
"""

def clean_data(df: pd.DataFrame) -> pd.DataFrame:
    """
    Clean a raw dataframe and prepare it for analysis.

    Steps:
    1. Standardize column names
    2. Remove duplicates
    3. Handle missing values
    4. Convert data types
    5. Fix outliers (optional)
    6. Return a cleaned DataFrame
    """
    df = df.copy()

    # --- 1. Standardize column names ---
    df.columns = (
        df.columns
        .str.strip()
        .str.lower()
        .str.replace(" ", "_")
        .str.replace("-", "_")
    )

    # --- 2. Remove duplicates ---
    initial_shape = df.shape
    df.drop_duplicates(inplace=True)
    print(f"Removed {initial_shape[0] - df.shape[0]} duplicate rows")

    # --- 3. Handle missing values ---
    missing_summary = df.isna().sum()
    print("\nMissing values per column before cleaning:")
    print(missing_summary[missing_summary > 0])

    # Fill numeric NaN with median
    for col in df.select_dtypes(include=[np.number]).columns:
        df[col] = df[col].fillna(df[col].median())

    # Fill categorical NaN with mode
    for col in df.select_dtypes(include=["object"]).columns:
        if df[col].isna().sum() > 0:
            df[col] = df[col].fillna(df[col].mode()[0])

    # --- 4. Convert data types ---
    for col in df.columns:
        if "date" in col or "time" in col:
            try:
                df[col] = pd.to_datetime(df[col])
            except Exception:
                pass

    # --- 5. Fix outliers (optional example) ---
    for col in df.select_dtypes(include=[np.number]).columns:
        q1, q3 = df[col].quantile([0.25, 0.75])
        iqr = q3 - q1
        lower, upper = q1 - 1.5 * iqr, q3 + 1.5 * iqr
        outlier_mask = (df[col] < lower) | (df[col] > upper)
        if outlier_mask.sum() > 0:
            print(f"{outlier_mask.sum()} outliers detected in '{col}' — capped to IQR range.")
            df[col] = np.clip(df[col], lower, upper)

    # --- 6. Final report ---
    print("\n✅ Data cleaning complete!")
    print(f"Final shape: {df.shape}")

    return df


def summarize_data(df: pd.DataFrame) -> pd.DataFrame:
    """
    Generate a quick summary of the dataset.
    """
    summary = pd.DataFrame({
        "dtype": df.dtypes,
        "missing_values": df.isna().sum(),
        "unique_values": df.nunique()
    })
    summary["missing_%"] = (summary["missing_values"] / len(df)) * 100
    return summary.sort_values(by="missing_%", ascending=False)

# =====================================
# Fonctions de nettoyage par type
# =====================================
def clean_text_column(df: pd.DataFrame, column: str) -> pd.DataFrame:
    """Nettoie une colonne texte : strip et lowercase."""
    df[column] = df[column].astype(str).str.strip().str.lower()
    return df

def clean_numeric_column(df: pd.DataFrame, column: str) -> pd.DataFrame:
    """Convertit une colonne en numérique et remplace les NaN par 0."""
    df[column] = pd.to_numeric(df[column], errors="coerce").fillna(0)
    return df

def clean_date_column(df: pd.DataFrame, column: str) -> pd.DataFrame:
    """Convertit une colonne en datetime."""
    df[column] = pd.to_datetime(df[column], errors="coerce")
    return df


# =====================================
# Fonction principale générique
# =====================================


def clean_all_data(*dfs) -> list:
    """
    Nettoie plusieurs DataFrames passés séparément ou en dictionnaire.

    Args:
        *dfs: un ou plusieurs DataFrames, ex:
            clean_all_data(df_customers, df_orders)

    Returns:
        Liste de DataFrames nettoyés, dans le même ordre que l'entrée.
    """
    cleaned = []

    for df in dfs:
        df_clean = df.copy()

        for col in df_clean.columns:
            # si la colonne est du type texte : on applique clean_text_column (strip + lowercase).
            if pd.api.types.is_string_dtype(df_clean[col]):
                df_clean = clean_text_column(df_clean, col)
            # si la colonne est numérique : on applique clean_numeric_column (conversion + remplacement NaN par 0).
            elif pd.api.types.is_numeric_dtype(df_clean[col]):
                df_clean = clean_numeric_column(df_clean, col)
            # si la colonne est de type date : on applique clean_date_column (conversion en datetime).
            elif pd.api.types.is_datetime64_any_dtype(df_clean[col]) or "date" in col.lower():
                df_clean = clean_date_column(df_clean, col)

        cleaned.append(df_clean)

    return cleaned