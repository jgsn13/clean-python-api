# pylint: disable=E1101


from src.infra.config import DBConnectionHandler
from src.infra.entities import User


class FakerRepo:
    """Fake repositpry"""

    @classmethod
    def insert_user(cls):
        """Insert a new user"""

        with DBConnectionHandler() as db_conn:
            try:
                new_user = User(name="Joaquim", password="123456")
                db_conn.session.add(new_user)
                db_conn.session.commit()
            except:
                db_conn.session.rollback()
                raise
            finally:
                db_conn.session.close()
