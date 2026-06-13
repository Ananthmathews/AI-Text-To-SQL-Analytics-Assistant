from typing import TypedDict, Any

class GraphState(TypedDict):

    question: str
    sql_query: str
    results: list[Any]
    error: str
