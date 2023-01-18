from apscheduler.schedulers.background import BackgroundScheduler
from .hackernewsapi import update_news

def start():
    scheduler = BackgroundScheduler()
    scheduler.add_job(update_news, 'interval', minutes=5)
    scheduler.start()