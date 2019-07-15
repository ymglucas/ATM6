from core import src
from conf.settings import LOGGING_DIC
import logging.config
logging.config.dictConfig(LOGGING_DIC)


def auth(func):
    def inner(*args,**kwargs):
        if src.user_info['name']:
            return func(*args,**kwargs)
        else:
            src.login()
    return inner


def get(name):
    return logging.getLogger(name)