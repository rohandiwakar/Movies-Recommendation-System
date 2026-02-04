# 🎥 Movie Recommendation System

This **Movie Recommendation System** is a content-based recommender application built using **Python** and **Streamlit**.  
It suggests movies similar to a selected movie by analyzing similarity scores and enhances the user experience by displaying movie posters fetched from the **TMDb API**.

---

## 📌 Project Overview

With the increasing number of movies available online, users often find it difficult to decide what to watch next.  
This project helps users discover movies similar to their favorites using **machine learning–based similarity analysis**.

The system:
- Takes a movie name as input
- Finds similar movies based on precomputed similarity scores
- Displays recommended movie titles along with their posters

---

## 🎯 Objectives

- Build a content-based movie recommender system  
- Apply similarity-based recommendation techniques  
- Create an interactive web interface using Streamlit  
- Integrate real movie posters using TMDb API  

---

## 🚀 Features

- Content-based movie recommendation  
- Interactive Streamlit web interface  
- Displays movie posters  
- Error handling for invalid movie names  
- Fast and user-friendly UI  

---

## 🧠 Recommendation Technique

- **Approach:** Content-Based Filtering  
- **Similarity Metric:** Cosine Similarity (precomputed)  
- **Model Data:** Pickle files (`movie_dict.pkl`, `similarity.pkl`)  

The recommendation is based on the similarity between movies rather than user behavior.

---

## 🛠️ Technologies Used

- **Programming Language:** Python  
- **Libraries:**
  - NumPy
  - Pandas
  - Scikit-learn
  - Requests
  - Streamlit
- **API Used:** TMDb (The Movie Database)
- **IDE:** PyCharm / Jupyter Notebook  

---

## 📂 Project Structure
├── app.py # Streamlit application
├── code.ipynb # Model & preprocessing notebook
├── movie_dict.pkl # Movie data
├── similarity.pkl # Similarity matrix
