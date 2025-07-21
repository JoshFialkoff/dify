import os
import time

from dify_app import Flask


def init_app(app: Flask):
    os.environ["TZ"] = "UTC"
    # windows platform not support tzset
    if hasattr(time, "tzset"):
        time.tzset()
