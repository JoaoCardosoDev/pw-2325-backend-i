

import json
import random
from fastapi import APIRouter


router= APIRouter(prefix="/trivia", tags=["Trivia"])


@router.get("")
def get_random_question():
    with open('trivia.json') as file:
        triviadb = json.load(file)
        idx = random.randint(0, len(triviadb) - 1)
        return triviadb