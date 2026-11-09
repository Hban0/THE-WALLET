import asyncio
import logging
from apscheduler.schedulers.asyncio import AsyncIOScheduler
from apscheduler.triggers.cron import CronTrigger
from app.config import settings
from app.core.pipeline import run_daily_cycle

log = logging.getLogger(__name__)

async def start_scheduler() -> None:
    scheduler = AsyncIOScheduler(timezone=settings.timezone)
    scheduler.add_job(
        run_daily_cycle,
        CronTrigger(hour=0, minute=0, timezone=settings.timezone),
        id="daily_sports_analysis",
        replace_existing=True,
        max_instances=1,
        coalesce=True,
    )
    scheduler.start()
    log.info("Scheduler actif : tous les jours à 00:00 (%s).", settings.timezone)
    try:
        while True:
            await asyncio.sleep(3600)
    finally:
        scheduler.shutdown(wait=False)
