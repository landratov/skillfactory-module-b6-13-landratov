import sqlalchemy as sa
from sqlalchemy.orm import sessionmaker
from sqlalchemy.ext.declarative import declarative_base


DB_PATH = "sqlite:///albums.sqlite3"
Base = declarative_base()


class Album(Base):
    """
    Описывает структуру таблицы album для хранения записей музыкальной библиотеки
    """

    __tablename__ = "album"

    id = sa.Column(sa.INTEGER, primary_key = True)
    year = sa.Column(sa.INTEGER)
    artist = sa.Column(sa.TEXT)
    genre = sa.Column(sa.TEXT)
    album = sa.Column(sa.TEXT)


def connect_db():
    """
    Устанавливает соединение к базе данных, создает таблицы, если их еще нет и возвращает объект сессии 
    """
    engine = sa.create_engine(DB_PATH)
    Base.metadata.create_all(engine)
    session = sessionmaker(engine)
    return session()


def find(artist):
    """
    Находит все альбомы в базе данных по заданному артисту
    """
    session = connect_db()
    albums = session.query(Album).filter(sa.func.lower(Album.artist) == artist.lower()).all()
    return albums

def checkAlbum(artist, album, genre, year):
    """
    Проверяет, есть ль альбом в базе
    """
    session = connect_db()
    albums = session.query(Album).filter(sa.func.lower(Album.artist) == artist.lower()).filter(sa.func.lower(Album.album) == album.lower()).filter(sa.func.lower(Album.genre) == genre.lower()).filter(Album.year == year).all()
    return albums

def add(artist, album, genre, year):
    """
    Добавляет новый альбом в базу
    """
    session = connect_db()
    album = Album(
        artist = artist,
        album = album,
        genre = genre,
        year = year)
    session.add(album)
    session.commit()