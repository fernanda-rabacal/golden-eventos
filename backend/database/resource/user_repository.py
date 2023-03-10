from core.models.user import UserDO
from app.errors.exceptions import DatabaseException
from database.schemas.user_entity import UserEntity
from database import session_factory


class UserConverter:
    @staticmethod
    def toDO(user_entity: UserEntity) -> UserDO:
        return UserDO (
            id = user_entity.id, 
            email = user_entity.email,
            nome = user_entity.nome,
            senha = user_entity.senha,
            cpf = user_entity.cpf,
            promotor = user_entity.promotor 
        )
    
    @staticmethod
    def toEntity(user_do: UserDO) -> UserEntity:
        return UserEntity (
            id = user_do.id, 
            email = user_do.email,
            nome = user_do.nome,
            senha = user_do.senha,
            cpf = user_do.cpf,
            promotor = user_do.promotor if user_do.promotor is not None else False
        )
    

def save_and_flush(userDO: UserDO) -> int:
    with session_factory() as session:
        try:
            if userDO.id is not None:
                user = session.get(UserEntity, userDO.id)
                user.fill_fields_to_edit(userDO)
            else:
                user = UserConverter.toEntity(userDO)
                session.add(user)
            session.commit()
            return user.id
        except Exception as err:
            session.rollback()
            raise DatabaseException (
                status = 'INTERNAL_SERVER_ERROR',
                message = 'Não foi possivel realizar processar sua requisição no banco',
                error = str(err)
            )

def delete_by_id(id: int) -> None:
    with session_factory() as session:
        try:
            user: UserEntity = session.get(UserEntity, id)
            session.delete(user)
            session.commit()
        except Exception as err:
            session.rollback()
            raise DatabaseException (
                status = 'INTERNAL_SERVER_ERROR',
                message = 'Não foi possivel realizar processar sua requisição no banco',
                error = str(err)
            )

def find_all() -> list[UserDO] | None:
    all_users = [UserConverter.toDO(user) for user in session_factory().query(UserEntity).all()]
    return all_users if len(all_users) > 0 else None

def find_by_id(user_id: int) -> UserDO | None:
    user = session_factory().get(UserEntity, user_id)
    return UserConverter.toDO(user) if user is not None else None

def find_by_email(email: str) -> UserDO | None:
    user = session_factory().query(UserEntity).filter_by(email = email).first()
    return UserConverter.toDO(user) if user is not None else None