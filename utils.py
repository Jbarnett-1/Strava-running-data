import json
import re
import sys
import math
from datetime import datetime, timedelta

def format_time(time):
    hh, mm, ss = "", "", ""
    if len(time) > 1:
        ss = time[-2:]
        time_chopped = time[:-2]
    else:
        ss = time
    if len(time_chopped) > 1:
        mm = time_chopped[-2:]
        time_chopped = time_chopped[:-2]
    else:
        mm = time_chopped
    if len(time_chopped) > 0:
        hh = time_chopped
    formatted_time = ""
    if hh:
        hh = int(hh)
    else:
        hh = 0
    if mm:
        mm = int(mm)
    else:
        mm = 0
    if ss:
        ss = int(ss)
    else:
        ss = 0
    minutes = hh * 60 + mm + ss / 60
    return minutes

def get_pace(minutes, distance):
    pace = float(minutes) / float(distance)
    pace_min = math.floor(pace)
    remainder = round(60 * (pace - pace_min))
    return f"{pace_min}:{remainder}"

def get_dates(string=False, days=3, frmt="%Y-%m-%d"):
    dates = []
    for day in range(0, days):
        yesterday = datetime.now() - timedelta(day)
        yesterday = datetime.strftime(yesterday, frmt)
        dates.append(yesterday)
    return dates