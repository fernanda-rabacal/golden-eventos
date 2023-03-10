from pydantic import BaseModel


class BasicResponse(BaseModel):
    status: str
    message: str

class ErrorResponse(BasicResponse):
    error: str

class CreateResponse(BasicResponse):
    created_id: int