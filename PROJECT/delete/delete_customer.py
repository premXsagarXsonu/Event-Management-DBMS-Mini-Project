import pandas as pd
import streamlit as st
from database import delete_customer_data

def delete_customer(customer_id):
    selected_id = st.selectbox("Choose The Cusomer Id :",customer_id)
    st.warning("Do you want to delete ::{}".format(selected_id))

    if st.button("Delete Customer Record"):
        delete_customer_data(selected_id)
        st.success("Customer Record has been Deleted Successfully")