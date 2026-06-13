from graph.state import GraphState
from sql_generator import generate_sql
from utils.helpers import is_safe_sql
from database.db import excute_query


def generate_sql_node(state: GraphState):

    question = state["question"]

    sql = generate_sql(question)

    state["sql_query"] = sql

    return state


def validate_sql_node(state: GraphState):

    sql = state["sql_query"]

    if not is_safe_sql(sql):
        state["error"] = "Unsafe SQL detected"

    return state


def excute_sql_node(state: GraphState):

    if state.get("error"):
        return state

    results = excute_query(
        state["sql_query"]
    )

    state["results"] = results

    return state