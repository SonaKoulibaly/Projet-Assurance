# Projet-Assurance
Analyse des Sinistres &amp; Profil des Assurés
# 📊 AssurAnalytics — Analyse des Sinistres & Profil des Assurés

> **Mastère 2 Big Data & Data Stratégie**  
> Auteur : **Sona KOULIBALY**  
> Stack : Python · Dash · Plotly · Pandas · Bootstrap

---

## 🎯 Problématique

Comment permettre à une compagnie d'assurance de **suivre ses sinistres**, **identifier les profils à risque**, **visualiser les tendances** et **aider à la décision** pour la tarification ou la prévention ?

Ce dashboard interactif répond à cette problématique en faisant **parler les données** à travers des visualisations riches, un storytelling automatique et des exports professionnels.

---

## 🗂️ Structure du Projet

```
assuranalytics/
├── app.py               # Cœur de l'application — initialisation Dash, chargement données
├── layout.py            # Interface utilisateur — structure HTML/composants
├── callbacks.py         # Logique & interactivité — callbacks, graphiques, exports
├── requirements.txt     # Dépendances Python
├── data/
│   └── assurance_data_1000.csv   # Base de données (1 000 assurés)
├── assets/
│   ├── style.css        # Design personnalisé
│   └── logo*.png        # Logos de l'application
└── docs/
    ├── documentation.docx         # Documentation technique complète
    └── screenshots/               # Captures d'écran du dashboard
```

---

## 📦 Installation

### Prérequis
- Python 3.12+
- pip

### 1. Cloner le dépôt
```bash
git clone https://github.com/<votre-username>/assuranalytics.git
cd assuranalytics
```

### 2. Créer un environnement virtuel *(recommandé)*
```bash
python -m venv venv
# Windows
venv\Scripts\activate
# macOS / Linux
source venv/bin/activate
```

### 3. Installer les dépendances
```bash
pip install -r requirements.txt
```

### 4. Lancer l'application
```bash
python app.py
```

### 5. Ouvrir dans le navigateur
```
http://127.0.0.1:9753
```

---

## 📋 Dépendances

| Package | Version | Rôle |
|---|---|---|
| `dash` | 2.17.1 | Framework web interactif |
| `dash-bootstrap-components` | 1.6.0 | Composants Bootstrap pour Dash |
| `plotly` | 5.22.0 | Graphiques interactifs |
| `pandas` | 2.2.2 | Manipulation et analyse de données |
| `numpy` | 1.26.4 | Calculs numériques |
| `openpyxl` | 3.1.4 | Export Excel |
| `reportlab` | 4.2.2 | Génération de rapports PDF |
| `gunicorn` | 22.0.0 | Serveur WSGI pour déploiement |

---

## 🗃️ Base de Données

**Fichier** : `data/assurance_data_1000.csv` — 1 000 assurés, séparateur `;`

| Colonne | Type | Description |
|---|---|---|
| `id_assure` | int | Identifiant unique |
| `age` | int | Âge de l'assuré (18–79 ans) |
| `sexe` | str | `masculin` / `feminin` |
| `type_assurance` | str | `Auto` / `Santé` / `Habitation` / `Vie` |
| `duree_contrat` | int | Durée du contrat (années) |
| `montant_prime` | float | Prime annuelle (€) |
| `nb_sinistres` | int | Nombre de sinistres déclarés |
| `montant_sinistres` | float | Montant total des sinistres (€) |
| `date_derniere_sinistre` | datetime | Date du dernier sinistre |
| `region` | str | `Dakar` / `Thiès` / `Kaolack` / `Saint-Louis` |
| `bonus_malus` | float | Coefficient bonus/malus (0.5–1.5) |

**Variables calculées automatiquement à l'initialisation :**

| Variable | Calcul | Description |
|---|---|---|
| `tranche_age` | `pd.cut()` — 6 tranches | Segmentation démographique |
| `ratio_SP` | `montant_sinistres / montant_prime` | Indicateur de rentabilité |
| `bm_cat` | `pd.cut()` — 4 catégories | Bonus fort / Bonus / Neutre / Malus |

---

## 🖥️ Fonctionnalités du Dashboard

### 🔍 Filtres Interactifs (Panneau Gauche)
- **Type d'assurance** — Multi-sélection (Auto, Santé, Habitation, Vie)
- **Sexe** — Multi-sélection (Masculin, Féminin)
- **Région** — Multi-sélection (4 régions du Sénégal)
- **Nb sinistres** — Multi-sélection (0, 1, 2, 3, 4+)
- **Tranche d'âge** — Slider range (18–79 ans)
- **Bonus/Malus** — Slider range (0.5–1.5)
- **Bouton Réinitialiser** — Reset de tous les filtres en un clic

### 📊 KPIs (8 indicateurs)
**Principaux :** Total assurés · Total sinistres · Coût moyen sinistre · Prime moyenne  
**Secondaires :** Taux de sinistralité · Ratio S/P médian · B/M moyen · % assurés déficitaires

### 💡 Insights Clés — Storytelling Automatique
Le dashboard génère **9 insights dynamiques** mis à jour à chaque filtre :
- Sélection active et % du portefeuille
- Taux de sinistralité vs moyenne globale
- Comparaison du coût moyen vs référence
- Alerte de rentabilité (ratio S/P)
- Région la plus coûteuse
- Tranche d'âge à risque
- Analyse Bonus/Malus
- Recommandation tarifaire automatique

### 📈 Visualisations (13 graphiques en 5 sections)

