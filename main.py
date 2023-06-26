import tkinter as tk
from tkinter import messagebox
import pandas as pd
import numpy as np

def get_movie_recommendations():
    # Lees het csv-bestand met films in
    df_movies = pd.read_csv("movie.csv", delimiter=",")

    # Split de genres in een lijst
    df_movies['genrelist'] = df_movies['genres'].str.split('|')

    # Maak een set van unieke genres in de dataset
    unique_genres = set(genre for genres in df_movies['genrelist'] for genre in genres)

    # Maak een DataFrame met een kolom voor elk genre
    df_genres = pd.DataFrame(0, index=df_movies.index, columns=unique_genres)

    # Vul de DataFrame in met 1 voor films die bij een genre horen
    for i, row in df_movies.iterrows():
        for genre in row['genrelist']:
            df_genres.loc[i, genre] = 1

    # Converteer de DataFrame naar een numpy-array
    df = df_genres.values

    def cosine_similarity(x, y):
        # Zorg ervoor dat de lengte van x en y hetzelfde is
        if len(x) != len(y):
            return None

        # Bereken het dot-product tussen x en y
        dot_product = np.dot(x, y)

        # Bereken de L2-normen (magnitude) van x en y
        magnitude_x = np.sqrt(np.sum(x ** 2))
        magnitude_y = np.sqrt(np.sum(y ** 2))

        # Bereken de cosine similarity
        cosine_similarity = dot_product / (magnitude_x * magnitude_y)

        return cosine_similarity

    # Zoek de film in de DataFrame
    liked_movie = movie_entry.get().strip().lower()  # Normaliseer de ingevoerde filmnaam
    movie_index = df_movies[df_movies['movie_title'].str.strip().str.lower() == liked_movie].index
    if len(movie_index) == 0:
        messagebox.showerror("Film niet gevonden", "De ingevoerde film is niet gevonden.")
        return

    x = df_genres.values[movie_index[0]]

    # Bereken de cosine similarity tussen de film en alle andere films
    similarities = []
    for y in df_genres.values:
        similarity = cosine_similarity(x, y)
        similarities.append(similarity)

    # Maak een lijst van (index, similarity) tuples
    indexed_list = list(enumerate(similarities))

    # Sorteer op basis van de similarity in aflopende volgorde
    sorted_list = sorted(indexed_list, key=lambda x: x[1], reverse=True)

    # Haal de indexnummers op van de hoogst gewaardeerde films
    highest_indexes = [item[0] for item in sorted_list[1:11]]

    # Haal de titels op van de aanbevolen films
    recommended_movies = df_movies.loc[highest_indexes, 'movie_title']

    # Filter de ingevoerde film uit de aanbevelingen
    recommended_movies = recommended_movies[recommended_movies != liked_movie]

    # Toon de aanbevolen films in een messagebox
    if recommended_movies.empty:
        messagebox.showinfo("Geen aanbevelingen", "Er zijn geen aanbevelingen beschikbaar.")
    else:
        messagebox.showinfo("Aanbevolen films", "\n".join(recommended_movies))

# Maak het hoofdvenster
window = tk.Tk()
window.title("Film Aanbevelingssysteem")

# Maak een invoerveld voor de gewenste film
tk.Label(window, text="Welke film vind je leuk?").pack()
movie_entry = tk.Entry(window)
movie_entry.pack()

# Maak een knop om de aanbevelingen op te halen
tk.Button(window, text="Aanbevelingen", command=get_movie_recommendations).pack()

# Start de GUI
window.mainloop()

