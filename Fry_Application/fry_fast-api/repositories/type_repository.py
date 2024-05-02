from typing import List

from models.type_model import Type
from repositories.db_connection import DBConnection

GET_ALL = "SELECT typeid, media_type, checkout_time from type"
INSERT = "INSERT INTO type (typeid, media_type, checkout_time) VALUES (%s,%s,%s)"
GET_BY_ID = "SELECT typeid, media_type, checkout_time from type where typeid = %s"
UPDATE = "UPDATE type set media_type=%s, checkout_time=%s WHERE typeid = %s"
DELETE = "DELETE FROM type where typeid=%s"

###Returns all existing type entities
def get_all_types() -> List[Type]:
    type = []
    db = DBConnection()
    cur = db.get_cursor()
    cur.execute(GET_ALL)
    for row in cur:
        type.append(Type(typeid=str(row[0]), media_type=row[1], checkout_time=str(row[2])))
    return type

##Adds a new type to database
def create_type(type: Type) -> Type:
    db = DBConnection()
    cur = db.get_cursor()
    cur.execute(INSERT, (
        type.typeid,
        type.media_type,
        type.checkout_time
    ))
    db.connection.commit()
    return get_type(type.typeid)

##Gets type with provided id
def get_type(id: int) -> Type:
    db = DBConnection()
    cur = db.get_cursor()
    cur.execute(GET_BY_ID, [id])
    for row in cur:
        type = Type(typeid=str(row[0]), media_type=row[1], checkout_time=str(row[2]))
        return type

##Updates type with provided id
def update_type(type: Type) -> Type:
    db = DBConnection()
    cur = db.get_cursor()
    id = int(type.typeid)
    cur.execute(UPDATE, (type.media_type, type.checkout_time, id))
    db.connection.commit()
    return get_type(id)

##Delete type with provided id
def delete_type(id: int):
    db = DBConnection()
    cur = db.get_cursor()
    cur.execute(DELETE, [id])
    db.connection.commit()
    return