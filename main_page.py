import streamlit as st

st.markdown("# Main page 🎈")
st.sidebar.markdown("# Main page 🎈")

title = st.text_input('Movie title', 'Life of Brian')
st.write('The current movie title is', title+'DJ')