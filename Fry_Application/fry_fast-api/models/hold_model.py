from fastapi_camelcase import CamelModel
from typing import Optional


class Hold(CamelModel):
    holdid: Optional[str] = None
    mediaid: Optional[str] = None
    clientid: Optional[str] = None
    holddate: Optional[str] = None
    holdqueue: Optional[str] = None