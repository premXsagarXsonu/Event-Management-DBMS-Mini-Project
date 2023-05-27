import pandas as pd
import streamlit as st
from read.read_event import view_event
from read.read_customer import view_customer
from read.read_worker import view_worker
from read.read_admin import view_admin


def read_entity(choice):
# def read_entity():
    # menu = ["Student","Employee","Hostel","Visitors","Room","Cloak_Room"]
    # choice = st.selectbox("Choose the entity",menu)

    if choice == "Admin":
        st.subheader("View Admin details")
        view_admin()
    if choice == "Event":
        st.subheader("View Event details")
        view_event()
    if choice == "Worker":
        st.subheader("View Worker details")
        view_worker()
    if choice == "Customer":
        st.subheader("View Customer details")
        view_customer()
