from sql_generator import generate_sql
from utils.helpers import is_safe_sql
from database.db import excute_query

def query_and_answer(question: str):

    print("=" * 50)
    print("QUESTION:")
    print(question)

    cleaned_sql = generate_sql(question)

    print("GENERATED SQL:")
    print(cleaned_sql)

    if not is_safe_sql(cleaned_sql):
        raise ValueError("The generated SQL query is not safe to execute.")

    results = excute_query(cleaned_sql)

    print(f"ROWS RETURNED: {len(results)}")

    return {
        "sql_query": cleaned_sql,
        "results": results,
    }