import pandas as pd
import streamlit as st
from database import view_all_admin
from delete.delete_admin import delete_admin
from update.update_admin import update_admin

def view_admin():
    result = view_all_admin()
    df = pd.DataFrame(result, columns=["a_id","a_name"])
    with st.expander("View All Admin : "):
        st.dataframe(df)

    #getting list of admin by the admin_id
    admin = [i[0] for i in result]
    selection = st.selectbox("Do you want to UPDATE or DELETE a record ?",['-','Delete','Update'])
    if selection == "Delete":
        delete_admin(admin)

    if selection == "Update":
        update_admin(admin)
        