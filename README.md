# THE WALLET 😈

Moteur de pronostics sportifs — socle technique expérimental.

## État
Le planificateur et la base SQLite fonctionnent. Aucun fournisseur de données sportives, modèle prédictif calibré, ou publication automatique de pronostics n'est encore opérationnel. **Aucune sélection ne doit être inventée.**

## Démarrage
1. Copier `.env.example` vers `.env`.
2. Installer les dépendances : `pip install -r requirements.txt`.
3. Tester un cycle : `python -m app.main --once`.
4. Démarrer le planificateur : `python -m app.main`.

Le cycle s'exécute tous les jours à minuit, fuseau Europe/Brussels. Sans fournisseur de données il consigne `no_provider_configured` et ne publie rien.

## Docker
`docker compose up -d --build`

## Telegram
Créer un bot avec BotFather et placer son token dans la variable d'environnement `TELEGRAM_BOT_TOKEN` (jamais dans Git). Commandes : /start, /status, /preview.

## Prochaines étapes
Brancher des fournisseurs autorisés de calendriers, statistiques et cotes; mesurer la qualité et la fraîcheur des données; construire des modèles par sport et les backtester; implémenter validation humaine et publication contrôlée; déployer sur une machine cloud avec volume persistant.

Les catégories de confiance ne garantissent aucun gain. Les mises en pourcentage de bankroll ne sont pas des probabilités.
