from fastapi_camelcase import CamelModel
from typing import Optional


class Loan(CamelModel):
    checkid: Optional[str] = None
    mediaid: Optional[str] = None
    clientid: Optional[str] = None
    dateout: Optional[str] = None
    datedue: Optional[str] = None