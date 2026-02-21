from datetime import date
from decimal import Decimal
from typing import Any


class Fator_b3: 
    rate: Decimal
    last_date_prior: date
    isin: str

    @classmethod
    def from_model(cls,model:dict):
        obj = cls()
        obj.isin = model['isin']
        obj.rate = model["rate"]
        obj.last_date_prior = model["last_date_prior"]
        return obj