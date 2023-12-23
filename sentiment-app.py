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


# create title
st.title('Sentiment Analysis Model')
st.write('Enter your review and let the model predict sentiment.')


review = st.text_input('Enter your review:')

submit = st.button('Predict')

        
        
if submit:
    prediction = model.predict([review])

    if prediction[0] == 'positive':
        st.success('😃 Positive Review')
    else:
        st.warning('😟 Negative Review')
        
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

