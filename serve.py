from fastapi import FastAPI
from langchain_core.prompts import ChatPromptTemplate
from langchain_core.output_parsers import StrOutputParser
from langchain_groq import ChatGroq
from langserve import add_routes
from dotenv import load_dotenv
import os
import uvicorn

# Load environment variables
load_dotenv()

# Get Groq API Key
groq_api_key = os.getenv("GROQ_API_KEY")

if not groq_api_key:
    raise ValueError("GROQ_API_KEY not found in .env")

# Create LLM
llm = ChatGroq(
    model="llama-3.1-8b-instant",
    groq_api_key=groq_api_key
)

# Prompt Template
prompt = ChatPromptTemplate.from_messages(
    [
        ("system", "Translate the following text into {language}."),
        ("human", "{text}")
    ]
)

# Output Parser
parser = StrOutputParser()

# LCEL Chain
chain = prompt | llm | parser

# FastAPI App
app = FastAPI(
    title="LangServe Demo",
    version="1.0",
    description="A simple translation API using LangChain Expression Language"
)

# Add LangServe Route
add_routes(
    app,
    chain,
    path="/chain"
)

# Run Server
if __name__ == "__main__":
    uvicorn.run(
        app,
        host="127.0.0.1",
        port=8000
    )
