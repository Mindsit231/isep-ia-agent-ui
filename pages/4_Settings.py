import streamlit as st

st.title("⚙️ Settings")

st.subheader("Model Configuration")
st.selectbox(
    "Choose a model",
    ["Mock Model", "GPT-4 (API)", "Llama 3.1", "Mistral 7B"]
)

st.subheader("Theme")
st.radio("Choose theme", ["Dark", "Light"], index=0)
