import streamlit as st
import pandas as pd

from graph.workflow import workflow
from visualization.dashboard_builder import build_dashboard
from visualization.insights import simple_insights

st.set_page_config(
    page_title="Text-To-SQL Analytics Assistant",
    page_icon="📊",
    layout="wide",
)

st.title("📊 Text-To-SQL Analytics Assistant")
st.caption("Ask questions in plain English → SQL → Dashboard → Insights")

# ----------------------------
# Sidebar
# ----------------------------

with st.sidebar:

    st.header("Example Questions")

    examples = [
        "Show monthly revenue trend",
        "Top 10 product categories by revenue",
        "How many orders were placed in each customer state?",
        "What is the average review score?",
    ]

    for ex in examples:

        if st.button(ex, width="stretch"):
            st.session_state["question"] = ex

# ----------------------------
# Input
# ----------------------------

question = st.text_input(
    "Ask a question",
    value=st.session_state.get("question", ""),
    placeholder="e.g. Show monthly revenue trend",
)

# ----------------------------
# Submit
# ----------------------------

if st.button("Submit", type="primary"):

    if not question.strip():

        st.warning("Please enter a question.")
        st.stop()

    with st.spinner("Generating SQL and running query..."):

        try:

            response = workflow.invoke(
                {
                    "question": question
                }
            )

        except Exception as e:

            st.error(str(e))
            st.stop()

    # ----------------------------
    # Graph Errors
    # ----------------------------

    if response.get("error"):

        st.error(
            response["error"]
        )

        st.stop()

    sql = response["sql_query"]
    df = pd.DataFrame(response["results"])

    # ----------------------------
    # SQL
    # ----------------------------

    st.subheader("Generated SQL")

    st.code(
        sql,
        language="sql"
    )

    # ----------------------------
    # Dashboard Generation
    # ----------------------------

    dashboards = build_dashboard(df)

    st.subheader("Analytics Dashboard")

    # ----------------------------
    # KPI Cards
    # ----------------------------

    if dashboards.get("kpis"):

        metrics = dashboards["kpis"]

        metric_cols = st.columns(len(metrics))

        for i, (name, value) in enumerate(metrics.items()):

            metric_cols[i].metric(
                name.replace("_", " ").title(),
                value
            )

    # ----------------------------
    # Charts
    # ----------------------------

    st.subheader("Charts")

    chart_col1, chart_col2 = st.columns(2)

    with chart_col1:

        if "bar" in dashboards:

            st.plotly_chart(
                dashboards["bar"],
                width="stretch"
            )

        if "line" in dashboards:

            st.plotly_chart(
                dashboards["line"],
                width="stretch"
            )

        if "scatter" in dashboards:

            st.plotly_chart(
                dashboards["scatter"],
                width="stretch"
            )

    with chart_col2:

        if "pie" in dashboards:

            st.plotly_chart(
                dashboards["pie"],
                width="stretch"
            )

        if "histogram" in dashboards:

            st.plotly_chart(
                dashboards["histogram"],
                width="stretch"
            )

    # ----------------------------
    # Data Table
    # ----------------------------

    st.subheader("Data")

    st.dataframe(
        df,
        width="stretch",
        height=450
    )

    # ----------------------------
    # Insights
    # ----------------------------

    st.subheader("Insights")

    insights = simple_insights(
        df,
        question
    )

    for insight in insights:

        st.markdown(
            f"- {insight}"
        )