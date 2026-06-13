import pandas as pd
import plotly.express as px
import plotly.graph_objects as go


def build_chart(df: pd.DataFrame, chart_type: str, question: str):

    if df.empty:
        return None

    if chart_type in ["none", "kpi"]:
        return None

    cols = df.columns.tolist()

    if len(cols) < 2 and chart_type not in ["histogram"]:
        return None

    x_col = cols[0]
    y_col = cols[1] if len(cols) > 1 else cols[0]

    # Line Chart
    if chart_type == "line":

        fig = px.line(
            df,
            x=x_col,
            y=y_col,
            title=question,
            markers=True,
        )

    # Bar Chart
    elif chart_type == "bar":

        fig = px.bar(
            df,
            x=x_col,
            y=y_col,
            title=question,
            text=y_col,
        )

        fig.update_traces(
            texttemplate="%{text:.2s}",
            textposition="outside"
        )

    # Pie Chart
    elif chart_type == "pie":

        fig = px.pie(
            df,
            names=x_col,
            values=y_col,
            title=question,
            hole=0.4,
        )

    # Scatter Plot
    elif chart_type == "scatter":

        fig = px.scatter(
            df,
            x=x_col,
            y=y_col,
            title=question,
        )

    # Histogram
    elif chart_type == "histogram":

        fig = px.histogram(
            df,
            x=x_col,
            title=question,
        )

    else:
        return None

    fig.update_layout(
        template="plotly_white",
        title_font_size=18,
        title_x=0.02,
        hovermode="x unified",
        height=500,
        margin=dict(
            l=20,
            r=20,
            t=60,
            b=20,
        ),
    )

    return fig


def build_kpi_cards(df: pd.DataFrame):
    """
    If result contains a single row
    and numeric columns,
    show KPI cards.
    """

    if df.empty or len(df) != 1:
        return None

    metrics = {}

    for col in df.columns:

        value = df[col].iloc[0]

        if isinstance(value, (int, float)):
            metrics[col] = value

    return metrics if metrics else None