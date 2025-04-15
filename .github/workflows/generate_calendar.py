from ics import Calendar, Event
from datetime import datetime, timedelta
import pytz

def create_event(title, description, date, start_hour=9, duration_mins=30):
    event = Event()
    est = pytz.timezone("US/Eastern")
    start = est.localize(datetime(date.year, date.month, date.day, start_hour, 30))
    end = start + timedelta(minutes=duration_mins)
    event.name = title
    event.begin = start
    event.end = end
    event.description = description
    return event

today = datetime.now(pytz.timezone("US/Eastern"))
monday = today - timedelta(days=today.weekday())

c = Calendar()

# 本周事件示例
c.events.add(create_event("Tesla 本周关键压力位测试", "观察是否反弹至 170 并回落", monday + timedelta(days=1)))
c.events.add(create_event("Intel 技术回踩日", "观察 39.80 压力位情况", monday + timedelta(days=2)))
c.events.add(create_event("宏观风险日", "初请+地缘政治干扰波动", monday + timedelta(days=3)))

with open("short_term_trading.ics", "w") as f:
    f.writelines(c.serialize_iter())
