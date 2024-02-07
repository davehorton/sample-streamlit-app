
import streamlit as st
import json

st.set_page_config(page_title="Few-shot examples", page_icon="📄")
st.header('Some Few-shot examples')

examples = st.text_area("Add or edit as desired:", height=500, value=st.session_state.examples)
st.session_state['examples'] = examples
