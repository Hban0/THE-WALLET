import argparse
import asyncio
import logging
from app.core.logging_config import configure_logging
from app.core.pipeline import run_daily_cycle
from app.core.scheduler import start_scheduler
from app.telegram.bot import build_application

async def main(once: bool = False) -> None:
    configure_logging()
    log = logging.getLogger(__name__)
    if once:
        result = await run_daily_cycle()
        log.info("Résultat du cycle : %s", result)
        return

    telegram = build_application()
    if telegram:
        await telegram.initialize()
        await telegram.start()
        if telegram.updater:
            await telegram.updater.start_polling()
    try:
        await start_scheduler()
    finally:
        if telegram:
            if telegram.updater:
                await telegram.updater.stop()
            await telegram.stop()
            await telegram.shutdown()

if __name__ == "__main__":
    parser = argparse.ArgumentParser()
    parser.add_argument("--once", action="store_true", help="Exécuter un cycle puis quitter")
    args = parser.parse_args()
    asyncio.run(main(once=args.once))
