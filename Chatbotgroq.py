import streamlit as st
import joblib
import pandas as pd
import os

from groq import Groq



#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
st.write("# Chat Bot 3.14")

client = Groq(
    api_key=os.environ.get("GROQ_API_KEY"),
)

chat_completion = client.chat.completions.create(
    messages=[
        {
            "role": "user",
            "content": "Explain the importance of fast language models",
        }
    ],
    model="llama3-8b-8192",
)

print(chat_completion.choices[0].message.content)