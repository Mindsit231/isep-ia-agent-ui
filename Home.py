import streamlit.web.cli as stcli
__hidden = True


import streamlit as st



st.set_page_config(
    page_title="GenAI Document Repository",
    page_icon="📄",
    layout="wide",
    initial_sidebar_state="expanded"
)


st.switch_page("pages/1_Chat.py")
