#Step1: Setup API Keys for Groq, OpenAI and Tavily
import os

GROQ_API_KEY=os.environ.get("GROQ_API_KEY")
TAVILY_API_KEY=os.environ.get("TAVILY_API_KEY")
OPENAI_API_KEY=os.environ.get("OPENAI_API_KEY")

#Step2: Setup LLM & Tools
from langchain_groq import ChatGroq
from langchain_openai import ChatOpenAI
from langchain_community.tools.tavily_search import TavilySearchResults

openai_llm=ChatOpenAI(model="gpt-4o-mini")
groq_llm=ChatGroq(model="llama-3.3-70b-versatile")

search_tool=TavilySearchResults(max_results=2)

#Step3: Setup AI Agent with Search tool functionality
from langgraph.prebuilt import create_react_agent
from langchain_core.messages import SystemMessage, HumanMessage, AIMessage

system_prompt="Act as an AI chatbot who is smart and friendly"

def get_response_from_ai_agent(llm_id, messages_list, allow_search, system_prompt, provider):
    if provider=="Groq":
        llm=ChatGroq(model=llm_id)
    elif provider=="OpenAI":
        llm=ChatOpenAI(model=llm_id)
    else:
        raise ValueError("Unsupported provider")

    tools=[TavilySearchResults(max_results=2)] if allow_search else []
    
    agent=create_react_agent(
        model=llm,
        tools=tools
    )
    
    # state={"messages": [AIMessage(content=system_prompt), AIMessage(content=query)]}
    
    # Convert messages_list to HumanMessage objects
    messages_objs = [HumanMessage(content=msg) for msg in messages_list]

    # Full state: system + user messages
    state = {
        "messages": [SystemMessage(content=system_prompt)] + messages_objs
    }

    response=agent.invoke(state)
    messages=response.get("messages", [])
    ai_messages=[m.content for m in messages if isinstance(m, AIMessage)]
    return ai_messages[-1] if ai_messages else "No AI response received."