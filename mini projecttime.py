import time
from datetime import datetime
import os
from zoneinfo import ZoneInfo
while True:
    os.system("cls")
    current_time = datetime.now(ZoneInfo("Asia/Kolkata"))
    print("DIGITAL CLOCK")
    print("Date:",current_time.strftime("%D-%m-%Y"))
    print("Day:",current_time.strftime("%A"))
    print("time:",current_time.strftime("%I:%M:%S %p"))
    print("Zone:","Indian Standard Time (IST)")
    time.sleep(1)
