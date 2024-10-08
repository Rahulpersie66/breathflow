import streamlit as st

def menu():
  st.sidebar.page_link("app.py", label="🏠 Home")
  st.sidebar.page_link("pages/feedback.py", label="🖼️ Posture Analysis")
  st.sidebar.page_link("pages/grading.py", label="📺 Motion Analysis")
