import pandas as pd
import streamlit as st
from database import view_all_event
from update.update_event import update_event
from delete.delete_event import delete_event

def view_event():
    result = view_all_event()
    df = pd.DataFrame(result, columns=["e_id","e_date","e_place","e_type","e_fee","w_id","a_id","c_id"])
    with st.expander("View All Event : "):
        st.dataframe(df)
    
    #getting list of event by their ids 

    # DELETION
    ids = [i[0] for i in result]
    selection = st.selectbox("Do you want to UPDATE or DELETE a record ?",['-','Delete','Update'])
    
    if selection == "Delete":
        selected_id = st.selectbox("Choose the Event Id :",ids)
        st.warning("Do you want to delete ::{}".format(selected_id))
        delete_event(selected_id)
    # UPDATION 
    if selection == "Update":
        selected_id = st.selectbox("Choose the Event Id :",ids)
        st.warning("Do you want to update ::{}".format(selected_id))
        update_event(selected_id)
