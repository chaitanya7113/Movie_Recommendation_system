import streamlit as st
import requests
import ast
def set_background_image(image_url):
    st.markdown(
        f"""
        <style>
        .stApp {{
            background-image: url("{image_url}");
            background-size: cover;
            background-repeat: no-repeat;
            background-attachment: fixed;
            
        }}
        </style>
        """,
        unsafe_allow_html=True
    )

# Your background image URL
image_url = "https://images.unsplash.com/photo-1616530940355-351fabd9524b?q=80&w=1935&auto=format&fit=crop&ixlib=rb-4.0.3&ixid=M3wxMjA3fDB8MHxwaG90by1wYWdlfHx8fGVufDB8fHx8fA%3D%3D"


def fetch_poster(movie_id):
    

    url = f"https://api.themoviedb.org/3/movie/{movie_id}?language=en-US"

    headers = {
    "accept": "application/json",
    "Authorization": "Bearer eyJhbGciOiJIUzI1NiJ9.eyJhdWQiOiJlYzJlYjU4ZDIzNjlkMTQzMzhkYmU0NzRlNzhlZDA2ZiIsIm5iZiI6MTc0NDM5ODA4MS4zNzEsInN1YiI6IjY3Zjk2NzAxN2Y3MGFjMWEyMWQ5N2EwYyIsInNjb3BlcyI6WyJhcGlfcmVhZCJdLCJ2ZXJzaW9uIjoxfQ.jdJGhmeXR59qbNDJMlGQDRTi7F_t0mxk6PhiMnYDJkg"
    }

    response = requests.get(url, headers=headers)
    response = response.json()
    poster_path = response['poster_path']
    if poster_path!=None:
        full_path = "https://image.tmdb.org/t/p/w500/" + poster_path
    else:
        full_path="image_/poster_comman.jpg"
    return full_path
    

def literal_eval(value):
    value_list = ast.literal_eval(value)
    clean_value = ", ".join(value_list)
    return clean_value
