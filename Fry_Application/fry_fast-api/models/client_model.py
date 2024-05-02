from fastapi_camelcase import CamelModel
from typing import Optional


class Client(CamelModel):
    cid: Optional[str] = None
    first_name: Optional[str] = None
    last_name: Optional[str] = None
    street_address: Optional[str] = None
    postal: Optional[str] = None
    phone: Optional[str] = None
    email: Optional[str] = None
    pswd: Optional[str] = None