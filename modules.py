import datetime
# - also can work from datetime import datetime # importing datetime from datetime module
import time

today = datetime.date.today()

timestamp = time.time()  # get the current timestamp

print(f"Current timestamp: {timestamp}")
print(f"Current date and time: {datetime.datetime.now()}")
print(f"Current date: {datetime.date.today()}")
print(f"Today's date is: {today}")
