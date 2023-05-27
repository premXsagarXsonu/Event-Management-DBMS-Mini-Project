import pandas as pd
import streamlit as st
from database import update_admin_data

def update_admin(ids):
    selected_id = st.selectbox("Choose the Admin Id :",ids)
    st.warning("Do you want to delete ::{}".format(selected_id))
    # col1, col2 = st.columns(2)
    # with col1:
    #     # a_id = st.text_input("Enter your Admin Id :")
        

    # with col2:
    a_name = st.text_input("Enter your Admin Name :")
    if st.button("Update Admin"):
        update_admin_data(selected_id,a_name)
        st.success("Updated Admin record : {}".format(selected_id))