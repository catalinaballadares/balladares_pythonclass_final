import torch
import streamlit as st
from transformers import pipeline

sentiment_model = pipeline("sentiment-analysis", model="distilbert-base-uncased-finetuned-sst-2-english")

st.title("Sentiment Analysis App")

st.write("Enter a sentence to analyze its sentiment:")

user_input = st.text_area("Your sentence here", height=100)

if st.button("Analyze Sentiment"):
    if user_input.strip() == "":
        st.write("Please enter a sentence to analyze.")
    else:
        result = sentiment_model(user_input)[0]
        label = result['label']
        score = result['score']
        st.write(f"Sentiment: **{label}** (Confidence: {score:.2f})")