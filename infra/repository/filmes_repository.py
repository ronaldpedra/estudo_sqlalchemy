''' Imports necessários para o arquivo '''

from sqlalchemy.orm.exc import NoResultFound
from infra.configs.connection import DBConnectionHandler
from infra.entities.filmes import Filmes


class FilmesRepository:

    ''' Classe CRUD para Filmes '''

    def select(self):

        ''' Seleciona todos os registros da tabela filmes '''

        with DBConnectionHandler() as db:
            data = db.session.query(Filmes).all()
            return data
    
    def select_drama_filmes(self):

        ''' Seleciona todos os registros da tabela filmes do genero Drama '''

        with DBConnectionHandler() as db:
            try:
                data = db.session.query(Filmes).filter(Filmes.genero == 'asad').one()
                return data
            except NoResultFound:
                return None
            except Exception as exception:
                db.session.rollback()
                raise exception

    def insert(self, titulo, genero, ano):

        ''' Insere um registro na tabela filmes '''

        with DBConnectionHandler() as db:
            try:
                data_insert = Filmes(titulo=titulo, genero=genero, ano=ano)
                db.session.add(data_insert)
                db.session.commit()
            except Exception as exception:
                db.session.rollback()
                raise exception

    def delete(self, titulo):

        ''' Deleta um registro na tabela filmes '''

        with DBConnectionHandler() as db:
            db.session.query(Filmes).filter(Filmes.titulo == titulo).delete()
            db.session.commit()

    def update(self, titulo, ano):

        ''' Atualiza o ano de um registro na tabela filmes '''

        with DBConnectionHandler() as db:
            db.session.query(Filmes).filter(Filmes.titulo == titulo).update({'ano': ano})
            db.session.commit()
