import streamlit as st
from datetime import datetime, date

class UserInputs:

    def __init__(self):
        col1, col2 = st.columns(2)
        with col1:
            self.fname = st.text_input("First Name")
            self.lname = st.text_input("Last Name")
            self.dob = st.date_input("Date of birth")
        with col2:
            self.gender = st.radio('Sex', ["Male", "Female"])
            self.labels = st.checkbox("Horizontal and Vertical Planes", value=True)
        
    def is_valid(self):
        # Ensure all fields are filled and date input is not in the future
        return all([
            self.fname, 
            self.lname, 
            self.gender,
            self.dob <= date.today()
        ])
