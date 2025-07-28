import streamlit as st

def input_form():
    """Create input form for daily entries"""
    journal = st.text_area("Morning Journal")
    intention = st.text_input("Intention of the Day")
    dream = st.text_area("Dream")
    priorities = st.text_input("Top 3 Priorities (comma-separated)")
    return journal, intention, dream, priorities