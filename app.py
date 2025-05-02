#R1 model
import os
import streamlit as st
import base64
import google.generativeai as genai
from google import genai
from google.genai import types
from dotenv import load_dotenv
from PIL import Image
import google.generativeai as genai

# Load the API key from the environment variable
load_dotenv()
key = os.getenv('api_key')

genai.configure(api_key=key)


#icon 
icon = Image.open("valorant-logo.png")

#page title config
st.set_page_config(
    page_icon=icon,
    layout='centered',
    page_title="Valo R1 Model"
)

st.markdown(f"""
            <style>
            .stApp {{
                background-image: url("https://i.pinimg.com/originals/fd/11/a1/fd11a15d48f729f8054ca5cff46d55c8.gif"); 
                background-attachment: fixed;
                background-size: cover;
            }}
            .chat-message {{
                background-color: #808080;
                border-radius: 0px;
                padding: 10px;
                margin-bottom: 0px;
                /* From https://css.glass */
                background: rgba(255, 255, 255, 0.03);
                border-radius: 16px;
                box-shadow: 0 4px 30px rgba(0, 0, 0, 0.1);
                backdrop-filter: blur(6.2px);
                -webkit-backdrop-filter: blur(6.2px);
                border: 1px solid rgba(255, 255, 255, 0.18);
            }}
            .user-message {{
                /* From https://css.glass */
                background: rgba(255, 255, 255, 0.03);
                border-radius: 16px;
                box-shadow: 0 4px 30px rgba(0, 0, 0, 0.1);
                backdrop-filter: blur(6.2px);
                -webkit-backdrop-filter: blur(6.2px);
                border: 1px solid rgba(255, 255, 255, 0.18);
            }}
            .bot-message {{
                /* From https://css.glass */
                background: rgba(255, 255, 255, 0.03);
                border-radius: 16px;
                box-shadow: 0 4px 30px rgba(0, 0, 0, 0.1);
                backdrop-filter: blur(6.2px);
                -webkit-backdrop-filter: blur(6.2px);
                border: 1px solid rgba(255, 255, 255, 0.18);
            }}
            </style>
            """, unsafe_allow_html=True)

c30, c31, c32 = st.columns([0.02, 0.3, 3])

with c30:
    st.caption(" ")
    st.image("valorant-logo.png", width=120)

with c32:
    st.title("Valo R1 Model")

st.subheader(' ', divider='rainbow')


# Define the model configuration
generation_config = {
    "temperature": 0.89,
    "top_p": 0.95,
}

#safety settings
safety_settings = [
    {"category": "HARM_CATEGORY_HARASSMENT", "threshold": "BLOCK_MEDIUM_AND_ABOVE"},
    {"category": "HARM_CATEGORY_HATE_SPEECH", "threshold": "BLOCK_MEDIUM_AND_ABOVE"},
    {"category": "HARM_CATEGORY_SEXUALLY_EXPLICIT", "threshold": "BLOCK_MEDIUM_AND_ABOVE"},
    {"category": "HARM_CATEGORY_DANGEROUS_CONTENT", "threshold": "BLOCK_MEDIUM_AND_ABOVE"},
]

# Initialize the model
model = genai.GenerativeModel(
    model_name="gemma-3-27b-it",
    generation_config=generation_config,
    safety_settings=safety_settings
)

# Initialize chat history
if 'chat_history' not in st.session_state:
    st.session_state.chat_history = []

# User input
ask = st.text_input("Ask Me Anything:")

# Handle user input and generate response
if st.button("Send"):
    if ask:
        prompt_parts = [ask]
        
        # Generate response from the model
        response = model.generate_content(prompt_parts)
        
        # Store the conversation in chat history
        st.session_state.chat_history.append({"user": ask, "bot": response.text})

# Display chat history
for chat in st.session_state.chat_history:
    st.markdown(f"<div class='chat-message user-message'><strong>🙍‍♂️ You:</strong> {chat['user']}</div>", unsafe_allow_html=True)
    st.markdown(f"<div class='chat-message bot-message'><strong>🤖 Bot:</strong> {chat['bot']}</div>", unsafe_allow_html=True)
    st.subheader(' ', divider='rainbow')  # Separator for readability