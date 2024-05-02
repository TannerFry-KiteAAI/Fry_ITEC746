import uuid
from typing import List

from models.loan_model import Loan
from repositories.db_connection import DBConnection

GET_ALL = "SELECT l.checkid, m.title, c.first_name || ' ' || c.last_name AS Name, l.dateout, l.datedue FROM loans l JOIN media m on l.mediaid = m.mid JOIN client c on l.clientid = c.cid"
CHECKOUT = "INSERT INTO loans (checkid, mediaid, clientid, dateout, datedue) VALUES (%s,%s,%s,CURRENT_DATE, CURRENT_DATE + interval '1 week' * (select checkout_time from type where typeid = (select medtype from media where mid = %s)))"
GET_BY_ID = "SELECT l.checkid, m.title, c.first_name || ' ' || c.last_name AS Name, l.dateout, l.datedue FROM loans l JOIN media m on l.mediaid = m.mid JOIN client c on l.clientid = c.cid WHERE checkid = %s"
RENEW = "UPDATE loans SET datedue = datedue + interval '1 week' * (SELECT checkout_time FROM type WHERE typeid = (SELECT medtype FROM media where mid = mediaid)) where checkid = %s"
CHECKIN = "DELETE FROM loans where checkid=%s"

##Show all loans currently in database
def get_all_loans() -> List[Loan]:
    loan = []
    db = DBConnection()
    cur = db.get_cursor()
    cur.execute(GET_ALL)
    for row in cur:
        loan.append(Loan(checkid=str(row[0]), mediaid=str(row[1]), clientid=str(row[2]), dateout=str(row[3]), datedue=str(row[4])))
    return loan

##Creates a loan, checking out a media to a client
def check_out(loan: Loan) -> Loan:
    db = DBConnection()
    cur = db.get_cursor()
    uid = uuid.uuid4()
    cur.execute(CHECKOUT, (
        uid,
        loan.mediaid,
        loan.clientid,
        loan.mediaid,
    ))
    db.connection.commit()
    return get_loan_by_id(uid)

##Get details on a loan based on a single id
def get_loan_by_id(uid: uuid) -> Loan:
    db = DBConnection()
    cur = db.get_cursor()
    cur.execute(GET_BY_ID, [uid])
    for row in cur:
        loan = Loan(checkid=str(row[0]), mediaid=str(row[1]), clientid=str(row[2]), dateout=str(row[3]), datedue=str(row[4]))
        return loan

##Renews a loan, extending its due date
def renew(loan: Loan) -> Loan:
    db = DBConnection()
    cur = db.get_cursor()
    uid = uuid.UUID(loan.checkid)
    cur.execute(RENEW, [uid])
    db.connection.commit()
    return get_loan_by_id(uid)

##Checks in a loan, effectively deleting it
def check_in(uid: uuid):
    db = DBConnection()
    cur = db.get_cursor()
    cur.execute(CHECKIN, [uid])
    db.connection.commit()
    return