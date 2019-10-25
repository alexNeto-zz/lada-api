# https://github.com/reddit-archive/reddit/blob/master/r2/r2/lib/db/_sorts.pyx

from datetime import datetime
from math import log

epoch = datetime(1970, 1, 1)


def epoch_seconds(date: datetime) -> float:
    td = date - epoch
    return td.days * 86400 + td.seconds + (float(td.microseconds) / 1000000)


def score(ups: int, downs: int) -> int:
    return ups - downs


def ranking(ups: int, downs: int, date: datetime) -> float:
    s = score(ups, downs)
    order = log(max(abs(s), 1), 10)
    sign = 1 if s > 0 else -1 if s < 0 else 0
    seconds = epoch_seconds(date) - 1134028003
    return round(sign * order + seconds / 45000, 7)


def default_rank():
    return ranking(0, 0, datetime.now())
