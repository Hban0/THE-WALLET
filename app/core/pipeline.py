import logging
from datetime import datetime, timezone
from app.database.db import connect

log = logging.getLogger(__name__)

async def run_daily_cycle() -> dict:
    started = datetime.now(timezone.utc).isoformat()
    con = connect()
    try:
        cur = con.execute(
            "INSERT INTO cycles(started_at, status, details) VALUES (?, ?, ?)",
            (started, "no_provider_configured",
             "Cycle exécuté ; aucun fournisseur sportif actif ; aucune sélection générée.")
        )
        con.commit()
        cycle_id = cur.lastrowid
    finally:
        con.close()
    log.warning("Cycle %s terminé sans données sportives connectées.", cycle_id)
    return {"cycle_id": cycle_id, "status": "no_provider_configured", "predictions": 0}
