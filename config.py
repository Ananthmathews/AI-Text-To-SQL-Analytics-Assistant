import os
from dotenv import load_dotenv
# Load environment variables from .env file

load_dotenv()
DATABASE_URL = os.getenv("DATABASE_URL")

# LLM settings
OPENAI_API_KEY = os.getenv("OPENAI_API_KEY")
LLM_PROVIDER = os.getenv("LLM_PROVIDER") 
# vector database
CHROMA_PATH = os.getenv("CHROMA_PATH")    
