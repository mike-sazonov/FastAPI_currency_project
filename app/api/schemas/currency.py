from pydantic import BaseModel


class CurrentConvert(BaseModel):
    from_code: str
    to_code: str
    amount: str = '1'
