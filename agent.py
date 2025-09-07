import os

# setup and fetch API keys from .env
groq_key = os.environ.get("GROQ_API_KEY")
tavily_key = os.environ.get("TAVILY_API_KEY")
openai_key = os.environ.get("OPENAI_API_KEY")


# setup llm and tools
from langchain_groq import ChatGroq
from langchain_openai import ChatOpenAI
from langchain_tavily import TavilySearch, TavilyExtract

openai_llm = ChatOpenAI(model="gpt-4o")
groq_llm = ChatGroq(model="llama-3.3-70b-versatile")
search_tool = TavilySearch(max_results=2)


# steup ai agent with seach tool functionlaity
from langgraph.prebuilt import create_react_agent
from langchain_core.messages import AIMessage

system_prompt = "Act as an AI chatbot who is smart and friendly"


def ai_agent(llm_id, provider, system_prompt, query, allow_search):
    if provider == "Groq":
        llm = ChatGroq(model=llm_id)
    elif provider == "OpenAI":
        llm = ChatOpenAI(model=llm_id)

    if allow_search:
        tools = [TavilySearch(max_results=2)]
    else:
        tools = []

    agent = create_react_agent(model=llm, tools=tools, prompt=system_prompt)
    state = {"messages": query}
    response = agent.invoke(state)
    messages = response.get("messages")
    ai_message = [
        message.content for message in messages if isinstance(message, AIMessage)
    ]
    return ai_message[-1]
