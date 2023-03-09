from database.connection import session_factory
from core.models.user import UserDO 
from database.schemas import UserEntity


class UserConverter:
    @staticmethod
    def toDO(user_entity: UserEntity) -> UserDO:
        return UserDO (
            id = user_entity.id,
            username = user_entity.username,
            password = user_entity.password,
            admin = user_entity.admin
        )
    
    @staticmethod
    def toEntity(user_do: UserDO) -> UserEntity:
        return UserEntity (
            id = user_do.id,
            username = user_do.username,
            password = user_do.password,
            admin = user_do.admin
        )
    

def save_and_flush(user: UserDO) -> UserDO:
    with session_factory() as session:
        try:
            session.add(UserConverter.toEntity(user))
            session.commit()
            return True
        except Exception as err:
            session.rollback()
            raise err('Não foi possivel adicionar ou editar o usuario')

def delete_by_id(id: int) -> bool:
    with session_factory() as session:
        user = session.query(UserEntity).filter_by(id = id).first()
        if user is not None:
            try:
                session.delete(user)
                session.commit()
                return True
            except Exception as err:
                raise err('Não foi possivel deletar o usuario')

def find_all() -> list[UserDO] | None:
    all_users = [UserConverter.toDO(user) for user in session_factory().query(UserEntity).all()]
    return all_users if len(all_users) > 0 else None

def find_by_id(user_id: int) -> UserDO | None:
    user = session_factory().query(UserEntity).filter_by(id = user_id).first()
    return UserConverter.toDO(user) if user is not None else None