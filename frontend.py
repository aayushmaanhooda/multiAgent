# setup ui with streamlit (model provider, model, system prompt, query)
import streamlit as st
import os

# Use environment variable for API URL, fallback to localhost for development
# For Render deployment, BACKEND_URL should be set to your backend service URL
API_URL = os.getenv("BACKEND_URL", "https://multiagent-piqd.onrender.com/") + "/chat"

st.set_page_config(page_title="Langraph Agent UI", layout="wide")
st.title("AI Chatbot Agent")
st.write("Create and Interact with the AI Agents!")


system_prompt = st.text_area(
    "Define your AI Agent: ", height=30, placeholder="Type your system propmpt here...."
)

MODEL_NAMES_GROQ = ["llama-3.3-70b-versatile", "llama3-70b-8192"]
MODEL_NAMES_OPENAI = ["gpt-4o-mini", "gpt-4o"]

provider = st.radio("Select Provider: ", ("Groq", "OpenAI"))
if provider == "Groq":
    selected_model = st.selectbox("Select Groq Model:", MODEL_NAMES_GROQ)
elif provider == "OpenAI":
    selected_model = st.selectbox("Select OpenAI Model:", MODEL_NAMES_OPENAI)


allow_web_search = st.checkbox("Allow Web Search")

user_query = st.text_area(
    "Enter your Query: ", height=150, placeholder="How can I help you...."
)

if st.button("As Agent!"):
    if user_query.strip():
        # connect with bakcned url
        import requests

        payload = {
            "model_name": selected_model,
            "model_provider": provider,
            "system_prompt": system_prompt,
            "messages": [user_query],
            "allow_search": allow_web_search,
        }

        response = requests.post(API_URL, json=payload)

        if response.status_code == 200:
            response_data = response.json()
            if "error" in response_data:
                st.error(response_data["error"])
            else:
                st.subheader("Agent Response")
                st.markdown(f"**AI:** {response_data}")
