from core.models.user import UserDO 
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
            promotor = user_do.promotor 
        )
    

def save_and_flush(user: UserDO) -> UserDO:
    with session_factory() as session:
        try:
            user_entity = session.get(UserEntity, user.id)

            # Novas Infos
            user_entity.email = user.email
            user_entity.nome = user.nome
            user_entity.senha = user.senha
            user_entity.cpf = user.cpf
            user_entity.promotor = user.promotor
            
            session.commit()
            return True
        except Exception as err:
            session.rollback()
            raise err

def delete_by_id(id: int) -> bool:
    with session_factory() as session:
        try:
            user: UserEntity = session.get(UserEntity, id)
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