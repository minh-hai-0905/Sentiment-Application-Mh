#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sat Dec 23 20:48:45 2023

@author: mhai0905
"""

import streamlit as st
import pickle
import io
import os


# load model
model = pickle.load(open('sentiment_analysis_mh.pkl', 'rb'))


## 
st.set_page_config(
    page_title="Predict the sentiment of movie reviews",
    layout="wide",
    initial_sidebar_state="expanded",

)
col1, col2 = st.columns((6, 1))
col1.title(" PREDICT SENTIMENT OF MOVIE REVIEWS ")
col2.image("assets/customer-reviews-and-feedback.jpeg", width=120)
st.sidebar.image("assets/icon.png")
st.sidebar.title("Sentiment Analysis Model📈")
st.sidebar.caption("""I proceeded to build an sentiment classification model for IMDB reviews using TF-IDF. Utilizing different classification algorithms, the LinearSVC model achieved the highest accuracy of 91.23%.
                   Then, I employed pickle and streamlit to develop a web application that predicts emotions for any review.""")
st.sidebar.markdown("Made by Trinh Minh Hai")
st.sidebar.markdown("Mail: haiminh2892002@gmail.com")

st.sidebar.write("---\n")
st.sidebar.caption("You can check out the source code [here](https://github.com/minh-hai-0905/Sentiment-Application-Mh/tree/main).")
st.sidebar.write("---\n")


####-----APP-----
review = st.text_input('Please enter your review:')

submit = st.button('Predict')
       
if submit:
    prediction = model.predict([review])

    if prediction[0] == 'positive':
        st.success(' 🤩🤩 Positive Review')
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

#link to IMDB Review
st.markdown(" 👉 [🎥Visit IMDB: The world's most popular and authoritative source for movie](https://www.imdb.com/?ref_=nv_home)")
