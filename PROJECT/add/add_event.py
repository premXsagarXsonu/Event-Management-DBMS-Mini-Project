import streamlit as st
from database import add_event_data

def create_event():
    col1, col2 = st.columns(2)
    with col1:
        e_id = st.number_input("Enter Event Id")
        e_date = st.date_input("Enter Event Date :")
        e_place = st.text_input("Enter Event Place :")
        e_type = st.selectbox("Event Type :",["Marriage","Birthday","Enagagement","Naming Ceromony","Fest","Mehendi","Anniversary"])

    with col2:
        e_fee = st.number_input("Enter Event Fee :")
        w_id = st.number_input("Worker Id : ")
        a_id = st.number_input("Admin Id : ")
        c_id = st.number_input("Customer Id :")
        
    
    if st.button("Add Event"):
        add_event_data(e_id,e_date,e_place,e_type,e_fee,w_id,a_id,c_id)
        st.success("Added Event Record : {}".format(e_id))