# import tkinter as tk
# from tkinter import messagebox
# import pandas as pd
# import numpy as np
#
# def get_movie_recommendations():
#     # Lees het csv-bestand met films in
#     df_movies = pd.read_csv("movie.csv", delimiter=",")
#
#     # Split de genres in een lijst
#     df_movies['genrelist'] = df_movies['genres'].str.split('|')
#
#     # Maak een set van unieke genres in de dataset
#     unique_genres = set(genre for genres in df_movies['genrelist'] for genre in genres)
#
#     # Maak een DataFrame met een kolom voor elk genre
#     df_genres = pd.DataFrame(0, index=df_movies.index, columns=unique_genres)
#
#     # Vul de DataFrame in met 1 voor films die bij een genre horen
#     for i, row in df_movies.iterrows():
#         for genre in row['genrelist']:
#             df_genres.loc[i, genre] = 1
#
#     # Converteer de DataFrame naar een numpy-array
#     df = df_genres.values
#
#     def cosine_similarity(x, y):
#         # Zorg ervoor dat de lengte van x en y hetzelfde is
#         if len(x) != len(y):
#             return None
#
#         # Bereken het dot-product tussen x en y
#         dot_product = np.dot(x, y)
#
#         # Bereken de L2-normen (magnitude) van x en y
#         magnitude_x = np.sqrt(np.sum(x ** 2))
#         magnitude_y = np.sqrt(np.sum(y ** 2))
#
#         # Bereken de cosine similarity
#         cosine_similarity = dot_product / (magnitude_x * magnitude_y)
#
#         return cosine_similarity
#
#     # Zoek de film in de DataFrame
#     liked_movie = movie_entry.get().strip().lower()  # Normaliseer de ingevoerde filmnaam
#     movie_index = df_movies[df_movies['movie_title'].str.strip().str.lower() == liked_movie].index
#     if len(movie_index) == 0:
#         messagebox.showerror("Film niet gevonden", "De ingevoerde film is niet gevonden.")
#         return
#
#     x = df_genres.values[movie_index[0]]
#
#     # Bereken de cosine similarity tussen de film en alle andere films
#     similarities = []
#     for y in df_genres.values:
#         similarity = cosine_similarity(x, y)
#         similarities.append(similarity)
#
#     # Maak een lijst van (index, similarity) tuples
#     indexed_list = list(enumerate(similarities))
#
#     # Sorteer op basis van de similarity in aflopende volgorde
#     sorted_list = sorted(indexed_list, key=lambda x: x[1], reverse=True)
#
#     # Haal de indexnummers op van de hoogst gewaardeerde films
#     highest_indexes = [item[0] for item in sorted_list[:5]]
#
#     # Haal de titels op van de aanbevolen films
#     recommended_movies = df_movies.loc[highest_indexes, 'movie_title']
#
#     # Toon de aanbevolen films in een messagebox
#     messagebox.showinfo("Aanbevolen films", "\n".join(recommended_movies))
#
# # Maak het hoofdvenster
# window = tk.Tk()
# window.title("Film Aanbevelingssysteem")
#
# # Maak een invoerveld voor de gewenste film
# tk.Label(window, text="Welke film vind je leuk?").pack()
# movie_entry = tk.Entry(window)
# movie_entry.pack()
#
# # Maak een knop om de aanbevelingen op te hal
#
# # Maak een knop om de aanbevelingen op te halen
# tk.Button(window, text="Aanbevelingen", command=get_movie_recommendations).pack()
#
# # Start de GUI
# window.mainloop()


# import pandas as pd
# from sklearn.metrics.pairwise import cosine_similarity
# import time
# import tkinter as tk
# from tkinter import messagebox
#
# def recommend_movies_based_on(title, df_movies):
#     # Split genres into a list
#     df_movies['genrelist'] = df_movies['genres'].str.split('|')
#
#     # Get a list of unique genres in the dataset
#     unique_genres = set(genre for genres in df_movies['genrelist'] for genre in genres)
#
#     # Create a DataFrame with a column for each genre
#     df_genres = pd.DataFrame(0, index=df_movies.index, columns=unique_genres)
#
#     # Mark each genre in each movie with 1
#     for i, row in df_movies.iterrows():
#         for genre in row['genrelist']:
#             df_genres.loc[i, genre] = 1
#
#     # Calculate the cosine similarity between all movies
#     cosine_sim = cosine_similarity(df_genres.values)
#
#     # Make a DataFrame from the similarities
#     df_similarities = pd.DataFrame(cosine_sim, index=df_movies['movie_title'], columns=df_movies['movie_title'])
#
#     similar_movies = df_similarities[title].sort_values(ascending=False)
#     return similar_movies[:100]
#
# def get_recommendations():
#     movie_title = entry.get()
#     if movie_title:
#         try:
#             recommendations = recommend_movies_based_on(movie_title, df_movies)
#             messagebox.showinfo("Recommendations", recommendations.to_string())
#         except KeyError:
#             messagebox.showerror("Error", "Movie title not found.")
#     else:
#         messagebox.showwarning("Warning", "Please enter a movie title.")
#
#
# # df = pd.read_csv('movie.csv')
# # # Lijst maken van de kolom 'movie_title'
# # movie_title_list = df['movie_title'].tolist()
# #
# # print(movie_title_list)
#
#
# # Load the dataset
# df_movies = pd.read_csv('movie.csv')  # Replace 'movies.csv' with your actual dataset
#
# # Create the main window
# window = tk.Tk()
# window.title("Movie Recommender")
#
# # Create a label and an entry for the movie title
# label = tk.Label(window, text="Enter the movie title:")
# label.pack()
# entry = tk.Entry(window)
# entry.pack()
#
# # Create a button to get recommendations
# button = tk.Button(window, text="Get Recommendations", command=get_recommendations)
# button.pack()
#
# # Run the main window loop
# window.mainloop()
