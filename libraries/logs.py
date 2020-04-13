import logging
import os
import sys
import io
import time
from logging.handlers import RotatingFileHandler
from logging import handlers
import datetime as dt
from datetime import date, datetime


def get_logger(ar_log_path, ar_file_name="Unknow", ar_log_level=10):


    logName = os.path.join(ar_log_path, "{}_{}.log".format(ar_file_name,datetime.now().strftime("%Y%m%d%H%M%S")))
    logger = None
    try:

        logger = logging.getLogger(ar_file_name)
        logger.setLevel(ar_log_level)
        format = logging.Formatter("%(asctime)s - [%(levelname)s] - [%(name)s] : %(message)s")

        loginStreamHandler = logging.StreamHandler(sys.stdout)
        loginStreamHandler.setFormatter(format)
        logger.addHandler(loginStreamHandler)

        fileHandler = handlers.RotatingFileHandler(logName, maxBytes=(1048576*5), backupCount=7)
        fileHandler.setFormatter(format)
        logger.addHandler(fileHandler)


    except Exception as Exc:
        print(str(Exc))
        logger = None
    return logger