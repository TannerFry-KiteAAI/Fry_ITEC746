import uuid
from typing import List

from models.hold_model import Hold
from repositories.db_connection import DBConnection

GET_ALL = "SELECT h.holdid, m.title, c.first_name || ' ' || c.last_name AS Name, h.holddate, h.holdqueue FROM holds h JOIN media m on h.mediaid = m.mid JOIN client c on h.clientid = c.cid"
PLACE = "INSERT INTO holds (holdid, mediaid, clientid, holddate, holdqueue) VALUES (%s,%s,%s,CURRENT_DATE, 0 + (SELECT COUNT(*) FROM holds WHERE mediaid = %s))"
GET_BY_ID = "SELECT h.holdid, m.title, c.first_name || ' ' || c.last_name AS Name, h.holddate, h.holdqueue FROM holds h JOIN media m on h.mediaid = m.mid JOIN client c on h.clientid = c.cid WHERE h.holdid = %s"
UPDATE_QUEUE = "UPDATE holds SET holdqueue = holdqueue - 1 WHERE mediaid = (Select mediaid from holds where holdid = %s)"
REMOVE = "DELETE FROM holds where holdid=%s"

##Show all holds currently in database
def get_all_holds() -> List[Hold]:
    hold = []
    db = DBConnection()
    cur = db.get_cursor()
    cur.execute(GET_ALL)
    for row in cur:
        hold.append(Hold(holdid=str(row[0]), mediaid=str(row[1]), clientid=str(row[2]), holddate=str(row[3]), holdqueue=str(row[4])))
    return hold

##Place a hold, reserving a media to a client
def place_hold(hold: Hold) -> Hold:
    db = DBConnection()
    cur = db.get_cursor()
    uid = uuid.uuid4()
    cur.execute(PLACE, (
        uid,
        hold.mediaid,
        hold.clientid,
        hold.mediaid,
    ))
    db.connection.commit()
    return get_hold_by_id(hold.mediaid)

##Gets holds for a specific media
def get_hold_by_id(uid: uuid) -> Hold:
    db = DBConnection()
    cur = db.get_cursor()
    cur.execute(GET_BY_ID, [uid])
    for row in cur:
        hold = Hold(holdid=str(row[0]), mediaid=str(row[1]), clientid=str(row[2]), holddate=str(row[3]), holdqueue=str(row[4]))
        return hold

##Update holdqueue for all holds for a particular media. Gets this media from the holdid
def update_hold(hold: Hold) -> Hold:
    db = DBConnection()
    cur = db.get_cursor()
    uid = uuid.UUID(hold.holdid)
    cur.execute(UPDATE_QUEUE, [uid])
    db.connection.commit()
    return get_hold_by_id(uid)

##Removes a hold. In a live database, this would occur when a user checks out their hold, or if they cancel prior to checkout.
def remove(uid: uuid):
    db = DBConnection()
    cur = db.get_cursor()
    cur.execute(REMOVE, [uid])
    db.connection.commit()
    return