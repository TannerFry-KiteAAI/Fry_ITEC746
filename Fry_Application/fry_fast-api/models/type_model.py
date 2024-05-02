from fastapi_camelcase import CamelModel
from typing import Optional


class Type(CamelModel):
    typeid: Optional[str] = None
    media_type: Optional[str] = None
    checkout_time: Optional[str] = None