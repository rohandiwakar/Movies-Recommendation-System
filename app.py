import streamlit as st
import pickle
import pandas as pd
import requests
import time

# Function to fetch poster from TMDb with retry and exponential backoff
def fetch(movie_id, retries=3, base_delay=5):
    url = f"https://api.themoviedb.org/3/movie/{movie_id}?api_key=8265bd1679663a7ea12ac168da84d2e8&language=en-US"
    for attempt in range(retries):
        try:
            response = requests.get(url, timeout=10)
            response.raise_for_status()
            data = response.json()
            poster_path = data.get('poster_path')
            if poster_path:
                return "https://image.tmdb.org/t/p/w500/" + poster_path
        except requests.exceptions.RequestException as e:
            wait = base_delay * (2 ** attempt)
            print(f"Attempt {attempt + 1} failed: {e}. Retrying in {wait} seconds...")
            time.sleep(wait)
    return "https://via.placeholder.com/500x750?text=No+Image"

# Recommendation function with error handling
def recommend(movie):
    matches = movies[movies['title'].str.lower().str.strip() == movie.lower().strip()]
    if matches.empty:
        st.error(f"No match found for movie title: '{movie}'")
        return [], []

    movie_index = matches.index[0]
    distances = similarity[movie_index]
    movies_list = sorted(list(enumerate(distances)), reverse=True, key=lambda x: x[1])[1:6]

    recommend_movies = []
    recommend_movie_posters = []
    for i in movies_list:
        movie_id = movies.iloc[i[0]].movie_id
        recommend_movie_posters.append(fetch(movie_id))
        recommend_movies.append(movies.iloc[i[0]].title)

    return recommend_movies, recommend_movie_posters

# Load data
movies_dict = pickle.load(open('movie_dict.pkl', 'rb'))
movies = pd.DataFrame(movies_dict)
similarity = pickle.load(open('similarity.pkl', 'rb'))

# Streamlit UI
st.set_page_config(page_title="Movie Recommender", layout="wide")
st.title("🎥 Movie Recommendation System")

selected_movie_name = st.selectbox(
    "Select a movie to get recommendations:",
    movies['title'].tolist()
)

if st.button("Recommend Movie"):
    recommended_movie_names, recommended_movie_posters = recommend(selected_movie_name)
    if recommended_movie_names:
        cols = st.columns(5)
        for idx, col in enumerate(cols):
            with col:
                st.text(recommended_movie_names[idx])
                st.image(recommended_movie_posters[idx])
    else:
        st.warning("No recommendations available. Please try a different movie.")