from typing import Optional
from fastapi import FastAPI
from fastapi.encoders import jsonable_encoder
from pydantic import BaseModel

app = FastAPI()

movies = []

class Movies(BaseModel):
    id : int 
    name : str
    release_year : int
    genres : str

@app.get("/")
def read_root():
    return {"title":"Welcome to Movie mania"}

@app.get("/movies")
def get_movies():
    return movies

@app.get("/movie/id/{movie_id}")
def get_a_movie(movie_id : int):
    movie = movie_id - 1
    return movies[movie]

@app.post("/movies")
def add_movie(movie : Movies):
    # import pdb;pdb.set_trace()
    movies.append(movie.dict())
    return movies[-1]


@app.get("/movie_by_genre/{genres}")
def get_movie_by_geners(genres:str):
    import pdb;pdb.set_trace()
    movieList = []
    for movie in movies:
        # temp = jsonable_encoder.loads(movie)
        if movie['genres'] == genres:
            movieList.append(movie)
    return movieList


@app.delete("/movies/{movie_id}")
def delete_movie(movie_id:int):
    movies.pop(movie_id-1)
    return {"task" : "deletion successfull"}