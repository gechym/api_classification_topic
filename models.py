from pydantic import BaseModel

class ClassificationRequest(BaseModel):
    topic: str
    content: str

class ClassificationResponse(BaseModel):
    topic: str
    content: str
    result: bool
