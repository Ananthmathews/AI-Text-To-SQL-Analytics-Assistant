import pandas as pd
import plotly.express as px


def build_dashboard(df: pd.DataFrame):

    dashboard = {}

    if df.empty:
        return dashboard

    cols = df.columns.tolist()

    numeric_cols = df.select_dtypes(
        include=["number"]
    ).columns.tolist()

    # ------------------
    # KPI Metrics
    # ------------------

    metrics = {}

    if len(df) == 1:

        for col in numeric_cols:
            metrics[col] = df[col].iloc[0]

    dashboard["kpis"] = metrics

    # ------------------
    # Charts
    # ------------------

    if len(cols) >= 2 and len(numeric_cols) >= 1:

        x_col = cols[0]
        y_col = numeric_cols[0]

        # BAR

        dashboard["bar"] = px.bar(
            df,
            x=x_col,
            y=y_col,
            title=f"{y_col} by {x_col}",
            color=y_col,
        )

        # PIE

        dashboard["pie"] = px.pie(
            df,
            names=x_col,
            values=y_col,
            title=f"{y_col} Share",
            hole=0.4,
        )

        # LINE

        dashboard["line"] = px.line(
            df,
            x=x_col,
            y=y_col,
            title=f"{y_col} Trend",
            markers=True,
        )

        # SCATTER

        dashboard["scatter"] = px.scatter(
            df,
            x=x_col,
            y=y_col,
            title=f"{y_col} Relationship",
            color=y_col,
        )

    # ------------------
    # HISTOGRAM
    # ------------------

    if len(numeric_cols) > 0:

        dashboard["histogram"] = px.histogram(
            df,
            x=numeric_cols[0],
            title=f"{numeric_cols[0]} Distribution",
        )

    return dashboard