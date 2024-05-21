'''Modulos do sqlalchemy'''


from sqlalchemy import create_engine, Column, String, Integer
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker


# Configurações
engine = create_engine('mysql+pymysql://ronaldpedra:PASSWORD@192.168.1.13:3306/cinema')
Base = declarative_base()
Session = sessionmaker(bind=engine)
session = Session()


# Entidades
class Filmes(Base):
    ''' Classe que representa a tabela filmes'''


    __tablename__ = 'filmes'

    titulo = Column(String, primary_key=True)
    genero = Column(String, nullable=False)
    ano = Column(Integer, nullable=False)

    def __repr__(self):
        return f'Filme [titulo={self.titulo}, ano={self.ano}]'

# SQL
# INSERT
data_insert = Filmes(titulo='jfasasufy', genero='Acao', ano=1111)
session.add(data_insert)
session.commit()


# DELETE
session.query(Filmes).filter(Filmes.titulo=='Dracula').delete()
session.commit()


# UPDATE
session.query(Filmes).filter(Filmes.genero=='Drama').update({'ano': 2000})
session.commit()


# SELECT
data = session.query(Filmes).all()
print(data)
print(data[0].titulo)

session.close()
