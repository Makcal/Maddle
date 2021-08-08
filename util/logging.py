from common import flask_stream, maddle_stream
from .time import get_msk_time


def start_logging():
    start_line = f"================{get_msk_time()}================\n"
    flask_stream.write(start_line)
    maddle_stream.write(start_line)

def log(message):
    maddle_stream.write(f"{get_msk_time()} - {message}\n")
