from fastapi import APIRouter
from pydantic import BaseModel

from services.ai_service import extract_user_intent, generate_explanation
from services.transaction_service import fetch_transactions, get_category_breakdown

router = APIRouter()

class MessageBody(BaseModel):
    content: str

@router.post("/{chat_id}/messages")
def chat(chat_id: int, body: MessageBody):
    intent_data = extract_user_intent(body.content)
    filters = intent_data["filters"]
    transactions = fetch_transactions(filters)
    breakdown = get_category_breakdown(transactions)
    analysis = generate_explanation(body.content, breakdown)
    return {
        "intent": intent_data,
        "breakdown": breakdown,
        "analysis": analysis
    }