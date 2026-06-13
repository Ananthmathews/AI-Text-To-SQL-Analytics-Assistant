from rag.retriever import retrieve
from prompts.sql_prompt import build_sql_prompt
from models.openai_model import get_llm
from utils.helpers import clean_sql


def generate_sql(question: str):

    schema = retrieve(question)

    prompt = build_sql_prompt(
        question=question,
        schema=schema,
    )

    llm = get_llm()

    response = llm.invoke(prompt)

    cleaned_sql = clean_sql(
        response.content
    )

    return cleaned_sql