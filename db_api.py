import sqlite3, sqlalchemy
from sqlalchemy import Table, Column, Integer, String, ForeignKey, MetaData, create_engine, text, inspect
from fastapi import Depends, FastAPI, HTTPException, status
import numpy as np
from pydantic import BaseModel
from my_db import my_dataset
#from IPython.display import Markdown, display

engine = create_engine('sqlite:///my_dabase.db', echo=True)

with engine.connect() as connection:
    results = connection.execute("SELECT * FROM my_dataset LIMIT 10;")
    print(results.fetchall())


api = FastAPI(
    title='Netflix'
)

class Movies(BaseModel):
    show_id: str
    type: str
    title: str
    director: str
    cast: str
    country: str
    date_added: str
    release_year: int
    rating: str
    duration: str
    listed_in: str
    description: str

# It allow to add a movie in the list
@api.put('/update')
def insert_movie(movie: Movies):
    
    new_movie = [(movie.show_id, 
                  movie.type,
                  movie.title,
                  movie.director,
                  movie.cast,
                  movie.country,
                  movie.date_added,
                  movie.release_year,
                  movie.rating,
                  movie.duration,
                  movie.listed_in,
                  movie.description)]

    with engine.connect() as connection:
        with connection.begin() as transaction:
            try:
                markers = ','.join('?' * len(new_movie[0])) 
                ins = 'INSERT OR REPLACE INTO {tablename} VALUES ({markers})'
                ins = ins.format(tablename=my_dataset.name, markers=markers)
                connection.execute(ins, new_movie)
   
            except:
                transaction.rollback()
                raise
        
            else:
                transaction.commit()
