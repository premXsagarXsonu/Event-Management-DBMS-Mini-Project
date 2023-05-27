# add the layout of the homepage with a photo
from PIL import Image
import streamlit as st

def home():
    img = Image.open("cover.jpg")
    st.image(img,width=600)