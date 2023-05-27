import pandas as pd
import streamlit as st
from database import view_all_customer
from delete.delete_customer import delete_customer
from update.update_customer import update_customer


def view_customer():
    result = view_all_customer()
    # st.write(result)
    df = pd.DataFrame(result, columns=["c_id","c_name","c_place","c_phone"])
    with st.expander("View All Customers : "):
        st.dataframe(df)

    #getting list of Customers by their ids 
    ids = [i[0] for i in result]
    selection = st.selectbox("Do you want to UPDATE or DELETE a record ?",['-','Delete','Update'])
    if selection == "Delete":
        delete_customer(ids)

    if selection == "Update":
        update_customer(ids)