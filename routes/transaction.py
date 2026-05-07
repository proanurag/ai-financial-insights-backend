from fastapi import APIRouter
from schemas.transaction import Transaction as TransactionRequest
from database import SessionLocal
from models.transaction import Transaction
from fastapi import UploadFile, File
import csv
from io import StringIO
from datetime import datetime

router = APIRouter()

@router.post("/")
def add_transaction(body: TransactionRequest):
    db = SessionLocal()
    txn = Transaction(**body.model_dump())
    db.add(txn)
    db.commit()
    db.refresh(txn)
    db.close()
    return txn

@router.get("/")    
def get_transactions():
    db=SessionLocal()
    data=db.query(Transaction).all()
    db.close()
    result = []
    for i in data:
        result.append({"amount": i.amount, "category": i.category, "date": i.date})
    return result

@router.post('/upload')
def file_upload(file: UploadFile = File(...)):
    contents =file.file.read().decode('utf-8')
    reader = csv.DictReader(StringIO(contents))
    db= SessionLocal()
    for row in reader:
        transactions = Transaction(
            amount = row['amount'],
            category = row['category'],
            date = datetime.strptime(row['date'], '%Y-%m-%d').date()
        )
        db.add(transactions)
    db.commit()
    db.close()
    return {"message": "File uploaded successfully"}

