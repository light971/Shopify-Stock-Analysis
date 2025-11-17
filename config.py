import os
import sys

# Définir le chemin absolu du projet (racine)
PROJECT_ROOT = os.path.abspath(os.path.dirname(__file__))

# Ajouter 'src' au chemin Python si non présent
SRC_PATH = os.path.join(PROJECT_ROOT, "src")
if SRC_PATH not in sys.path:
    sys.path.append(SRC_PATH)

# 📂 Définir quelques chemins utiles
DATA_RAW = os.path.join(PROJECT_ROOT, 'data', 'raw')
DATA_PROCESSED = os.path.join(PROJECT_ROOT, 'data', 'processed')
REPORTS_SUMMARY = os.path.join(PROJECT_ROOT, 'reports', 'summary')
FIGURES_PATH = os.path.join(PROJECT_ROOT, 'reports', 'figures')

print("✅ config.py chargé")
print("SRC_PATH:", SRC_PATH)
