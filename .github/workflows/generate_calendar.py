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

# Tesla
c.events.add(create_event(
    "Tesla 本周做空观察点",
    "Q1交付后走势弱于市场，ASP 拖累整体表现，周内反弹乏力可寻找做空窗口。",
    monday + timedelta(days=1)
))

# Intel
c.events.add(create_event(
    "Intel 本周反弹顶部预警",
    "AI 噱头兑现短期利好后，反弹动能弱，警惕 $39.80 压力位回落。",
    monday + timedelta(days=2)
))

# 宏观预警
c.events.add(create_event(
    "初请 + 地缘风险监控日",
    "周四关注地缘政治及VIX波动可能带来的短期空头机会。",
    monday + timedelta(days=3)
))

with open("short_term_trading.ics", "w") as f:
    f.writelines(c.serialize_iter())
