from datetime import datetime

now = datetime.now()
current_time = now.strftime("%H:%M:%S")
print("Current Time = ", current_time)
present = now.strftime("%d/%m/%y")
print("Present Date = ", present)