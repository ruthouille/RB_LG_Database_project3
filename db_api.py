import sqlite3, sqlalchemy
from sqlalchemy import insert, create_engine, text, inspect
from fastapi import Depends, FastAPI, HTTPException, status
import numpy as np
from pydantic import BaseModel
from my_db import my_dataset
import json
#from IPython.display import Markdown, display

engine = create_engine('sqlite:///my_dabase.db', echo=True)
conn = engine.connect()

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

# It allow to add a movie in the database
@api.put('/update/insert')
def insert_movie(movie: Movies):
    """
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
                ins = ins.format(tablename=my_dataset, markers=markers)
                connection.execute(ins, new_movie)
   
            except:
                transaction.rollback()
                raise
        
            else:
                transaction.commit()
                return new_movie

#
    sql = insert(my_dataset).values(show_id=movie.show_id, 
                  type=movie.type,
                  title=movie.title,
                  director=movie.director,
                  cast=movie.cast,
                  country=movie.country,
                  date_added=movie.date_added,
                  release_year=movie.release_year,
                  rating=movie.rating,
                  duration=movie.duration,
                  listed_in=movie.listed_in,
                  description=movie.description)
    compiled = sql.compile()
    print(compiled.params)
"""    


# Delete an element in the database
@api.put('/update/delete')
def delete_movie(id: str):
    try:
        sql = text("DELETE FROM my_dataset WHERE my_dataset.show_id" + " =" + "'" + id + "'")
        engine.execute(sql)
        #result.fetchall()
        sql2 = text("SELECT show_id FROM my_dataset where show_id = " + "'" + id + "'")
        result2 = engine.execute(sql2).fetchall()
        return json.dumps(dict(result2))

    except IndexError:
        return {}

#Display the column show_id and the type
@api.get('/display/type')
def get_type():
    try:
        sql = text("SELECT show_id, type FROM my_dataset")
        result = engine.execute(sql).fetchall()
        return json.dumps(dict(result))

    except IndexError:
        return {}

#Display the column show_id and the title
@api.get('/display/title')
def get_title():
    try:
        sql = text("SELECT show_id, title FROM my_dataset")
        result = engine.execute(sql).fetchall()
        return json.dumps(dict(result))

    except IndexError:
        return {}

#Display the column show_id and the title grouped by country
@api.get('/display/title/country')
def get_title_by_country():
    try:
        sql = text("SELECT show_id, title FROM my_dataset GROUP BY country")
        result = engine.execute(sql).fetchall()
        return json.dumps(dict(result))

    except IndexError:
        return {}