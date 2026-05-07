from database import SessionLocal
from models.transaction import Transaction
from datetime import datetime

def fetch_transactions(filters: dict):
    db = SessionLocal()
    query = db.query(Transaction)

    # Category filter
    if filters.get("category"):
        query = query.filter(Transaction.category == filters["category"])

    data = query.all()
    db.close()

    # Time filtering (simple version)
    if filters.get("time_range") == "this_month":
        current_month = datetime.now().month
        data = [t for t in data if t.date.month == current_month]

    return [
        {
            "amount": t.amount,
            "category": t.category,
            "date": t.date.isoformat()
        }
        for t in data
    ]


def get_category_breakdown(data):
    result = {}

    for t in data:
        category = t["category"]
        amount = t["amount"]

        result[category] = result.get(category, 0) + amount

    return dict(sorted(result.items(), key=lambda x: x[1], reverse=True))