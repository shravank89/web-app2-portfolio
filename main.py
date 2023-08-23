import streamlit as st
import pandas

st.set_page_config(layout="wide")

col1, col2 = st.columns(2)

with col1:
    st.image("images/image.jpg")

with col2:
    st.title("Shravan Kumar")
    content = """
    Hi, I am Shravan! I am an advancing Data Engineer. I have graduated as a Bachelor of Technology in Electronics 
    Engineering. I have 11 years of IT Experience in Python development and Big Data Technologies.
    """
    st.info(content)
content2="""
Below you can find some of the app that i have built in Python. Feel free to contact me!
"""
st.write(content2)

col3, col4 = st.columns(2)

df = pandas.read_csv("data.csv",sep=";")

with col3:
    for index, row in df[:10].iterrows():
        st.header(row["title"])

with col4:
    for index, row in df[10:].iterrows():
        st.header(row["title"])

