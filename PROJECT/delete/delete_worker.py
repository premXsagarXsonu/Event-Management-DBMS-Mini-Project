import pandas as pd
import streamlit as st
from database import delete_worker_data

def delete_worker(ids):
    selected_id = st.selectbox("Choose The Worker Id :",ids)
    st.warning("Do you want to delete ::{}".format(selected_id))
    if st.button("Delete Worker Data"):
        delete_worker_data(selected_id)
        st.success("Worker Data Has Been Deleted Successfully")