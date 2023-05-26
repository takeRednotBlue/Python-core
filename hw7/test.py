# from datetime import datetime

# seventh_day_2020 = datetime(year=2020, month=1, day=7, hour=14)
# ts = seventh_day_2020.timestamp()
# print(ts)   # 1578398400.0
# print(datetime.fromtimestamp(ts))   # 2020-01-08 17:46:40

# ts += 100_000
# print(ts)   # 1578398400.0
# print(datetime.fromtimestamp(ts))   # 2020-01-08 17:46:40

# print(type(100_000))

from datetime import datetime, timedelta

py_core_end = datetime(2023, 7, 16)
wed_duration = timedelta(weeks=16)

project_start = py_core_end + wed_duration

print(project_start)