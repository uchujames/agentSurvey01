import streamlit as st
import sqlite3

# Make connection to database
conn = sqlite3.connect("data.db", check_same_thread=False)
cursor = conn.cursor()

# Function to display form
def formCreation():
    st.write("Please fill out the form below:")
    with st.form(key="survey_data"):
        name = st.text_input("Your name")
        email = st.text_input("Your email")
        message = st.text_area("Do you think AI agents will impact your job? Why or why not? (No wrong answers!)")
        submit_button = st.form_submit_button(label="Submit")

        if submit_button:
            st.success("Form submitted!")
            addInfo(name, email, message)

# Function to add form to database
def addInfo(a,b,c):
    # Create table if it doesn't exist
    cursor.execute(
        """
CREATE TABLE IF NOT EXISTS survey_data (NAME TEXT(50), EMAIL TEXT(50), MESSAGE TEXT(1000))
"""
    )
    # Insert data into table
    cursor.execute("INSERT INTO survey_data VALUES (?, ?, ?)", (a, b, c))
    conn.commit()
    conn.close()
    st.success("Data added to database!")

# Run the first function
formCreation()


########## NEED A RULE TO ENSURE THE FORM IS COMPLETE!!!!



