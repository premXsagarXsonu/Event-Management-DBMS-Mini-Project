import pandas as pd
import streamlit as st
from database import delete_event_data

def delete_event(selected_id):
    if st.button("Delete Event Detail"):
        delete_event_data(selected_id)
        st.success("Event Record Has Been Deleted Successfully")