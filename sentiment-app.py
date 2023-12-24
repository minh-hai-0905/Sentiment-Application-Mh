#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sat Dec 23 20:48:45 2023

@author: mhai0905
"""

import streamlit as st
import pickle

# load model
model = pickle.load(open('sentiment_analysis_mh.pkl', 'rb'))


## 
st.set_page_config(
    page_title="Predict the sentiment of movie reviews",
    layout="wide",
    initial_sidebar_state="expanded",

)
col1, col2 = st.columns((6, 1))
col1.title("Predict Sentiment of Movie Review")
col2.image("assets/customer-feedback.png", width=120)

st.sidebar.image("assets/icon.png")
st.sidebar.title("Sentiment Analysis Model")
st.sidebar.markdown("""
    <div style='border:1px solid #ccc; padding: 10px; border-radius: 10px;'>
        <ul style='list-style-type: circle;'>
            <li>I proceeded to build a sentiment classification model for IMDB reviews using TF-IDF.</li>
            <li>Utilizing different classification algorithms, the LinearSVC model achieved the highest accuracy of 91.23%.</li>
            <li>Then, I employed pickle and streamlit to develop a web application that predicts emotions for any review.</li>
        </ul>
    </div>
""", unsafe_allow_html=True)


st.sidebar.write("---\n")
st.sidebar.markdown("Made by: Trinh Minh Hai")
st.sidebar.markdown("Mail: haiminh2892002@gmail.com")

st.sidebar.write("---\n")
st.sidebar.markdown("You can check out the source code [here](https://github.com/minh-hai-0905/Sentiment-Application-Mh/tree/main).")
st.sidebar.write("---\n")
st.sidebar.markdown("🤍🤍 Thank you very much 🤍🤍")

####-----APP-----

st.markdown('Please enter your review 👇👇', height=150)

st.markdown(
    """
    <style>
    div[data-baseweb="textarea"] textarea {
        background-color: ##993b58 !important;
    }
    </style>
    """,
    unsafe_allow_html=True
)

submit = st.button('Predict')      
if submit:
    prediction = model.predict([review])

    if prediction[0] == 'positive':
        st.success(' 🥰🥰 Positive Review')
    else:
        st.warning(' 🥺🥺 Negative Review')
        
st.markdown(
    """
    <style>
    body {
        background-color: #f0f0f0;
    }
    </style>
    """,
    unsafe_allow_html=True
)

st.title("Introduce | IMDb ✨✨✨")
#link to IMDB Review
st.markdown(" 👉 [🎥Visit IMDb: The world's most popular and authoritative source for movie](https://www.imdb.com/?ref_=nv_home)")
st.image("assets/imdb.png")
("""
* IMDb (Internet Movie Database) is an online database of information related to films, television series, podcasts, home videos, video games,
and streaming content online – including cast, production crew and personal biographies, plot summaries, trivia, ratings, and fan and critical reviews. 
IMDb began as a fan-operated movie database on the [Usenet](https://en.wikipedia.org/wiki/Usenet) group "rec.arts.movies" in 1990, and moved to the Web in 1993. 
Since 1998, it has been owned and operated by IMDb.com, Inc., a subsidiary of [Amazon](https://en.wikipedia.org/wiki/Amazon_(company)).

* As of 2019, IMDb was the 52nd most visited website on the Internet, as ranked by [Alexa](https://en.wikipedia.org/wiki/Alexa_Internet). 
As of March 2022, the database contained some 10.1 million titles (including television episodes), 11.5 million person records, and 83 million registered users.
""")
