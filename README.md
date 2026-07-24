# 🌍 Language Translator using LangChain Expression Language (LCEL)

A simple Language Translator application built using **LangChain Expression Language (LCEL)** and **Groq LLM** with a **Streamlit** interface.

The primary objective of this project is **to understand and implement LangChain Expression Language (LCEL)** rather than building a complex translation application. It demonstrates how LangChain components can be composed into reusable AI pipelines using LCEL.

---

## 📖 About the Project

LangChain Expression Language (LCEL) is a declarative way of composing AI applications in LangChain. Instead of writing long procedural code, LCEL allows developers to connect prompts, models, output parsers, retrievers, and other components into a single executable pipeline.

This project uses a language translation task as a practical example to understand:

- LCEL chaining
- Prompt Templates
- Chat Models
- Output Parsers
- Runnable Pipelines
- Streamlit integration

---

## 🚀 Features

- Translate text into multiple languages
- Built completely using LCEL
- Groq LLM integration
- Interactive Streamlit UI
- Clean and beginner-friendly implementation
- Easy to extend with more LCEL components

---

## 🛠️ Tech Stack

- Python
- LangChain
- LangChain Expression Language (LCEL)
- LangChain Groq
- Groq API
- Streamlit

---

## 🧠 LCEL Pipeline

The application creates the following execution chain:

```
User Input
      │
      ▼
ChatPromptTemplate
      │
      ▼
Groq Chat Model
      │
      ▼
StrOutputParser
      │
      ▼
Translated Output
```

In code:

```python
chain = prompt | llm | parser
```

This single line is the essence of LangChain Expression Language.

---

## 📂 Project Structure

```
LangChain-Expression-Language/
│
├── client.py
├── requirements.txt
├── simplellmLCEL.ipynb
├── README.md
└── .gitignore
```

---

## ⚙️ Installation

Clone the repository

```bash
git clone https://github.com/Bhumi472/LangChain-Expression-Language.git
```

Move into the project directory

```bash
cd LangChain-Expression-Language
```

Install dependencies

```bash
pip install -r requirements.txt
```

---

## 🔑 Configure API Key

Create a Streamlit Secret named:

```
GROQ_API_KEY
```

or configure it in Streamlit Cloud Secrets.

Example:

```
GROQ_API_KEY="your_groq_api_key"
```

---

## ▶️ Run the Application

```bash
streamlit run client.py
```

---

## 📚 Concepts Covered

This project demonstrates:

- LangChain Expression Language (LCEL)
- Prompt Engineering
- ChatPromptTemplate
- RunnableSequence
- ChatGroq Integration
- StrOutputParser
- AI Pipeline Composition
- Streamlit Deployment

---

## 🎯 Learning Outcome

After completing this project, you will understand:

- What LCEL is
- Why LCEL is used
- How to connect LangChain components
- How AI pipelines are created
- How prompts flow through a model
- How output parsers work
- How to deploy an LCEL application

---

## 🔮 Future Improvements

- Conversation Memory
- Prompt Templates Library
- Multiple LLM Providers
- Streaming Responses
- Chat Interface
- RAG Integration
- LangServe API Version
- Docker Deployment

---

## 👨‍💻 Author

**Bhumi Boinwad**

B.Tech Artificial Intelligence & Data Science

GitHub: https://github.com/Bhumi472
