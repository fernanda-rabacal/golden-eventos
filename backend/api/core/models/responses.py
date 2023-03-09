from pydantic import BaseModel


class BasicResponse(BaseModel):
    message: str

class CreateResponse(BasicResponse):
    created_id: int