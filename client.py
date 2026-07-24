import streamlit as st

from langchain_groq import ChatGroq
from langchain_core.prompts import ChatPromptTemplate
from langchain_core.output_parsers import StrOutputParser

# -------------------- Page Config --------------------
st.set_page_config(
    page_title="Language Translator using LCEL",
    page_icon="🌍",
    layout="centered"
)

st.title("🌍 Language Translator using LCEL")

# -------------------- Load API Key --------------------
try:
    groq_api_key = st.secrets["GROQ_API_KEY"]
except Exception:
    st.error("❌ GROQ_API_KEY not found in Streamlit Secrets.")
    st.stop()

# -------------------- Create LLM --------------------
llm = ChatGroq(
    model="llama-3.1-8b-instant",
    groq_api_key=groq_api_key
)

# -------------------- Prompt --------------------
prompt = ChatPromptTemplate.from_messages(
    [
        ("system", "Translate the following text into {language}."),
        ("human", "{text}")
    ]
)

# -------------------- Output Parser --------------------
parser = StrOutputParser()

# -------------------- LCEL Chain --------------------
chain = prompt | llm | parser

# -------------------- UI --------------------
text = st.text_area(
    "Enter Text",
    placeholder="Type something..."
)

language = st.selectbox(
    "Translate To",
    [
        "French",
        "Hindi",
        "Spanish",
        "German",
        "Japanese",
        "Italian",
        "Marathi"
    ]
)

# -------------------- Translate --------------------
if st.button("Translate"):

    if text.strip() == "":
        st.warning("Please enter some text.")
    else:

        with st.spinner("Translating..."):

            try:
                result = chain.invoke(
                    {
                        "language": language,
                        "text": text
                    }
                )

                st.success("Translation Completed ✅")
                st.write(result)

            except Exception as e:
                st.error(f"Error: {e}")