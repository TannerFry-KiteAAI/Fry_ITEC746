from fastapi_camelcase import CamelModel
from typing import Optional


class Media(CamelModel):
    mid: Optional[str] = None
    title: Optional[str] = None
    dewey: Optional[str] = None
    location: Optional[str] = None
    mediatype: Optional[str] = None
    cancheck: Optional[str] = None