import pandas as pd
import streamlit as st
from database import view_all_worker
from update.update_worker import update_worker
from delete.delete_worker import delete_worker

def view_worker():
    result = view_all_worker()
    df = pd.DataFrame(result, columns=["w_id","w_name","w_type","w_email","w_city","w_phone"])
    with st.expander("View all Wrokers : "):
        st.dataframe(df)

    #getting list of employees by their ids 
    ids = [i[0] for i in result]
    selection = st.selectbox("Do you want to UPDATE or DELETE a record ?",['-','Delete','Update'])
    if selection == "Delete":
            delete_worker(ids)

    if selection == "Update":
        update_worker(ids)
            