# =============================================================
#  app.py — AssurAnalytics
#  Projet : Analyse des Sinistres & Profil des Assurés
#  Auteur : Sona KOULIBALY — Mastère 2 Big Data & Data Stratégie
# =============================================================

import os
import pandas as pd
import dash
import dash_bootstrap_components as dbc
from dotenv import load_dotenv

# ── Chargement des variables d'environnement (.env en local) ──
load_dotenv()

# ════════════════════════════════════════════════════════════════
# INITIALISATION DE L'APPLICATION
# ════════════════════════════════════════════════════════════════
app = dash.Dash(
    __name__,
    external_stylesheets=[
        dbc.themes.BOOTSTRAP,
        "https://cdnjs.cloudflare.com/ajax/libs/font-awesome/6.4.0/css/all.min.css",
    ],
    suppress_callback_exceptions=True,
    meta_tags=[
        {"name": "viewport", "content": "width=device-width, initial-scale=1"},
        {"name": "description", "content": "AssurAnalytics — Dashboard d'analyse des sinistres"},
    ],
    title="AssurAnalytics"
)

# ── Exposition du server WSGI (obligatoire pour Render/Gunicorn) ──
server = app.server

# ── Clé secrète sécurisée via variable d'environnement ──
server.secret_key = os.environ.get("SECRET_KEY", "dev-key-change-in-prod")

# ════════════════════════════════════════════════════════════════
# CHARGEMENT ET ENRICHISSEMENT DES DONNÉES
# ════════════════════════════════════════════════════════════════

# Chemin absolu — fonctionne en local ET sur Render
BASE_DIR = os.path.dirname(os.path.abspath(__file__))
DATA_PATH = os.path.join(BASE_DIR, "data", "assurance_data_1000.csv")

# Vérification que le fichier existe (aide au débogage sur Render)
if not os.path.exists(DATA_PATH):
    raise FileNotFoundError(
        f"Fichier CSV introuvable : {DATA_PATH}\n"
        f"Répertoire courant : {os.getcwd()}\n"
        f"Contenu de BASE_DIR : {os.listdir(BASE_DIR)}"
    )

df = pd.read_csv(DATA_PATH, sep=';')

# Conversion des dates
df['date_derniere_sinistre'] = pd.to_datetime(df['date_derniere_sinistre'], errors='coerce')

# Variables calculées
df['tranche_age'] = pd.cut(
    df['age'],
    bins=[17, 25, 35, 45, 55, 65, 79],
    labels=['18-25', '26-35', '36-45', '46-55', '56-65', '66-79'],
    include_lowest=True
)
df['ratio_SP'] = (df['montant_sinistres'] / df['montant_prime']).round(2)
df['bm_cat'] = pd.cut(
    df['bonus_malus'],
    bins=[0.4, 0.8, 1.0, 1.2, 1.6],
    labels=['Bonus fort', 'Bonus', 'Neutre', 'Malus']
)
df['annee_sinistre'] = df['date_derniere_sinistre'].dt.year
df['mois_sinistre']  = df['date_derniere_sinistre'].dt.month

# ════════════════════════════════════════════════════════════════
# LAYOUT & CALLBACKS
# ════════════════════════════════════════════════════════════════
from layout import create_layout
from callbacks import register_callbacks

app.layout = create_layout(app)
register_callbacks(app, df)

# ════════════════════════════════════════════════════════════════
# LANCEMENT
# ════════════════════════════════════════════════════════════════
if __name__ == '__main__':
    debug_mode = os.environ.get("DEBUG", "False").lower() == "true"
    app.run(debug=debug_mode, host='0.0.0.0', port=9753)
