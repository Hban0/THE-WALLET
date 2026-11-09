# État d'implémentation

## Fonctionnel dans le socle
- Planification quotidienne à minuit, heure Europe/Brussels
- Schéma SQLite (cycles, matchs, pronostics, résultats)
- Calcul des probabilités implicites et espérance de valeur
- Contrôle minimum de qualité des données
- Bot Telegram optionnel : /start, /status, /preview
- Docker et tests unitaires

## Non implémenté
- Collecte de données sportives réelles
- Modèles de prévision calibrés par sport
- Vérification des compositions et blessures
- Suivi des cotes, validation et publication automatique
- Déploiement cloud

Sans fournisseur, les cycles enregistrent no_provider_configured et produisent zéro sélection.
