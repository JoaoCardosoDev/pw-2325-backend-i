

import json
from typing import List


def get_products(db_path:str)->List[dict]:
    result=[]
    with open(db_path,"r") as data:
        result=json.loads(data.readlines())
    return result