import streamlit as st
from send_email import send_email


st.header("Contact Me!")

with st.form(key='email_form'):
    email = st.text_input("Your email address")
    message = st.text_area("Your message")
    button = st.form_submit_button("Submit")
    mail_text = f"""\
Subject: New mail from {email}

From: {email}
{message} 
"""


if button:
    send_email(mail_text)
    st.info("Mail sent!")