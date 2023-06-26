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




