import pandas as pd
import streamlit as st
from database import update_worker_data

def update_worker(ids):
    selected_id = st.selectbox("Choose the Worker Id :",ids)
    st.warning("Do you want to delete ::{}".format(selected_id))
    col1, col2 = st.columns(2)
    with col1:
        w_name = st.text_input("Worker Name :")
        w_type = st.text_input("Worker Type:")
        w_email = st.text_input("Worker Email :")

    with col2:
        w_city = st.text_input("Worker City :")
        w_phone = st.text_input("Worker Phone :")
        

    if st.button("Update Worker"):
        update_worker_data(selected_id,w_name,w_type,w_email,w_city,w_phone)
        st.success("Updated Worker: {}".format(selected_id))