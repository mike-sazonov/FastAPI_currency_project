from fastapi import APIRouter, Depends, HTTPException
from typing import Annotated

from app.utils.external_api import get_convert, get_list
from app.api.schemas.currency import CurrentConvert
from app.core.security import get_user_from_token, get_user_from_db


currency_router = APIRouter(
    prefix="/currency"
)


@currency_router.get("/exchange")
def convert_currency(
        from_code: str, to_code: str, amount: str, current_user: Annotated[str, Depends(get_user_from_token)]
):
    user = get_user_from_db(current_user)
    if user is None:
        raise HTTPException(status_code=403, detail="Not authorized")
    return get_convert(CurrentConvert(from_code=from_code, to_code=to_code, amount=amount))


@currency_router.get("/list")
def currency_list(current_user: Annotated[str, Depends(get_user_from_token)]):
    user = get_user_from_db(current_user)
    if user is None:
        raise HTTPException(status_code=403, detail="Not authorized")
    return get_list()
