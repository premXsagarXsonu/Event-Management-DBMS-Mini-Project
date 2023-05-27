import streamlit as st
from database import add_worker_data

def create_worker():
    col1, col2 = st.columns(2)
    with col1:
        w_id = st.number_input("Enter Worker Id :")
        w_name = st.text_input("Enter Worker Name :")
        w_type = st.text_input("Enter Worker Type :")
        

    with col2:
        w_city = st.text_input("Enter Worker City :")
        w_email = st.text_input("Enter Worker Email :")
        w_phone = st.text_input("Your Worker Phone :")
        # hostel_id = st.slider("Block number :",1,6)

    if st.button("Add Worker"):
        add_worker_data(w_id,w_name,w_type,w_email,w_city,w_phone)
        st.success("Added Worker Record : {}".format(w_id))