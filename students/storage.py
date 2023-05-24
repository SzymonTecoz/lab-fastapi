from functools import lru_cache
from fastapi import Depends, FastAPI
from . import config

app = FastAPI()

@lru_cache()
def get_students():
    return config.Students()