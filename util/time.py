from datetime import datetime, timedelta, timezone


def get_msk_time():
    tz = timezone(timedelta(hours=3))  # UTC+3 - Moscow (MSK)
    return datetime.now(tz)
