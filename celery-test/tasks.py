from celery import Celery
import os
import time
import signal
from celery.signals import worker_shutting_down, worker_process_shutdown, worker_shutdown



# Use environment variable for broker URL, default to localhost for development
broker_url = os.getenv('CELERY_BROKER_URL', 'redis://localhost:6379/0')
WAIT_SECONDS = int(os.getenv('WAIT_SECONDS', 50))  # Default to 50 seconds if not set

# @worker_shutting_down.connect
# def handle_worker_shutting_down(sig, how, **kwargs):
#     print(f"Worker is shutting down due to signal: {sig}, how: {how}", flush=True)
#     # Perform any necessary cleanup here
#     time.sleep(WAIT_SECONDS)
#     print("Cleanup complete. Worker has shut down.", flush=True)


# @worker_shutdown.connect
# def handle_worker_shutdown(sig, how, **kwargs):
#     print(f"Worker is shutting down due to signal: {sig}, how: {how}", flush=True)
#     # Perform any necessary cleanup here
#     time.sleep(WAIT_SECONDS)
#     print("Cleanup complete. Worker has shut down.", flush=True)

# @worker_process_shutdown.connect
# def handle_worker_process_shutdown(signal, **kwargs):
#     print(f"Worker process is shutting down due to:{signal} {kwargs}", flush=True)
#     # Perform any necessary cleanup here
#     time.sleep(WAIT_SECONDS)
#     print("Cleanup complete. Worker process has shut down.", flush=True)

app = Celery('tasks', broker=broker_url)

@app.task
def add(x, y):
    i = 0
    print(f"Starting task with x={x}, y={y}", flush=True)
    kill= time.time() + WAIT_SECONDS  # Default to 50 seconds if not set
    while True:
        if(time.time() > kill):
            print("Delay passed. Exiting now.", flush=True)
            break
        time.sleep(1)
        print(f"Doing something in a loop {i}: {x} + {y}", flush=True)
        i+=1
    return x + y


