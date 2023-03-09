from core.models.user import UserDTO, UserDO
import database.resource.user_repository as user_repository


def find_all() -> list[UserDTO] | None:
    users = user_repository.find_all()
    return [user.to_dto() for user in users] if users is not None else None

def find_by_id(id: int):
    user = user_repository.find_by_id(id)
    return user if user is not None else None

def user_exist(id: int) -> bool:
    return (True if find_by_id(id) is not None else False)

def create_user(user: UserDO) -> bool:
    if user.validate_create():
        return user_repository.save_and_flush(user)
    
    return False

def edit_user(user: UserDO) -> bool:
    if user_exist(user.id):
        if user.senha is None:
            user.senha = user_repository.find_by_id(user.id).senha
        return user_repository.save_and_flush(user)
    return False

def delete_user(id: int) -> bool:
    if user_exist(id):
        return user_repository.delete_by_id(id)
    return False
