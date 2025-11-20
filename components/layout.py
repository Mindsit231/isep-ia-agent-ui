import streamlit as st
from pathlib import Path

def init_page(page_title: str):
    """Set page config + load global CSS once per page."""
    st.set_page_config(
        page_title=page_title,
        page_icon="📄",
        layout="wide",
        initial_sidebar_state="expanded",
    )
    load_css()
    sidebar_brand()

def load_css():
    css_path = Path("assets/styles.css")
    if css_path.exists():
        with open(css_path) as f:
            st.markdown(f"<style>{f.read()}</style>", unsafe_allow_html=True)

def sidebar_brand():
    with st.sidebar:
        st.markdown("###  GenAI Doc Repository")
        st.caption("Masters project – ISEP / MindsIT")

def page_header(title: str, subtitle: str | None = None):
    st.markdown(f"## {title}")
    if subtitle:
        st.markdown(f"<p style='color:#9ca3af'>{subtitle}</p>", unsafe_allow_html=True)
    st.markdown("---")
