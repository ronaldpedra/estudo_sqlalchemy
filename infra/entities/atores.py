''' Pacotes necessário para o arquivo '''

from sqlalchemy import Column, String, Integer, ForeignKey
from infra.configs.base import Base


class Atores(Base):
    ''' Classe que representa a tabela filmes'''


    __tablename__ = 'atores'

    id = Column(Integer, primary_key=True)
    nome = Column(String, nullable=False)
    titulo_filme = Column(String, ForeignKey('filmes.titulo'))

    def __repr__(self):
        return f'Atores [nome={self.nome}, filme={self.titulo_filme}]'
