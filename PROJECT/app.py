import streamlit as st
from routes.home import home
from database import create_tables
from routes.r_entity import read_entity
from routes.create import create
from routes.custom import query



def main():
    st.title("Event Management Company Database")
    st.subheader("Prem Sagar J S - PES1UG20CS825,Bhavana N G- PES1UG20CS808")
    menu = ["Home","Add data","Admins","Events","Workers","Customers","Mysql Query"]
    choice = st.sidebar.selectbox("Menu",menu)
    create_tables()
    
    if choice == "Home":
        home()
    
    if choice == "Add data":
        create()
    
    if choice == "Admins":
        entity = "Admin"
        read_entity(entity)

    if choice == "Customers":
        entity = "Customer"
        read_entity(entity)

    if choice == "Workers":
        entity = "Worker"
        read_entity(entity)

    if choice == "Events":
        entity = "Event"
        read_entity(entity)

    if choice == "Mysql Query":
        query()
    



if __name__ == '__main__':
    main()