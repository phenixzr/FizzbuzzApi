from sqlalchemy import (Column, Integer, MetaData, String, Table, create_engine, ARRAY)
from databases import Database

DATABASE_URL = 'postgresql://fzapiuser:jn45vrt5v23@localhost/fizzbuzz'

engine = create_engine(DATABASE_URL)
metadata = MetaData()

fizzbuzzDb = Table(
    'fizzbuzz',
    metadata,
    Column('id', Integer, primary_key=True),
    Column('int1', Integer),
    Column('int2', Integer),
    Column('limit', Integer),
    Column('str1', String(250)),
    Column('str2', String(250))
)

database = Database(DATABASE_URL)