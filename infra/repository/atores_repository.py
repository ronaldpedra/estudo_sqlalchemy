''' Imports necessários para o arquivo '''

from infra.configs.connection import DBConnectionHandler
from infra.entities.atores import Atores
from infra.entities.filmes import Filmes


class AtoresRepository:

    ''' Classe CRUD para Atores '''

    def select(self):

        ''' Seleciona todos os registros da tabela filmes '''

        with DBConnectionHandler() as db:
            data = db.session\
                .query(Atores)\
                .join(Filmes, Atores.titulo_filme == Filmes.titulo)\
                .with_entities(
                    Atores.nome,
                    Filmes.genero,
                    Filmes.titulo
                )\
                .all()
            return data
