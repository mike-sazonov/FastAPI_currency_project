import requests
from fastapi import HTTPException

from app.core.config import settings
from app.api.schemas.currency import CurrentConvert


EXTERNAL_API_URL = "https://api.currencybeacon.com/v1"


def get_convert(convert_pare: CurrentConvert):
    response = requests.get(EXTERNAL_API_URL + "/convert", params={
        "from": convert_pare.from_code,
        "to": convert_pare.to_code,
        "amount": convert_pare.amount,
        "api_key": settings.API_KEY})
    if response.status_code == 200:
        return response.json()["response"]["value"]
    else:
        raise HTTPException(status_code=400, detail="Bad currency code")


def get_list():
    response = requests.get(EXTERNAL_API_URL + "/latest", params={"api_key": settings.API_KEY})
    if response.status_code == 200:
        return response.json()
    else:
        return None
