from langchain_openai import ChatOpenAI
from config import OPENAI_API_KEY

def get_llm():
    return ChatOpenAI(
        model = "gpt-4o-mini",
        api_key = OPENAI_API_KEY,
        temperature = 0,
    )