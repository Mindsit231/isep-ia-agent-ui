import streamlit as st

st.title(" Document Library")

st.info("Mock library. Backend integration pending.")


docs = ["Employee Handbook.pdf", "Safety Rules.docx"]

for d in docs:
    st.write(f"📄 {d}")
    col1, col2 = st.columns([1,1])
    with col1:
        st.button("Delete", key=f"del_{d}")
    with col2:
        st.button("Re-ingest", key=f"ing_{d}")
    st.divider()
