import pandas as pd
import streamlit as st
from database import update_customer_data

def update_customer(ids):
    selected_id = st.selectbox("Choose Customer Id :",ids)
    st.warning("Do you want to update ::{}".format(selected_id))
    col1, col2 = st.columns(2)
    with col1:
        # c_id = st.text_input("Customer Id :")
        c_name = st.text_input("Customer Name :")

    with col2:
        c_place = st.text_input("Customer Place :")
        c_phone= st.text_input("Customer Phone:")
        
    if st.button("Update Customer"):
        update_customer_data(selected_id,c_name,c_place,c_phone)
        st.success("Update Customer record : {}".format(selected_id))