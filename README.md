# Agentic Chatbot

## Project Overview
The **Agentic Chatbot** is an AI-powered conversational agent designed to interact intelligently with users by leveraging **ReAct agents** and **large language models (LLMs)**. It combines reasoning, tool usage, and natural language understanding to provide context-aware responses and execute actions when required.

The chatbot is built with a **modular architecture**:
- **LangChain** powers the ReAct agents and integrates external tools.
- **FastAPI** handles API endpoints for backend communication.
- **Groq** and **OpenAI** provide LLM capabilities for natural language understanding and response generation.
- **Streamlit** provides an interactive, user-friendly frontend for seamless user interaction.
- **Uvicorn** hosts the backend efficiently for fast API responses.

This project demonstrates the capabilities of modern **agentic AI systems**, combining reasoning, tool usage, and AI-driven conversation into a single application. It can serve as a foundation for building **AI assistants, virtual interviewers, or intelligent workflow automation agents**.

---

## Tech Stack
- **LangChain** – ReAct agents & tools integration
- **FastAPI** – Backend API
- **Groq** – LLM inference
- **OpenAI** – Natural language processing
- **Streamlit** – Frontend UI
- **Uvicorn** – Hosting and serving backend
- **Python** – Programming language

---

## Installation

1. **Clone the repository**
```bash
git clone https://github.com/Shristy-29/agentic-chatbot.git
cd agentic-chatbot

2. **Create a virtual environment**
```bash
# On Mac/Linux
python3 -m venv venv
source venv/bin/activate

# On Windows
python -m venv venv
venv\Scripts\activate

3. **Install dependencies**
```bash
pip install -r requirements.txt

4. **Setup environment variables**
Copy .env.example to .env and add your API keys
```bash
cp .env.example .env  # Mac/Linux
copy .env.example .env  # Windows

## **Usage**

1. **Start the backend server**  
Make sure your virtual environment is activated and run:
```bash
uvicorn backend:app --reload

2. **Launch the frontend**
```bash
streamlit run frontend/frontend.py

3. Open the Streamlit UI in your browser to interact with the chatbot

## Project Structure

agentic-chatbot/
│
├─ backend/
│   ├─ ai_agent.py
│   └─ backend.py
│
├─ frontend/
│   └─ frontend.py
│
├─ .env.example
├─ .gitignore
├─ requirements.txt
└─ README.md


git clone https://github.com/Shristy-29/agentic-chatbot.git
cd agentic-chatbot
