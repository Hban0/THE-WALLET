import logging
from telegram import Update
from telegram.ext import Application, CommandHandler, ContextTypes
from app.config import settings
from app.database.db import connect

log = logging.getLogger(__name__)

async def start(update: Update, context: ContextTypes.DEFAULT_TYPE) -> None:
    await update.message.reply_text(
        "THE WALLET 😈 — Sports Intelligence\n"
        "Moteur en construction. Aucune sélection n'est publiée sans données vérifiées.\n"
        "Commandes : /status /preview"
    )

async def status(update: Update, context: ContextTypes.DEFAULT_TYPE) -> None:
    con = connect()
    try:
        row = con.execute(
            "SELECT status, started_at FROM cycles ORDER BY id DESC LIMIT 1"
        ).fetchone()
    finally:
        con.close()
    if row:
        msg = f"Dernier cycle : {row['status']}\nDébut : {row['started_at']}"
    else:
        msg = "Aucun cycle exécuté pour le moment."
    await update.message.reply_text(msg)

async def preview(update: Update, context: ContextTypes.DEFAULT_TYPE) -> None:
    await update.message.reply_text(
        "Aucun pronostic validé disponible. Le système ne génère pas de sélections "
        "sans calendrier, statistiques et cotes vérifiables."
    )

def build_application() -> Application | None:
    if not settings.telegram_token:
        log.info("Telegram désactivé : TELEGRAM_BOT_TOKEN absent.")
        return None
    app = Application.builder().token(settings.telegram_token).build()
    app.add_handler(CommandHandler("start", start))
    app.add_handler(CommandHandler("status", status))
    app.add_handler(CommandHandler("preview", preview))
    return app
