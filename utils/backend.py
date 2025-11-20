import requests

BACKEND_URL = "http://localhost:8000/query"

def query_backend(question: str) -> str:
    """
    Sends a question to the backend API.
    If backend is not running, returns a mock response.
    """
    try:
        response = requests.post(
            BACKEND_URL,
            json={"question": question},
            timeout=20
        )
        response.raise_for_status()
        data = response.json()

        return data.get("answer", "⚠️ Backend returned no answer.")

    except Exception as e:
        # No backend? Return mock response so you can continue testing
        return f"(Mock Response) You asked: '{question}'. Backend not available yet."
