from celery import Celery
import time

app = Celery('tasks')
app.config_from_object('celeryconfig')

@app.task
def add(x, y):
    return x + y

@app.task
def sleep(t):
    time.sleep(t)
    return 'finished'
