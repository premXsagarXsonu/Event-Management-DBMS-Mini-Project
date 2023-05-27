import pandas as pd
import streamlit as st
from database import delete_admin_data

def delete_admin(ids):
    selected_id = st.selectbox("Choose The Admin Id :",ids)
    st.warning("Do you want to delete ::{}".format(selected_id))
    if st.button("Delete Admin Detail"):
        delete_admin_data(selected_id)
        st.success("Admin has been deleted successfully")
        st.write("In delete")