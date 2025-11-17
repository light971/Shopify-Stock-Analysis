"""
data_analysis.py
----------------
Template générique pour l'analyse de données.

Ce module contient des fonctions réutilisables pour :
- fusionner plusieurs DataFrames
- calculer des résumés statistiques
- générer des KPIs globaux
- analyser les tendances dans le temps
- regrouper par catégories ou variables clés

Ce template est adaptable à tous les projets Data Analyst.
"""

import pandas as pd


# =========================================================
# 🔗 FUSION DE PLUSIEURS DATAFRAMES
# =========================================================
def merge_dataframes(dfs: list, on: str, how: str = "inner") -> pd.DataFrame:
    """
    Fusionne une liste de DataFrames sur une colonne commune.

    Args:
        dfs: liste de DataFrames à fusionner
        on: colonne sur laquelle fusionner
        how: type de jointure ("inner", "left", "right", "outer")

    Returns:
        DataFrame fusionné
    """
    from functools import reduce
    df_merged = reduce(lambda left, right: pd.merge(left, right, on=on, how=how), dfs)
    return df_merged


# =========================================================
# 📊 RÉSUMÉ STATISTIQUE
# =========================================================
def summarize_numeric(df: pd.DataFrame) -> pd.DataFrame:
    """
    Retourne un résumé statistique des colonnes numériques.
    
    Args:
        df: DataFrame
    
    Returns:
        DataFrame avec count, mean, std, min, 25%, 50%, 75%, max
    """
    return df.describe().transpose()


# =========================================================
# 🧮 KPIs GLOBAUX
# =========================================================
def calculate_global_kpis(df: pd.DataFrame, value_column: str, group_column: str = None) -> dict:
    """
    Calcule des KPIs génériques sur une colonne numérique.

    Args:
        df: DataFrame
        value_column: nom de la colonne à analyser (ex: "sales", "amount")
        group_column: optionnel, calcul des KPIs par groupe

    Returns:
        dict avec total, moyenne, max, min, et éventuellement par groupe
    """
    if group_column:
        grouped = df.groupby(group_column)[value_column].agg(["sum", "mean", "max", "min"]).reset_index()
        return grouped
    else:
        return {
            "total": df[value_column].sum(),
            "mean": df[value_column].mean(),
            "max": df[value_column].max(),
            "min": df[value_column].min()
        }


# =========================================================
# 📅 ANALYSE DANS LE TEMPS
# =========================================================
def aggregate_over_time(df: pd.DataFrame, date_column: str, value_column: str, freq: str = "M") -> pd.DataFrame:
    """
    Agrège les valeurs d'une colonne sur une période temporelle.

    Args:
        df: DataFrame
        date_column: colonne de type date
        value_column: colonne à sommer ou agréger
        freq: fréquence d'agrégation ("D", "W", "M", "Q", "Y")

    Returns:
        DataFrame avec date et valeur agrégée
    """
    df = df.copy()
    df[date_column] = pd.to_datetime(df[date_column], errors="coerce")
    result = df.set_index(date_column).resample(freq)[value_column].sum().reset_index()
    return result


# =========================================================
# 🌍 AGRÉGATION PAR CATÉGORIE
# =========================================================
def aggregate_by_category(df: pd.DataFrame, category_column: str, value_column: str) -> pd.DataFrame:
    """
    Agrège une colonne numérique par catégorie.

    Args:
        df: DataFrame
        category_column: colonne catégorielle
        value_column: colonne numérique à sommer

    Returns:
        DataFrame avec total par catégorie
    """
    return df.groupby(category_column, as_index=False)[value_column].sum().sort_values(by=value_column, ascending=False)


# =========================================================
# 👥 KPIs PAR ENTITÉ
# =========================================================
def kpis_per_entity(df: pd.DataFrame, entity_column: str, value_column: str) -> pd.DataFrame:
    """
    Calcule des KPIs par entité (ex: client, produit).

    Args:
        df: DataFrame
        entity_column: colonne représentant l'entité
        value_column: colonne numérique à analyser

    Returns:
        DataFrame avec total, moyenne, max, min par entité
    """
    kpis = df.groupby(entity_column)[value_column].agg(["sum", "mean", "max", "min"]).reset_index()
    return kpis

