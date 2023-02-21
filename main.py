from fastapi import FastAPI
import pandas as pd
from typing import Optional


app = FastAPI()

#http://127.0.0.1:8000


# Define the csv
df = pd.read_csv("df_total_data.csv")

@app.get("/")
def read_root():
    return {"Hello!": "Welcome!"}


# Setpoint 1: Movie with longer duration with optional filters of YEAR, PLATFORM AND TYPE OF DURATION.
#             (the function should be called get_max_duration(year, platform, duration_type))

@app.get("/get_max_duration")
def get_max_duration(year: Optional[int] = None, platform: Optional[str] = None, duration_type: Optional[str] = 'min'):

    if duration_type is not None and duration_type not in ['min', 'season']:
        return {"Error": "Duration must be one of the following: min, season"}

    df_movies = df

    if year:
        df_movies = df_movies[df_movies.release_year == year]

    if platform:

        
        # We pass platform to lowercase in case a user writes it in uppercase
        platform = platform.lower()

        
        # We check that the entered platform is correct
        platforms = ["amazon", "disney", "hulu", "netflix"]

        if platform not in platforms:
            return {"Error": "Wrong platform! You must enter one of the following: amazon, disney, hulu, netflix"}

        df_movies = df_movies[df_movies.platform == platform ]

    # We check that the duration_type is valid
    if duration_type:
        
        # We pass duration_type to lowercase in case a user writes it in uppercase
        duration_type = duration_type.lower()

        df_movies = df_movies[df_movies.duration_type == duration_type]

    if not df_movies.empty:
        max_duration_movie = df_movies.sort_values('duration_int', ascending=False).iloc[0]['title']

    else:
        return {"Error": "No movie was found with the given parameters."}

    return {"max_duration_movie": max_duration_movie}


# Setpoint 2: Number of films by platform with a score greater than XX in a given year
#             (the function should be called get_score_count(platform, scored, year))

@app.get("/get_score_count/{platform}/{scored}/{year}")
def get_score_count(platform: str, scored: float, year: int):
    
    # We check that the entered platform is correct
    platform = platform.lower()

    platforms = {"amazon","disney","hulu","netflix"}

    if platform not in platforms:
        return {"Error": "Wrong platform! You must enter one of the following: amazon, disney, hulu, netflix"}

    # Verify that the scored range is valid. Should not be less than 0 or greater than 5
    if scored < 0 or scored > 5:
        return {"Error": "Score must be between 0 and 5."}

    # Filter by platform and year
    df_filtered = df[(df.platform == platform) & (df.release_year == year)]

    # Filter by score
    df_filtered = df_filtered[df_filtered.score_prom >= scored]

    # Count the movies
    count = df_filtered.shape[0]

    if count == 0:
        return {"Error": "No movies were found with the given parameters."}

    return {"count": count}


# Setpoint 3: Number of movies by platform with Platform filter (The function must be called get_count_platform(platform))

@app.get('/get_count_platform/{platform}')
def get_count_platform(platform: Optional[str] = None):

    # We check that the entered platform is correct
    if platform is not None and platform.lower() not in ['disney', 'amazon', 'hulu', 'netflix']:
        return {"Error": "The platform must be one of the valid options: Disney Plus, Amazon Prime, Hulu or Netflix."}
    
    # Filter the movies for the specified platform
    df_filtered = df[df.platform.str.lower() == platform.lower()] if platform is not None else df[df.type == 'movie']

    # Verify that there is at least one movie that meets the filters
    if df_filtered.empty:
        return {"Error": "There are no movies for that platform."}
    
    # Group by platform and count the number of resulting rows
    dict_count = df_filtered.groupby('platform').size().to_dict()

    count = dict_count[platform.lower()] if platform is not None else len(dict_count)

    return {"count": count}


# Setpoint 4: Actor who is most repeated according to platform and year. (The function should be called get_actor(platform, year)) 

@app.get('/get_actor/{platform},{year}')
def get_actor(platform: str = None, year: int = None):
    
    # We check that the entered platform is correct
    if platform is not None and platform.lower() not in ['disney', 'amazon', 'hulu', 'netflix']:
        return {"Error": "The platform must be one of the valid options: Disney Plus, Amazon Prime, Hulu or Netflix."}
   
    # Verify that the year is within the valid range
    if year is not None and (year <= 1920 or year >= 2021):
        return {"Error": "The year must be within the range of 1920 to 2021."}

        # Filter movies for the specified platform and year
    df_plataformaAño = df[(df.platform == platform) & (df.release_year == year)]
    
    # Separate the names of the actors and create a row for each one
    df_cast = df_plataformaAño.assign(cast=df_plataformaAño.cast.str.split(', ')).explode('cast')
    
    # Count the number of appearances of each actor
    actor_counts = df_cast.cast.value_counts()
    
    # Obtain the most repeated actor and his number of appearances
    max_actor = actor_counts.index[0]

    max_count = int(actor_counts.iloc[0])
    
    # Create a dictionary to be able to see the results
    famousactor = {'actor': max_actor, 'count': max_count}
    
    return famousactor 

    #You cand download here : https://deta.space/discovery/@gvbrilohenry/deta

    # For run the interface aplication locally : http://127.0.0.1:8000/docs#/