import streamlit as st
from add.add_event import create_event 
from add.add_worker import create_worker
from add.add_customer import create_customer
from add.add_admin import create_admin



def create():
    menu = ["Admin","Worker","Customer","Events"]
    choice = st.selectbox("Choose Any Entity",menu)

    if choice == "Admin":
        st.subheader("Add Admin Details")
        create_admin()
    if choice == "Worker":
        st.subheader("Add Worker Details")
        create_worker()
    if choice == "Customer":
        st.subheader("Add Customer Details")
        create_customer()
    if choice == "Events":
        st.subheader("Add Event Details")
        create_event()
   
    