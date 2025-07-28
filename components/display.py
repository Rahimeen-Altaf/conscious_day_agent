import streamlit as st

def display_entries(entries):
    """Display entries for a selected date in a clean format"""
    if entries:
        for i, entry in enumerate(entries):
            with st.expander(f"Entry from {entry[1]}", expanded=False):
                col1, col2 = st.columns(2)
                
                with col1:
                    st.markdown("**Morning Journal:**")
                    st.write(entry[2])
                    
                    st.markdown("**Intention:**")
                    st.write(entry[3])
                    
                    st.markdown("**Dream:**")
                    st.write(entry[4])
                    
                    st.markdown("**Priorities:**")
                    st.write(entry[5])
                
                with col2:
                    st.markdown("**Reflection:**")
                    st.write(entry[6])
                    
                    st.markdown("**Strategy:**")
                    st.write(entry[7])
                
                st.divider()
    else:
        st.info("No entries found for this date. Create your first entry above!")