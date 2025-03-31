import pickle

import pandas as pd
import streamlit as st
import requests
import requests


def fetch_poster(movie_id):
    api_key = "your_api_key_here"  # Replace with your actual API key
    url = f"https://api.themoviedb.org/3/movie/{movie_id}?api_key=8265bd1679663a7ea12ac168da84d2e8&language=en-US"

    response = requests.get(url)  # Ensure response is assigned

    if response.status_code != 200:
        print(f"Error fetching poster for movie_id {movie_id}: {response.status_code}")
        return None  # Return None if API request fails

    data = response.json()
    return "https://image.tmdb.org/t/p/w500/" + data.get("poster_path", "")


def recommend(movie):
    movie_index=movies[movies['title']==movie].index[0]
    distances=similarity[movie_index]
    movies_list=sorted(list(enumerate(distances)),reverse=True,key=lambda x:x[1])[1:6]

    recommended_movies=[]
    recommended_movies_posters=[]
    for i in movies_list:
        movie_id=movies.iloc[i[0]].movie_id

        recommended_movies.append(movies.iloc[i[0]].title)
        #fetch posters from API
        recommended_movies_posters.append(fetch_poster(movie_id))
    return recommended_movies , recommended_movies_posters


movies_dict=pickle.load(open('movie_dict.pkl', 'rb'))
movies=pd.DataFrame(movies_dict)

similarity=pickle.load(open('similarity.pkl', 'rb'))

st.title('Movie Recommendation System')

movie_list = movies['title'].values
selected_movie = st.selectbox(
    "Type or select a movie from the dropdown",
    movie_list
)

if st.button('Show Recommendation'):
    names, posters = recommend(selected_movie)

    cols = st.columns(5)  # Create 5 columns for 5 recommendations

    for i in range(5):
        with cols[i]:
            st.text(names[i])
            st.image(posters[i])

    # for i in recommendations:
    #     st.write(i)
