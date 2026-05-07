from pydantic import BaseModel

class MessageBody(BaseModel):
    content: str