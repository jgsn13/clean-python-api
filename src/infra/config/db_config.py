from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker


class DBConnectionHandler:
    """Database connection"""

    def __init__(self):
        self.__connection_string = "sqlite:///storage.db"
        self.__engine = create_engine(self.__connection_string)
        self.session = None

    def get_engine(self):
        """Return engine connection
        :param - None
        :return - engine connection to Database
        """
        return self.__engine

    def __enter__(self):
        session_maker = sessionmaker()
        self.session = session_maker(bind=self.__engine)
        return self

    def __exit__(self, exc_type, exc_val, exc_tb):
        self.session.close()  # pylint: disable=no-member
