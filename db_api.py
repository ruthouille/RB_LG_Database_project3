import sqlite3, sqlalchemy
from sqlalchemy import insert, create_engine, text, inspect
from fastapi import Depends, FastAPI, HTTPException, status
import numpy as np
from pydantic import BaseModel
from my_db import my_dataset, c
import json
#from IPython.display import Markdown, display

engine = create_engine('sqlite:///my_dabase.db', echo=True)
conn = engine.connect()

api = FastAPI(title='Netflix', openapi_tags=[
    {
        'name': 'Insert',
        'description': 'Insert a new element into the database'
    },
    {
        'name': 'Delete',
        'description': 'Delete an element into the database'
    },
    {
        'name': 'Type',
        'description': 'Display the movie type'
    },
    {
        'name': 'Title',
        'description': 'Display the movie location'
    },
    {
        'name': 'Country',
        'description': 'Titles grouped by movie location'
    }
])


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
@api.put('/update/insert', tags=["Insert"])
def insert_movie(movie: Movies):
    """This function adds a new element into the database
    """
    try:
        mydb = sqlite3.connect('my_dabase.db')
        mycursor = mydb.cursor()
        sql = "INSERT INTO my_dataset (show_id, type, title, director, cast, country, date_added, release_year, rating, duration,\
        listed_in, description) VALUES (?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?)"
        val = (movie.show_id, movie.type, movie.title, movie.director, movie.cast, movie.country, movie.date_added, movie.release_year,\
        movie.rating, movie.duration, movie.listed_in, movie.description)
    
        mycursor.execute(sql, val)
        mydb.commit()

        sql = text("SELECT show_id, title FROM my_dataset WHERE show_id = " + "'" + movie.show_id + "'")
        result = engine.execute(sql).fetchall()
        return json.dumps(dict(result))

    except IndexError:
        return {}

# Delete an element in the database
@api.put('/update/delete', tags=["Delete"])
def delete_movie(id: str):
    """This function removes an element into the database
    """
    try:
        sql = text("DELETE FROM my_dataset WHERE my_dataset.show_id" + " =" + "'" + id + "'")
        engine.execute(sql)
        #result.fetchall()
        sql2 = text("SELECT show_id FROM my_dataset WHERE show_id = " + "'" + id + "'")
        result2 = engine.execute(sql2).fetchall()
        return json.dumps(dict(result2))

    except IndexError:
        return {}

#Display the column show_id and the type
@api.get('/display/type', tags=["Type"])
def get_type():
    """This function shows the movie type
    """
    try:
        sql = text("SELECT show_id, type FROM my_dataset")
        result = engine.execute(sql).fetchall()
        return json.dumps(dict(result))

    except IndexError:
        return {}

#Display the column show_id and the title
@api.get('/display/title', tags=["Title"])
def get_title():
    """This function shows the movie title
    """
    try:
        sql = text("SELECT show_id, title FROM my_dataset")
        result = engine.execute(sql).fetchall()
        return json.dumps(dict(result))

    except IndexError:
        return {}

#Display the column show_id and the title grouped by country
@api.get('/display/title/country', tags=["Country"])
def get_title_by_country():
    """This function shows the titles grouped by the movie location
    """
    try:
        sql = text("SELECT show_id, title FROM my_dataset GROUP BY country")
        result = engine.execute(sql).fetchall()
        return json.dumps(dict(result))

    except IndexError:
        return {}