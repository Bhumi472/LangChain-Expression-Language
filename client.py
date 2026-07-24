import requests
import streamlit as st

st.title("🌍 Language Translator using LCEL")

text = st.text_input("Enter Text")

language = st.selectbox(
    "Translate To",
    ["French", "Hindi", "Spanish", "German", "Japanese"]
)


def get_response(text, language):

    url = "http://127.0.0.1:8000/chain/invoke"

    payload = {
        "input": {
            "language": language,
            "text": text
        }
    }

    response = requests.post(url, json=payload)

    print("Status Code:", response.status_code)
    print("Response:", response.text)

    if response.status_code == 200:
        return response.json()["output"]
    else:
        return response.text


if st.button("Translate"):
    st.write(get_response(text, language))