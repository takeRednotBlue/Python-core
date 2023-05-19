from datetime import datetime

seventh_day_2020 = datetime(year=2020, month=1, day=7, hour=14)
ts = seventh_day_2020.timestamp()
print(ts)   # 1578398400.0
print(datetime.fromtimestamp(ts))   # 2020-01-08 17:46:40

ts += 100_000
print(ts)   # 1578398400.0
print(datetime.fromtimestamp(ts))   # 2020-01-08 17:46:40

print(type(100_000))