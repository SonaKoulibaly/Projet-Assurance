# 📊 AssurAnalytics — Analyse des Sinistres & Profil des Assurés

> **Mastère 2 Big Data & Data Stratégie**  
> Auteur : **Sona KOULIBALY**  
> Stack : Python · Dash · Plotly · Pandas · Bootstrap

---

## 🌐 Démo en Ligne

👉 **[Voir le dashboard en ligne](https://assuranalytics1.onrender.com)**

> ⚠️ Hébergé sur Render (plan gratuit) — le service peut mettre ~30 secondes à démarrer après une période d'inactivité.

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
├── render.yaml          # Configuration déploiement Render
├── .env.example         # Modèle de configuration (à copier en .env)
├── .gitignore           # Fichiers exclus de GitHub (secrets, venv, cache)
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

## 📦 Installation Locale

### Prérequis
- Python 3.12+
- pip

### 1. Cloner le dépôt
```bash
git clone https://github.com/<votre-username>/assuranalytics.git
cd assuranalytics
```

### 2. Créer un environnement virtuel
```bash
python -m venv .venv

# Windows
.venv\Scripts\activate

# macOS / Linux
source .venv/bin/activate
```

### 3. Installer les dépendances
```bash
pip install -r requirements.txt
```

### 4. Configurer les variables d'environnement
```bash
# Copier le fichier modèle
cp .env.example .env

# Ouvrir .env et renseigner votre SECRET_KEY
```

### 5. Lancer l'application
```bash
python app.py
```

### 6. Ouvrir dans le navigateur
```
http://127.0.0.1:9753
```

---

## 🔒 Sécurité du Code

Ce projet est public sur GitHub. Les bonnes pratiques suivantes sont appliquées :

- **`.env`** — contient les secrets (SECRET_KEY) et n'est **jamais poussé** sur GitHub
- **`.gitignore`** — exclut `.env`, `.venv/`, `__pycache__/`, fichiers générés
- **`.env.example`** — modèle public sans valeurs sensibles, à copier localement
- **`render.yaml`** — la clé secrète est générée automatiquement par Render (`generateValue: true`), jamais écrite en clair
- **`os.environ.get()`** — toutes les variables sensibles sont lues depuis l'environnement, jamais codées en dur

---

## 🚀 Déploiement sur Render

### Étape 1 — Préparer le dépôt GitHub
Vérifiez que ces fichiers sont bien présents et commités :
```
✅ app.py          (avec server = app.server)
✅ requirements.txt (avec gunicorn)
✅ render.yaml
✅ .gitignore      (avec .env dedans)
✅ data/assurance_data_1000.csv
```

### Étape 2 — Créer le service sur Render
1. Aller sur **[render.com](https://render.com)** → créer un compte gratuit
2. Cliquer **New +** → **Web Service**
3. Connecter votre compte GitHub → sélectionner le repo `assuranalytics`
4. Render détecte automatiquement le `render.yaml`
5. Vérifier les paramètres :
   - **Build Command** : `pip install -r requirements.txt`
   - **Start Command** : `gunicorn app:server --workers 2 --bind 0.0.0.0:$PORT --timeout 120`
   - **Runtime** : Python 3

### Étape 3 — Configurer la variable SECRET_KEY
Dans Render → votre service → **Environment** → **Add Environment Variable** :
```
Key   : SECRET_KEY
Value : <générez une clé longue et aléatoire>
```

### Étape 4 — Déployer
Cliquer **Deploy** → Render build et démarre le service.  
Votre URL sera du type : `https://assuranalytics.onrender.com`

### Étape 5 — Mettre l'URL dans le README
Remplacez dans ce README :
```
https://assuranalytics.onrender.com
```
par votre vraie URL Render.

> **Note plan gratuit Render :** le service s'endort après 15 min d'inactivité et se réveille en ~30 secondes au premier accès. Pour éviter ça, il faut passer sur un plan payant.

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
| `python-dotenv` | 1.0.1 | Chargement des variables d'environnement |

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

---

## 🖥️ Fonctionnalités du Dashboard

### 🔍 Filtres Interactifs
- Type d'assurance · Sexe · Région · Nb sinistres · Tranche d'âge · Bonus/Malus
- Bouton **Réinitialiser** — reset de tous les filtres en un clic
- Bouton **Actualiser** — rechargement complet de la page

### 📊 KPIs (8 indicateurs dynamiques)
**Principaux :** Total assurés · Total sinistres · Coût moyen sinistre · Prime moyenne  
**Secondaires :** Taux de sinistralité · Ratio S/P médian · B/M moyen · % assurés déficitaires

### 💡 Insights Clés — Storytelling Automatique
9 insights générés dynamiquement à chaque filtre : sinistralité, rentabilité, régions à risque, recommandations tarifaires…

### 📈 Visualisations (13 graphiques en 5 sections)

**Section 1 — Profil des Assurés**
- Répartition par type d'assurance (donut)
- Distribution des âges par type (histogramme)
- Prime moyenne par tranche d'âge & sexe (barres groupées)
- Répartition régionale (donut)

**Section 2 — Analyse des Sinistres**
- Sinistres & montants par région (barres horizontales)
- Fréquence des sinistres (histogramme)
- Évolution temporelle 2020–2025 (barres + ligne double axe)
- Sinistres moyens par tranche d'âge & type (barres groupées)

**Section 3 — Rentabilité & Tarification**
- Prime vs Montant sinistre (nuage de points)
- Coût moyen vs Prime par type (barres groupées)

**Section 4 — Profils à Risque & Bonus/Malus**
- Heatmap risque Âge × Type
- Distribution Bonus/Malus (donut)
- B/M × Nb sinistres × Montant (nuage de points)

**Section 5 — Tableau de Données**
- 100 premières lignes filtrées, tri & filtre natifs
- Surbrillance conditionnelle (rouge si nb_sinistres > 2, jaune si B/M > 1.2)

### 📤 Exports
| Format | Contenu |
|---|---|
| **Excel** | 4 feuilles : Données, KPIs, Par Région, Par Type |
| **HTML** | Rapport avec graphiques Plotly interactifs |
| **PDF** | Rapport structuré (KPIs, tableau région, insights) |

---

## 🧠 Bonnes Pratiques de Visualisation Appliquées

| Principe | Application |
|---|---|
| **Tendance** | Série temporelle mensuelle 2020–2025 |
| **Comparaison** | Barres groupées H/F, coût vs prime par type |
| **Anomalie** | Heatmap risque, histogramme sinistres |
| **Relation** | Scatter prime vs sinistre |
| **Corrélation** | Nuage B/M × sinistres × montant |
| **Storytelling** | 9 insights automatiques contextuels |

---

## 🔮 Pistes d'Amélioration

- [ ] Score de risque ML (Random Forest) pour prédire la sinistralité
- [ ] Carte choroplèthe des régions du Sénégal
- [ ] Segmentation K-Means des profils assurés
- [ ] Multi-page Dash (onglets par section)
- [ ] Authentification login sécurisé
- [ ] Connexion base de données PostgreSQL

---

## 📸 Captures d'Écran

> Disponibles dans `docs/screenshots/`

---

## 👤 Auteur

**Sona KOULIBALY**  
Mastère 2 Big Data & Data Stratégie

[![GitHub](https://img.shields.io/badge/GitHub-votre--username-181717?style=flat&logo=github)](https://github.com/votre-username)
[![LinkedIn](https://img.shields.io/badge/LinkedIn-Sona%20KOULIBALY-0077B5?style=flat&logo=linkedin)](https://linkedin.com/in/votre-profil)
[![Demo](https://img.shields.io/badge/Demo-Render-46E3B7?style=flat&logo=render)](https://assuranalytics.onrender.com)

---

## 📄 Licence

Projet académique — Mastère 2 Big Data & Data Stratégie.  

Tous droits réservés © 2026 Sona KOULIBALY.
