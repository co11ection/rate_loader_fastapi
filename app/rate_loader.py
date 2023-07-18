import json
from models import InsuranceRate


def load_rates_from_json(file_path: str):
    with open(file_path) as file:
        rates = json.load(file)
        for rate in rates:
            InsuranceRate.create(cargo_type=rate['cargo_type'], rate=rate['rate'])
