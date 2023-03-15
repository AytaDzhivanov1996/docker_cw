from datetime import datetime, timedelta

from celery import shared_task

from tracker.models import Habit
from tracker.telegram import send_message


@shared_task
def check_time():
    time = datetime.now().time
    start_time = datetime.now() - timedelta(minutes=1)
    habit_data = Habit.objects.filter(time_gte=start_time)
    for item in habit_data.filter(time_lte=time):
        text = f'я буду {item.action} в {item.time} в {item.place}'
        send_message(text)
