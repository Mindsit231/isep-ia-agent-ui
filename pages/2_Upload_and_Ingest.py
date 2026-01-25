import streamlit as st
from utils.backend import upload_file_to_backend

st.title(" Upload & Ingest")

uploaded_files = st.file_uploader(
    "Upload documents",
    type=["pdf", "docx", "txt", "pptx", "xlsx"],
    accept_multiple_files=True
)

if uploaded_files:
    st.success(f"{len(uploaded_files)} file(s) uploaded successfully!")

    if st.button("Ingest Files"):
        with st.spinner("Uploading and processing documents..."):
            for file in uploaded_files:
                try:
                    result = upload_file_to_backend(file)
                    st.write(f" {file.name}: {result.get('message', 'Uploaded')}")
                    if 'collection' in result:
                        st.info(f"Indexed in collection: {result['collection']}")
                except Exception as e:
                    st.error(f" {file.name}: {e}")
