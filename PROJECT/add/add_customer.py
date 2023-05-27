import streamlit as st
from database import add_customer_data

def create_customer():
    col1, col2 = st.columns(2)
    with col1:
        c_id = st.number_input("Enter Customer Id:")
        c_name = st.text_input("Enter Customer Name:")
        

    with col2:
        
        c_place = st.text_input("Enter Customer Place:")
        c_phone = st.text_input("Enter Customer Phone:")
    
    if st.button("Add Customer"):
        add_customer_data(c_id,c_name,c_place,c_phone)
        st.success("Added details for room number : {}".format(c_id))