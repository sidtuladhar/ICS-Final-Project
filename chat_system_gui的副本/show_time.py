import time
from datetime import datetime

while True:
    now = datetime.now()
    current_time = now.strftime("%I:%M %p")
    current_second = now.strftime("%S")
    print(f"\033cClock: {current_time}\nSeconds: {current_second}")
    time.sleep(1)