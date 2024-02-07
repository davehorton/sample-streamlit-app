
import streamlit as st

st.set_page_config(page_title="Prompt", page_icon="📄")
st.header('The prompt')

# Using the multiline string as the default value in a text_area
prefix = st.text_area("Edit as desired:", height=500, value=st.session_state.prefix)
st.session_state.prefix = prefix
