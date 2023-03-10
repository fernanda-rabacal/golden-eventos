from api.core.models.user import UserDTO, UserDO
from api.core.models.exceptions import NotFoundException, NoContentException
import api.database.resource.user_repository as user_repository


def find_all() -> list[UserDTO]:
    users = user_repository.find_all()
    if users is None:
        raise NoContentException()
    return [user.to_dto() for user in users]

def find_by_id(id: int) -> UserDO:
    user = user_repository.find_by_id(id)
    if user is None:
        raise NotFoundException (
            'RECURSO_NAO_ENCONTRADO',
            'Não existe usuario com esse id.'
        ) 
    return user

def create_user(user: UserDO) -> int:
    user.create_validations()
    return user_repository.save_and_flush(user)

def edit_user(user: UserDO) -> int:
    user.edit_validations()
    find_by_id(user.id)
    return user_repository.save_and_flush(user)

def delete_user(id: int) -> bool:
    find_by_id(id)
    return user_repository.delete_by_id(id)
