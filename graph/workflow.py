from langgraph.graph import StateGraph
from graph.state import GraphState

from graph.nodes import (
    generate_sql_node,
    validate_sql_node,
    excute_sql_node
)

def build_graph():

    graph = StateGraph(GraphState)

    graph.add_node(
        "generate_sql",
        generate_sql_node
    )

    graph.add_node(
        "validate_sql",
        validate_sql_node
    )

    graph.add_node(
        "excute_sql",
        excute_sql_node
    )

    graph.set_entry_point(
        "generate_sql"
    )

    graph.add_edge(
        "generate_sql",
        "validate_sql"
    )

    graph.add_edge(
        "validate_sql",
        "excute_sql"
    )

    return graph.compile()

workflow = build_graph()



