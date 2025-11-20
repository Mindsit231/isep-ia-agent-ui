import streamlit as st
import uuid
from utils.backend import query_backend


if "conversations" not in st.session_state:
    st.session_state.conversations = {}

if "current_chat_id" not in st.session_state:
    st.session_state.current_chat_id = None


def start_new_chat():
    chat_id = str(uuid.uuid4())[:8]
    st.session_state.conversations[chat_id] = {
        "title": "New Chat",
        "messages": []
    }
    st.session_state.current_chat_id = chat_id
    return chat_id

# Auto-start first chat
if st.session_state.current_chat_id is None:
    start_new_chat()


with st.sidebar:
    st.markdown(" 💬 GenAI Chat")

    if st.button("➕ New Conversation", use_container_width=True):
        start_new_chat()
        st.rerun()

    st.markdown("### Recent Chats")
    for cid, chat in st.session_state.conversations.items():
        if st.button(chat["title"], key=cid, use_container_width=True):
            st.session_state.current_chat_id = cid
            st.rerun()


chat_id = st.session_state.current_chat_id
chat_obj = st.session_state.conversations[chat_id]

if len(chat_obj["messages"]) == 0:
    st.markdown(
        """
        <h3 style="text-align:center; margin-top:20px;">How can I help you today?</h3>
        <p style="text-align:center; color:#9ca3af;">Ask any question based on your documents.</p>
        """,
        unsafe_allow_html=True,
    )

# Display messages
for msg in chat_obj["messages"]:
    with st.chat_message(msg["role"]):
        st.write(msg["content"])

# Auto-scroll to bottom
js = """
<script>
window.scrollTo(0, document.body.scrollHeight);
</script>
"""
st.markdown(js, unsafe_allow_html=True)


# Chat input
user_input = st.chat_input("Type your message...")

if user_input:
    chat_obj["messages"].append({"role": "user", "content": user_input})

    if chat_obj["title"] == "New Chat":
        chat_obj["title"] = user_input[:25] + "..."

    # Backend or mock response
    with st.spinner("Assistant is thinking..."):
        reply = query_backend(user_input)


    chat_obj["messages"].append({"role": "assistant", "content": reply})

    st.rerun()
