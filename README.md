# -House-Price-Predictor-
🏠 House Price Predictor - Real-Time Dashboard
Une application web interactive et ultra-rapide construite avec Streamlit pour estimer la valeur des biens immobiliers en temps réel.

🚀 Concept "No-Scroll"
Cette interface a été optimisée pour tenir sur un seul écran :

Split-Screen : Les paramètres à gauche, le résultat à droite.

Zéro Clic : Pas de bouton "Prédire". Le prix s'actualise instantanément dès que vous modifiez une valeur.

Design Premium : Interface en mode sombre avec dégradés personnalisés.

📁 Structure du Projet
Pour que l'application fonctionne, votre dossier doit contenir :

dashboard.py : Le code principal de l'application.

house_model.pkl : Votre modèle de Machine Learning entraîné.

model_columns.pkl : La liste des colonnes utilisée pour l'entraînement (One-Hot Encoding).

🛠️ Installation et Utilisation
1. Cloner ou télécharger le projet
Assurez-vous d'avoir Python installé (3.8 ou plus).

2. Lancer l'application
Exécutez la commande suivante :

streamlit run app.py

📊 Caractéristiques Prises en Compte
L'algorithme analyse 12 variables clés pour estimer le prix :

Dimensions : Surface (sqft), Nombre de chambres, salles de bain, étages.

Localisation : Accès route principale, zone préférentielle.

Équipements : Climatisation, parking, sous-sol, chambre d'amis.

État : Statut de l'ameublement (Meublé, Semi-meublé, Non-meublé).

💡 Technologies Utilisées
Python (Langage de base)

Streamlit (Interface UI & Serveur)

Pandas (Manipulation des données)

Scikit-learn (Moteur de prédiction)
pip install -r requirements.txt
