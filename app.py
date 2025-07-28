import streamlit as st
from components.form import input_form
from components.display import display_entries
from database.db import create_table, save_entry, get_entries_by_date
from agent.reflection_agent import generate_insights
from datetime import datetime
import os
from dotenv import load_dotenv

# Load environment variables
load_dotenv()

# Initialize session state
if 'submitted' not in st.session_state:
    st.session_state.submitted = False

if 'reflection' not in st.session_state:
    st.session_state.reflection = ""

if 'strategy' not in st.session_state:
    st.session_state.strategy = ""

# Create database table
create_table()

# App title
st.title("ConsciousDay Agent")
st.markdown("*Reflect inward. Act with clarity.*")

# Input form
journal, intention, dream, priorities = input_form()

# Submit button with session state management
if st.button("Generate Insights", key="submit_button"):
    if journal and intention and dream and priorities:
        try:
            with st.spinner("Generating insights..."):
                reflection, strategy = generate_insights(journal, intention, dream, priorities)
                
                # Store in session state
                st.session_state.reflection = reflection
                st.session_state.strategy = strategy
                st.session_state.submitted = True
                
                # Save to database
                date = datetime.now().strftime("%Y-%m-%d")
                save_entry(date, journal, intention, dream, priorities, reflection, strategy)
                
                st.success("Insights generated and saved successfully!")
        except Exception as e:
            st.error(f"Error generating insights: {str(e)}")
            st.info("Please check your API keys or try again later.")
    else:
        st.warning("Please fill in all fields before submitting.")

# Display results if submitted
if st.session_state.submitted:
    st.subheader("Your Daily Insights")
    
    col1, col2 = st.columns(2)
    
    with col1:
        st.markdown("### Reflection")
        st.write(st.session_state.reflection)
    
    with col2:
        st.markdown("### Strategy")
        st.write(st.session_state.strategy)

# Display previous entries
st.subheader("Previous Entries")
selected_date = st.date_input("Select a date to view previous entries")
entries = get_entries_by_date(selected_date.strftime("%Y-%m-%d"))
display_entries(entries)