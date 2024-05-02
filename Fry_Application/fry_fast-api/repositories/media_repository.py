import uuid
from typing import List

from models.media_model import Media
from repositories.db_connection import DBConnection

GET_ALL = "SELECT mid, title, dewey, loc, medtype, cancheckout from media"
INSERT = "INSERT INTO media (mid, title, dewey, loc, medtype, cancheckout) VALUES (%s,%s,%s,%s,%s,%s)"
GET_BY_ID = "SELECT mid, title, dewey, loc, medtype, cancheckout from media WHERE mid = %s"
UPDATE = "UPDATE media set title=%s, dewey=%s, loc=%s, medtype=%s, cancheckout=%s WHERE mid = %s"
DELETE = "DELETE FROM media where mid=%s"

##Gets all media items in database. In live situation, this would require additional filtering
def get_all_media() -> List[Media]:
    media = []
    db = DBConnection()
    cur = db.get_cursor()
    cur.execute(GET_ALL)
    for row in cur:
        media.append(Media(mid=str(row[0]), title=row[1], dewey=str(row[2]), location=str(row[3]), mediatype=str(row[4]), cancheck=str(row[5])))
    return media

##Creates a new media entity
def create_media(media: Media) -> Media:
    db = DBConnection()
    cur = db.get_cursor()
    uid = uuid.uuid4()
    cur.execute(INSERT, (
        uid,
        media.title,
        media.dewey,
        media.location,
        media.mediatype,
        media.cancheck
    ))
    db.connection.commit()
    return get_media(uid)

##Gets details on singular media item with provided id
def get_media(uid: uuid) -> Media:
    db = DBConnection()
    cur = db.get_cursor()
    cur.execute(GET_BY_ID, [uid])
    for row in cur:
        media = Media(mid=str(row[0]), title=row[1], dewey=str(row[2]), location=str(row[3]), mediatype=str(row[4]), cancheck=str(row[5]))
        return media

##Updates details of singular media item with provided id
def update_media(media: Media) -> Media:
    db = DBConnection()
    cur = db.get_cursor()
    uid = uuid.UUID(media.mid)
    cur.execute(UPDATE, (media.title, media.dewey, media.location, media.mediatype, media.cancheck, uid))
    db.connection.commit()
    return get_media(uid)

##Deletes media item with provided id
def delete_media(uid: uuid):
    db = DBConnection()
    cur = db.get_cursor()
    cur.execute(DELETE, [uid])
    db.connection.commit()
    return