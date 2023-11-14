import streamlit as st
from send_email import send_email

st.header("Contact Me")

# Creates form for user to enter their email address into
with st.form(key="email_form"):
    user_email = st.text_input("Enter Your Email Address:")

    # st.text_area() creates a larger, extendable text box
    user_message_input = st.text_area("Enter Your Message:")
    user_message = f"""\
Subject: New email from {user_email}

From: {user_email}
{user_message_input}
"""
    button = st.form_submit_button("Submit")

    # When button is clicked, it passes True, otherwise it remains False
    if button:
        send_email(user_message)
        st.info("EMAIL SUCCESSFULLY SENT")