import streamlit as st
import mysql.connector

mydb = mysql.connector.connect(
database="ems",
# database="event_management_system",
user="root",
password="",
host="localhost",
# port=8929,
)
c = mydb.cursor(buffered=True)

# C - creating tables
def create_tables():
    c.execute('CREATE TABLE IF NOT EXISTS WORKER(W_Id INT NOT NULL,W_Name VARCHAR(20),W_Type VARCHAR(20),W_Email VARCHAR(20),W_City VARCHAR(20),W_Phone VARCHAR(10) NOT NULL,PRIMARY KEY (W_Id))')

    c.execute('CREATE TABLE IF NOT EXISTS CUSTOMER(C_ID INT NOT NULL,C_Name VARCHAR(20),C_Place VARCHAR(20),C_Phone VARCHAR(10) NOT NULL,PRIMARY KEY (C_ID))')

    c.execute('CREATE TABLE IF NOT EXISTS ADMIN(A_Id INT NOT NULL,A_Name VARCHAR(20),PRIMARY KEY (A_Id))')

    c.execute('CREATE TABLE IF NOT EXISTS EVENT(E_Id INT NOT NULL,E_Date DATE,E_Place VARCHAR(20),E_Type VARCHAR(20),E_Fee INT NOT NULL,W_Id INT NOT NULL,A_Id INT NOT NULL,C_ID INT NOT NULL,PRIMARY KEY (E_Id),FOREIGN KEY (W_Id) REFERENCES WORKER(W_Id),FOREIGN KEY (A_Id) REFERENCES ADMIN(A_Id),FOREIGN KEY (C_ID) REFERENCES CUSTOMER(C_ID))')

   

# execution of custom query
def custom_query(q):
    c.execute(q)
    data = c.fetchall()
    mydb.commit()
    return data



# adding data into tables

def add_admin_data(a_id,a_name):
    c.execute('INSERT INTO admin(a_id,a_name) VALUES(%s,%s)',(a_id,a_name))
    mydb.commit()

def add_worker_data(w_id,w_name,w_type,w_email,w_city,w_phone):
    c.execute('INSERT INTO worker(w_id,w_name,w_type,w_email,w_city,w_phone) VALUES(%s,%s,%s,%s,%s,%s)',(w_id,w_name,w_type,w_email,w_city,w_phone))
    mydb.commit()

def add_event_data(e_id,e_date,e_place,e_type,e_fee,w_id,a_id,c_id):
    c.execute('INSERT INTO event(e_id,e_date,e_place,e_type,e_fee,w_id,a_id,c_id) VALUES(%s,%s,%s,%s,%s,%s,%s,%s)',(e_id,e_date,e_place,e_type,e_fee,w_id,a_id,c_id))
    mydb.commit()

def add_customer_data(c_id,c_name,c_place,c_phone):
    c.execute('INSERT INTO customer(c_id,c_name,c_place,c_phone) VALUES (%s,%s,%s,%s)',(c_id,c_name,c_place,c_phone) )
    mydb.commit()

# R - reading data from the tables 
def view_all_admin():
    c.execute('select * from admin')
    data = c.fetchall()
    return data

def view_all_worker():
    c.execute('select * from worker')
    data = c.fetchall()
    return data

def view_all_event():
    c.execute('select * from event')
    data = c.fetchall()
    return data

def view_all_customer():
    c.execute('select * from customer')
    data = c.fetchall()
    return data


# U - update data/record entries
def update_admin_data(a_id,a_name):
    c.execute('UPDATE admin set a_name = %s where a_id=%s',(a_name,a_id) )
    mydb.commit()

def update_worker_data(w_id,w_name,w_type,w_email,w_city,w_phone):
    c.execute('UPDATE worker set w_name=%s,w_type=%s,w_email=%s,w_city=%s,w_phone=%s where w_id=%s',(w_name,w_type,w_email,w_city,w_phone,w_id))
    mydb.commit()

def update_event_data(e_id,e_date,e_place,e_type,e_fee,w_id,a_id,c_id):
    c.execute('UPDATE event set e_date =%s,e_place=%s,e_type=%s,e_fee=%s,w_id=%s,a_id=%s,c_id=%s where e_id=%s',(e_date,e_place,e_type,e_fee,w_id,a_id,c_id,e_id) )
    mydb.commit()

def update_customer_data(c_id,c_name,c_place,c_phone):
    c.execute('UPDATE customer set c_name=%s,c_place=%s,c_phone=%s where c_id=%s',(c_name,c_place,c_phone,c_id) )
    mydb.commit()

# D - delete records
def delete_admin_data(a_id):
    c.execute('DELETE FROM admin where a_id="{}"'.format(a_id))
    mydb.commit()

def delete_worker_data(w_id):
    c.execute('DELETE FROM worker where w_id="{}"'.format(w_id))
    mydb.commit()

def delete_event_data(e_id):
    c.execute('DELETE FROM event where e_id="{}"'.format(e_id))
    mydb.commit()

def delete_customer_data(c_id):
    c.execute('DELETE FROM customer where c_id="{}"'.format(c_id))
    mydb.commit()