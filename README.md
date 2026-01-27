#  GenAI Document Repository – Frontend (UI)

This repository contains the **frontend user interface** for the **GenAI Document Repository** project.
The UI provides an intuitive, chat-based interface that allows users to upload documents, ask questions, and view AI-generated responses.

The frontend is designed to be **simple, responsive, and backend-ready**, focusing purely on user experience.

---

##  Purpose of This Repository

The goal of this repository is to:

* Provide a **clean web interface** for interacting with the GenAI system
* Enable **document upload and management**
* Support a **chat-based question answering experience**
* Prepare the UI for **seamless backend integration**

>  Note: This repository handles **UI only**. Backend and AI logic are managed in separate repositories.

---

## Features

###  Sidebar Navigation

* Home
* Chat
* Upload and Ingest
* Library
* Settings
* About

###  Chat Interface

* Chat-style interaction similar to modern AI assistants
* Input box for user questions
* Display area for AI-generated responses
* Support for **multiple conversations**
* Conversation history stored per session

###  Document Library

* View uploaded documents
* Mock document list (backend integration pending)
* Actions available:

  * Delete document
  * Re-ingest document

###  UI Design

* Dark theme interface
* Custom CSS for improved appearance
* Simple and minimal layout for better usability

---

##  Technology Stack (Frontend)

* **Streamlit** – Web application framework
* **Python** – Core programming language
* **Streamlit Session State** – Session and chat history management
* **Custom CSS** – Styling and UI enhancements
* **Streamlit Chat Components** – Conversational UI

---

##  Current Status

* UI layout fully implemented
* Chat interface functional with mock responses
* Document library view implemented (mock data)
* ⏳ Backend integration pending

> The frontend is **fully ready** to connect with backend APIs for real-time document ingestion and AI responses.

---

##  How to Run the UI Locally

###  Clone the Repository

```bash
git clone <repository-url>
cd isep-ia-agent-ui
```

###  Create a Virtual Environment (Optional)

```bash
python -m venv venv
source venv/bin/activate   # macOS / Linux
```

###  Install Dependencies

```bash
pip install -r requirements.txt
```

###  Run the Application

```bash
streamlit run app.py
```

The application will be available at:

```
http://localhost:8501
```

---

##  Future Improvements

* Connect UI to backend APIs
* Real-time document ingestion status
* Source citation display in chat responses
* Advanced conversation history management
* Document-level filters during chat

---

##  Contributors (Frontend)

* **Sai Krishna Reddy**
* **Soniya**

---

##  Note

This repository focuses **only on the frontend**.
Backend logic, embeddings, vector databases, and RAG pipelines are handled in separate repositories.


