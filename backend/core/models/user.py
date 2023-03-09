from pydantic import BaseModel


class UserDTO(BaseModel):
    id: int | None = None
    username: str

class UserDO(UserDTO):
    password: str
    admin: bool = False

    def to_dto(self) -> UserDTO:
        return UserDTO(id = self.id, username = self.username)
    
    def validate_edit(self) -> bool:
        if self.id is None:
            return False