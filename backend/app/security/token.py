from pydantic import BaseModel 
from datetime import datetime as dt


class Token(BaseModel):
    token: str
    initiated_at: dt
    expiration: dt

class AuthorizationToken(BaseModel):
    owner_id: int
    initiated_at: dt
    expiration: dt