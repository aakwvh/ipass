"""
content based filtering algoritme:
stap 1:

bron: https://www.learndatasci.com/glossary/cosine-similarity/
"""

import tkinter as tk
from tkinter import ttk
import pandas as pd
import numpy as np
import time
from wiskundeFunctie import inwendig_product, calculate_magnitude

def load_movies_csv(file_path, delimiter=","):
    """
    Lees een CSV-bestand met films in en retourneer het resulterende gegevensframe.
    :param file_path: Pad naar het CSV-bestand
    :param delimiter: Delimiter die wordt gebruikt in het CSV-bestand
    :return: Gegevensframe met films
    """
    df_movies = pd.read_csv(file_path, delimiter=delimiter)
    return df_movies

def preprocess_genres(df_movies):
    """
    Voorverwerking van de genres in het gegevensframe om een genre-lijst te maken en een gegevensframe met genres.
    :param df_movies: Gegevensframe met films
    :return: Gegevensframe met genres
    """

    df_movies['genrelist'] = df_movies['genres'].str.split('|')
    unique_genres = set(genre for genres in df_movies['genrelist'] for genre in genres)
    df_genres = pd.DataFrame(0, index=df_movies.index, columns=unique_genres)
    for i, row in df_movies.iterrows():
        for genre in row['genrelist']:
            df_genres.loc[i, genre] = 1
    return df_genres


def cosine_similarity(x, y):
    """ bron: https://www.learndatasci.com/glossary/cosine-similarity/

    formule: similarity(x,y) = cos(𝑋⃗, 𝑌⃗) = 𝑋⃗⃗.𝑌⃗⃗ / |𝑋|.|𝑌|
    𝑋⃗⃗.𝑌⃗⃗ is Bereken het dot-product ofterwel inwendig product tussen x en y.
    Dus stel je voor D1 = [1,1,0,0] en D2 = [0,1,1,0], D1 * D2 = 1*0 + 1*1 + 0*1 + 0*0 = 1
    |𝑋|.|𝑌| hier berekenen we de magnitude van X en Y.

    met de cosine similarty kan je berekenen hoe vector x en y te vergelijkbaar zijn.
    Dus ze kijken hoe vergelijkbaar film a en film b. als je kijk naar bepaalde kenmerken van dat film in dit geval kijken we naar de genres.

    :return: een float tussen de 1 en de 0 dus hoe dichter bij de 1 hoe vergelijkbaar de de twee films en als dichtbij de 0 dan verschillend ze zijn van elkaar.
    """

    # Zorg ervoor dat de lengte van x en y hetzelfde is
    if len(x) != len(y):
        return None

    # Bereken het dot-product ofterwel inwendig product tussen x en y
    # dus stel je voor D1 = [1,1,0,0] en D2 = [0,1,1,0]
    # D1 * D2 = 1*0 + 1*1 + 0*1 + 0*0 = 1
    dot_product = inwendig_product(x, y)

    # Bereken de L2-normen (magnitude) van x en y
    magnitude_x = calculate_magnitude(x)
    magnitude_y = calculate_magnitude(y)

    # Bereken de cosine similarity
    cosine_similarity = dot_product / (magnitude_x * magnitude_y)

    return cosine_similarity



def recommend_similar_movies(df_genres, liked_movie_index, num_recommendations=5):
    """
    Genereer aanbevolen films op basis van de gelijkenis met een gegeven film.
    :param df_genres: Gegevensframe met genres
    :param liked_movie_index: Index van de gewaardeerde film
    :param num_recommendations: Aantal aanbevolen films om te genereren
    :return: Gegevensframe met aanbevolen films
    """
    movies_array = df_genres.values
    liked_movie = df_movies.loc[liked_movie_index, 'movie_title']
    liked_movie_vector = movies_array[liked_movie_index]
    similarities = []
    for i, movie_vector in enumerate(movies_array):
        if i != liked_movie_index:
            similarity = cosine_similarity(liked_movie_vector, movie_vector)
            similarities.append((i, similarity))
    similarities.sort(key=lambda x: x[1], reverse=True)
    top_recommendations = [index for index, _ in similarities[:num_recommendations]]
    recommended_movies = df_movies.loc[top_recommendations, 'movie_title']
    return recommended_movies

