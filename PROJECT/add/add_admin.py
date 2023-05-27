import streamlit as st
from database import add_admin_data

def create_admin():
    col1, col2 = st.columns(2)
    # col1 = st.columns(1)
    with col1:
        a_id = st.number_input("Enter Admin Id :")
        

    with col2:
        a_name = st.text_input("Enter Admin Name :")
    #     out_time = st.text_input("Enter out_time in 2400 hrs format :")
    #     mobile = st.number_input("Your mobile number :")
    #     srn = st.text_input("Enter the students srn :")
        
    if st.button("Add Admin"):
        add_admin_data(a_id,a_name)
        st.success("Added Admin Record : {}".format(a_id))