from fastapi import FastAPI
from database import engine, Base
from routes import transaction, chat



app = FastAPI()
Base.metadata.create_all(bind=engine)

app.include_router(transaction.router, prefix="/transactions")
app.include_router(chat.router, prefix="/chats")









    
