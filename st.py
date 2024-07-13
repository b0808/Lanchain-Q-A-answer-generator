import os
import streamlit as st
from model import generotor
st.title("Question Generator")
st.sidebar.title("give inputs ")

a = st.sidebar.text_input("enter your topic")
b = st.sidebar.number_input("no of Question",0,20)
c = st.sidebar.selectbox("difficulty level",["easy","medium","hard"])
k = st.sidebar.button("Click")
print(a,b,c,k)

if k :
    response = generotor(a,b,c)
    st.subheader(response['topic'])
    st.markdown(response['Que_no'])
    st.markdown('#') 
    st.markdown(response['Sol'])

