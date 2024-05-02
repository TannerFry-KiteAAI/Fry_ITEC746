import uuid

from fastapi import FastAPI, HTTPException
from typing import List

from models.media_model import Media
from models.client_model import Client
from models.loan_model import Loan
from models.hold_model import Hold
from models.type_model import Type
from repositories.media_repository import get_all_media, create_media, get_media, update_media, delete_media
from repositories.client_repository import get_all_client, create_client, get_client, update_client, delete_client
from repositories.loan_repository import get_all_loans, check_out, get_loan_by_id, renew, check_in
from repositories.hold_repository import get_all_holds, place_hold, get_hold_by_id, update_hold, remove
from repositories.type_repository import get_all_types, create_type, get_type, update_type, delete_type
app = FastAPI()


@app.get("/media")
def get_all_media_api() -> List[Media]:
    return get_all_media()


@app.post("/media")
def create_media_api(media: Media) -> Media:
    return create_media(media)


@app.get("/media/{media_id}")
def get_media_api(media_id: str) -> Media:
    mid = uuid.UUID(media_id)
    media = get_media(mid)
    return media


@app.put("/media/{media_id}")
def update_media_api(media_id: str, media: Media) -> Media:
    if media_id != media.mid:
        raise HTTPException(status_code=400, detail="path id and object id must match")
    return update_media(media)


@app.delete("/media/{media_id}")
def delete_media_api(media_id: str):
    mid = uuid.UUID(media_id)
    delete_media(mid)


@app.get("/client")
def get_all_client_api() -> List[Client]:
    return get_all_client()


@app.post("/client")
def create_client_api(client: Client) -> Client:
    return create_client(client)


@app.get("/client/{client_id}")
def get_client_api(client_id: str) -> Client:
    cid = uuid.UUID(client_id)
    client = get_client(cid)
    return client


@app.put("/client/{client_id}")
def update_client_api(client_id: str, client: Client) -> Client:
    if client_id != client.cid:
        raise HTTPException(status_code=400, detail="path id and object id must match")
    return update_client(client)


@app.delete("/client/{client_id}")
def delete_client_api(client_id: str):
    cid = uuid.UUID(client_id)
    delete_client(cid)


@app.get("/loan")
def get_all_loans_api() -> List[Loan]:
    return get_all_loans()


@app.post("/loan")
def check_out_api(loan: Loan) -> Loan:
    return check_out(loan)


@app.get("/loan/{check_id}")
def get_loan_by_id_api(check_id: str) -> Loan:
    checkid = uuid.UUID(check_id)
    loan = get_loan_by_id(checkid)
    return loan


@app.put("/loan/{check_id}")
def renew_api(check_id: str, loan: Loan) -> Loan:
    if check_id != loan.checkid:
        raise HTTPException(status_code=400, detail="path id and object id must match")
    return renew(loan)


@app.delete("/loan/{check_id}")
def check_in_api(check_id: str):
    checkid = uuid.UUID(check_id)
    check_in(checkid)


@app.get("/hold")
def get_all_holds_api() -> List[Hold]:
    return get_all_holds()


@app.post("/hold")
def check_out_api(hold: Hold) -> Hold:
    return place_hold(hold)


@app.get("/hold/{hold_id}")
def get_hold_by_id_api(hold_id: str) -> Hold:
    holdid = uuid.UUID(hold_id)
    hold = get_hold_by_id(holdid)
    return hold


@app.put("/hold/{hold_id}")
def update_hold_api(hold_id: str, hold: Hold) -> Hold:
    if hold_id != hold.holdid:
        raise HTTPException(status_code=400, detail="path id and object id must match")
    return update_hold(hold)


@app.delete("/hold/{hold_id}")
def remove_api(hold_id: str):
    holdid = uuid.UUID(hold_id)
    remove(holdid)


@app.get("/type")
def get_all_type_api() -> List[Type]:
    return get_all_types()


@app.post("/type")
def create_type_api(type: Type) -> Type:
    return create_type(type)


@app.get("/type/{type_id}")
def get_type_api(type_id: str) -> Type:
    typeid = int(type_id)
    type = get_type(typeid)
    return type


@app.put("/type/{type_id}")
def update_type_api(type_id: str, type: Type) -> Type:
    if type_id != type.typeid:
        raise HTTPException(status_code=400, detail="path id and object id must match")
    return update_type(type)


@app.delete("/type/{type_id}")
def delete_type_api(type_id: str):
    typeid = int(type_id)
    delete_type(typeid)

