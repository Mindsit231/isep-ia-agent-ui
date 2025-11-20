import streamlit as st

st.title("📂 Upload & Ingest")

uploaded_files = st.file_uploader(
    "Upload documents",
    type=["pdf", "docx", "pptx", "xlsx"],
    accept_multiple_files=True
)

if uploaded_files:
    st.success(f"{len(uploaded_files)} file(s) uploaded successfully!")
    if st.button("Ingest Files"):
        with st.spinner("Processing documents..."):
            st.success("Mock: Documents processed and indexed.")
