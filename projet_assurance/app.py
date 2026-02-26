# =============================================================
#  app.py  —  Cœur de l'application
#  Projet : Analyse des Sinistres & Profil des Assurés
#  Auteur : Sona KOULIBALY
#  Mastère 2 Big Data & Data Stratégie
# =============================================================

import dash
import dash_bootstrap_components as dbc
from layout import create_layout
from callbacks import register_callbacks
import pandas as pd

# ── Initialisation de l'application ───────────────────────────
app = dash.Dash(
    __name__,
    external_stylesheets=[
        dbc.themes.BOOTSTRAP,
        "https://cdnjs.cloudflare.com/ajax/libs/font-awesome/6.4.0/css/all.min.css",
    ],
    suppress_callback_exceptions=True,
    meta_tags=[
        {"name": "viewport", "content": "width=device-width, initial-scale=1"},
        {"charset": "UTF-8"},
    ]
)

server = app.server
app.title = "AssurAnalytics — Analyse des Sinistres & Profil des Assurés"

# ── Chargement & Enrichissement des données ───────────────────
try:
    df = pd.read_csv('data/assurance_data_1000.csv', sep=';')

    # Conversion dates
    df['date_derniere_sinistre'] = pd.to_datetime(
        df['date_derniere_sinistre'], errors='coerce'
    )

    # Tranches d'âge
    df['tranche_age'] = pd.cut(
        df['age'],
        bins=[17, 25, 35, 45, 55, 65, 79],
        labels=['18-25', '26-35', '36-45', '46-55', '56-65', '66-79'],
        include_lowest=True
    )

    # Ratio sinistre / prime (rentabilité)
    df['ratio_SP'] = (df['montant_sinistres'] / df['montant_prime']).round(2)

    # Catégorie bonus/malus
    df['bm_cat'] = pd.cut(
        df['bonus_malus'],
        bins=[0.4, 0.8, 1.0, 1.2, 1.6],
        labels=['Bonus fort', 'Bonus', 'Neutre', 'Malus']
    )

    # Année et mois du sinistre
    df['annee_sinistre'] = df['date_derniere_sinistre'].dt.year
    df['mois_sinistre']  = df['date_derniere_sinistre'].dt.to_period('M').astype(str)

    print(f"✅  Données chargées   : {len(df)} assurés")
    print(f"📊  Colonnes           : {df.columns.tolist()}")
    print(f"🗺️   Régions            : {df['region'].unique().tolist()}")
    print(f"🛡️   Types              : {df['type_assurance'].unique().tolist()}")
    print(f"📅  Âge                : {df['age'].min()} → {df['age'].max()} ans")

except Exception as e:
    print(f"❌ Erreur chargement données : {e}")
    import traceback; traceback.print_exc()
    df = pd.DataFrame()

# ── Layout & Callbacks ─────────────────────────────────────────
app.layout = create_layout()
register_callbacks(app, df)

# ── Lancement ─────────────────────────────────────────────────
if __name__ == '__main__':
    app.run(debug=True, host="127.0.0.1", port=9753)