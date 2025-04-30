import streamlit as st
import pandas as pd
import pickle
import gzip
import shutil
import os

from  util_1 import set_background_image,image_url,fetch_poster,literal_eval
set_background_image(image_url)



def fetching_poster(select_movie):
    Id=movies_data[movies_data['title'] == select_movie]['movie_id'].values[0]
    path=fetch_poster(Id)
    return path

def recommend(movie):
    movie_index = movies_data[movies_data['title']==movie].index[0]
    distances = similarity[movie_index]
    movies_list = sorted(list(enumerate(distances)),reverse=True,key=lambda x:x[1])

    recommended_movies = []
    recommended_movie_posters = []
    for i in movies_list[1:6]:
        movies_id = movies_data.iloc[i[0]].movie_id
        recommended_movie_posters.append(fetch_poster(movies_id))
        recommended_movies.append(movies_data.iloc[i[0]].title)
    return recommended_movies,recommended_movie_posters





file_path = os.path.join(os.path.dirname(__file__), 'data_', 'movies_data.pkl')

with open(file_path, 'rb') as f:
    movie_list = pickle.load(f)
movies_data = pd.DataFrame(movie_list)
with gzip.open('data_/similarity.pkl.gz', 'rb') as f:
    similarity = pickle.load(f)
st.title("Hollywood Silver Screen")
select_movie=st.selectbox(
    "Search Movie Title",
    movies_data['title'].values,
    index=None,
    placeholder="Search...",
)
if(select_movie!=None):
    col1, col2 = st.columns(2)
    with col1:
        st.image(fetching_poster(select_movie),width=200,caption=select_movie)
    
    with col2:
        st.markdown(f"Title: {select_movie}")
        st.markdown(f"Release Date: {movies_data[movies_data['title'] == select_movie]['release_date'].values[0]}")
        st.markdown(f"Director: {literal_eval(movies_data[movies_data['title'] == select_movie]['crew'].values[0])}")
        st.markdown(f"Cast: {literal_eval(movies_data[movies_data['title'] == select_movie]['cast'].values[0])}")
        st.markdown(f"Genres: {literal_eval(movies_data[movies_data['title'] == select_movie]['genres'].values[0])}")
        st.markdown(movies_data[movies_data['title'] == select_movie]['overview'].values[0])

if st.button("Show Recommend"):
    if select_movie!=None:
        recommended_movie_names,recommended_movie_posters = recommend(select_movie)
        col1, col2, col3, col4, col5 = st.columns(5)
        with col1:
            st.image(recommended_movie_posters[0])
            st.text(recommended_movie_names[0])
        with col2:
            st.image(recommended_movie_posters[1])
            st.text(recommended_movie_names[1])
        with col3:
            st.image(recommended_movie_posters[2])
            st.text(recommended_movie_names[2])
        with col4:
            st.image(recommended_movie_posters[3])
            st.text(recommended_movie_names[3])
        with col5:
            st.image(recommended_movie_posters[4])
            st.text(recommended_movie_names[4])
    else:
        st.markdown("Please select movie")

