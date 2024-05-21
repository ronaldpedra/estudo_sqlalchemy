''' Classe de Conecção ao Banco de Dados '''

from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker


class DBConnectionHandler:

    ''' Implementação da conecção ao banco de dados '''

    def __init__(self) -> None:
        self.__connection_string = 'mysql+pymysql://ronaldpedra:PASSWORD@192.168.1.13:3306/cinema'
        self.__engine = self.__create_database_engine()
        self.session = None

    def __create_database_engine(self):
        engine = create_engine(self.__connection_string)
        return engine

    def get_engine(self):
        ''' Retorna o objeto engine '''
        return self.__engine

    def __enter__(self):
        session_make = sessionmaker(bind=self.__engine)
        self.session = session_make()
        return self

    def __exit__(self, exc_type, exc_val, exc_tb):
        self.session.close()
