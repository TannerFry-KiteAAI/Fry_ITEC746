import uuid
from typing import List

from models.client_model import Client
from repositories.db_connection import DBConnection

GET_ALL = "SELECT cid, first_name, last_name, street_address, postal, phone, email, pswd from client"
INSERT = "INSERT INTO client (cid, first_name, last_name, street_address, postal, phone, email, pswd) VALUES (%s,%s,%s,%s,%s,%s,%s,%s)"
GET_BY_ID = "SELECT cid, first_name, last_name, street_address, postal, phone, email, pswd from client WHERE cid = %s"
UPDATE = "UPDATE client set pswd='none' WHERE cid = %s"
DELETE = "DELETE FROM client where cid=%s"

##Get all clients currently in database
def get_all_client() -> List[Client]:
    client = []
    db = DBConnection()
    cur = db.get_cursor()
    cur.execute(GET_ALL)
    for row in cur:
        client.append(Client(cid=str(row[0]), first_name=row[1], last_name=row[2], street_address=row[3], postal=str(row[4]), phone=row[5], email=row[6], pswd=row[7]))
    return client

##Add new client to database
def create_client(client: Client) -> Client:
    db = DBConnection()
    cur = db.get_cursor()
    uid = uuid.uuid4()
    cur.execute(INSERT, (
        uid,
        client.first_name,
        client.last_name,
        client.street_address,
        client.postal,
        client.phone,
        client.email,
        client.pswd
    ))
    db.connection.commit()
    return get_client(uid)

##Get a single client with the provided id
def get_client(uid: uuid) -> Client:
    db = DBConnection()
    cur = db.get_cursor()
    cur.execute(GET_BY_ID, [uid])
    for row in cur:
        client = Client(cid=str(row[0]), first_name=row[1], last_name=row[2], street_address=row[3], postal=str(row[4]), phone=row[5], email=row[6], pswd=row[7])
        return client

##Update client. In this case, client has too many overdue books. Set password to null
def update_client(client: Client) -> Client:
    db = DBConnection()
    cur = db.get_cursor()
    uid = uuid.UUID(client.cid)
    cur.execute(UPDATE, [uid])
    db.connection.commit()
    return get_client(uid)

##Remove client
def delete_client(uid: uuid):
    db = DBConnection()
    cur = db.get_cursor()
    cur.execute(DELETE, [uid])
    db.connection.commit()
    return