**Section 1 — Profil des Assurés**
| Graphique | Type | Ce qu'il révèle |
|---|---|---|
| Répartition par type d'assurance | Donut | Comparaison — Équilibre du portefeuille |
| Distribution des âges par type | Histogramme | Tendance — Structure démographique |
| Prime moy. par tranche d'âge & sexe | Barres groupées | Comparaison — Différences tarifaires H/F |
| Répartition régionale | Donut | Comparaison — Poids de chaque région |

**Section 2 — Analyse des Sinistres**
| Graphique | Type | Ce qu'il révèle |
|---|---|---|
| Sinistres & montants par région | Barres horizontales | Comparaison — Zones géographiques à risque |
| Fréquence des sinistres déclarés | Barres | Anomalie — % d'assurés sans sinistre |
| Évolution temporelle | Barres + ligne double axe | Tendance — Saisonnalité sur 5 ans |
| Sinistres moyens par tranche d'âge & type | Barres groupées | Relation — Profils d'âge les plus sinistrés |

**Section 3 — Rentabilité & Tarification**
| Graphique | Type | Ce qu'il révèle |
|---|---|---|
| Prime vs Montant sinistre | Nuage de points | Relation — Assurés déficitaires (au-dessus diagonale) |
| Coût moyen vs Prime par type | Barres groupées | Comparaison — Rentabilité par produit |

**Section 4 — Profils à Risque & Bonus/Malus**
| Graphique | Type | Ce qu'il révèle |
|---|---|---|
| Heatmap risque Âge × Type | Carte de chaleur | Anomalie — Profils les plus sinistrés |
| Distribution Bonus/Malus | Donut | Tendance — Équilibre B/M du portefeuille |
| B/M × Nb sinistres × Montant | Nuage de points | Corrélation — Détection profils extrêmes |

**Section 5 — Tableau de Données**
- Table interactive avec tri, filtre natif
- Mise en surbrillance conditionnelle (rouge si nb_sinistres > 2, jaune si B/M > 1.2)
- Affichage des 100 premières lignes filtrées

### 📤 Exports
| Format | Contenu | Téléchargement |
|---|---|---|
| **Excel** | 4 feuilles : Données, KPIs, Par Région, Par Type | Direct sur le PC |
| **HTML** | Rapport complet avec graphiques Plotly interactifs | Lien HTML |
| **PDF** | Rapport structuré (KPIs, tableau région, insights) | Direct sur le PC |

---

## 🏗️ Architecture Technique

```
┌─────────────────────────────────────────────────┐
│                   app.py                        │
│  ┌─────────────┐  ┌───────────┐  ┌───────────┐ │
│  │  Dash init  │  │ Data load │  │ Enrichment│ │
│  └─────────────┘  └───────────┘  └───────────┘ │
└────────────┬────────────────┬───────────────────┘
             │                │
    ┌────────▼───────┐  ┌─────▼──────────┐
    │   layout.py    │  │  callbacks.py  │
    │  Interface UI  │  │  Logique & viz │
    └────────────────┘  └────────────────┘
```

**Flux de données :**
```
CSV → pandas DataFrame → Enrichissement → filter_data() → Graphiques Plotly → Interface Dash
                                                       └→ Insights auto
                                                       └→ KPIs dynamiques
                                                       └→ Exports (Excel/HTML/PDF)
```

**Callbacks :**
- `reset_filters` — Réinitialisation des 6 filtres
- `update_all` — Callback principal (6 inputs → 30 outputs)
- `download_excel` — Export Excel multi-feuilles
- `download_html` — Export rapport HTML
- `download_pdf` — Export rapport PDF (ReportLab)

---

## 🧠 Bonnes Pratiques de Visualisation Appliquées

| Principe | Application dans le projet |
|---|---|
| **Tendance** | Série temporelle mensuelle (2020–2025) |
| **Comparaison** | Barres groupées H/F, coût vs prime par type |
| **Anomalie** | Heatmap risque, histogramme sinistres (0 = 61.7%) |
| **Relation** | Scatter prime vs sinistre, B/M vs nb sinistres |
| **Corrélation** | Nuage de points B/M × montant × fréquence |
| **Storytelling** | 9 insights automatiques contextuels |
| **UX** | Filtres sticky, tooltips, couleurs codées, sections |

---

## 🔮 Pistes d'Amélioration

- [ ] **Score de risque** — Modèle ML (régression logistique ou Random Forest) pour prédire la sinistralité
- [ ] **Carte géographique** — Visualisation Choropleth des régions du Sénégal
- [ ] **Segmentation K-Means** — Clustering automatique des profils assurés
- [ ] **Alertes en temps réel** — Notification automatique pour les profils à risque extrême
- [ ] **Multi-page Dash** — Séparer les sections en onglets dédiés
- [ ] **Authentification** — Login sécurisé pour accès au dashboard
- [ ] **Base de données** — Connexion PostgreSQL / SQLite pour données en temps réel
- [ ] **Déploiement cloud** — Hébergement sur Render, Railway ou Heroku

---

## 📸 Captures d'Écran

> Captures disponibles dans `docs/screenshots/`

| Vue | Description |
|---|---|
| `dashboard_overview.png` | Vue d'ensemble du dashboard complet |
| `filters_kpis.png` | Panneau filtres + KPIs principaux |
| `insights.png` | Section insights automatiques |
| `charts_section1.png` | Section profil des assurés |
| `charts_section2.png` | Section analyse des sinistres |
| `charts_section3.png` | Section rentabilité |
| `charts_section4.png` | Section profils à risque |
| `data_table.png` | Tableau de données interactif |

---

## 👤 Auteur

**Sona KOULIBALY**  
Mastère 2 Big Data & Data Stratégie  

---

## 📄 Licence

Ce projet est réalisé dans le cadre d'un projet académique — Mastère 2 Big Data & Data Stratégie.  
Tous droits réservés © 2025 Sona KOULIBALY.
