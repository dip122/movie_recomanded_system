import streamlit as st
import pickle
import pandas as pd

def recommand(movie):
        movie_index = movies[movies['title'] == movie].index[0]
        distances = similarity[movie_index]
        movies_list = sorted(list(enumerate(distances)), reverse=True, key=lambda x: x[1])[1:6]

        recommanded_movies = []
        for i in movies_list:
            recommanded_movies.append(movies.iloc[i[0]].title)
        return recommanded_movies



movies_dict = pickle.load(open('movie_dict.pkl','rb'))
movies = pd.DataFrame(movies_dict)

similarity= pickle.load(open('similarity.pkl','rb'))

st.title('Movie Recommender System')

selected_movie_name = st.selectbox(
    'How would you like to be contacted?',
    movies['title'].values)

if st.button('Recommand'):

    reco = recommand(selected_movie_name)
    for i in reco:
        st.write(i)

