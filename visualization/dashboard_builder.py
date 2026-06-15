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
            color_continuous_scale= "Viridis"
        )

        # PIE
        if len(df) <= 50:

            dashboard["pie"] = px.pie(
                df,
                names=x_col,
                values=y_col,
                title=f"{y_col} Share",
                hole=0.5
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
            color_continuous_scale="Turbo",
            size=y_col
        )

        # AREA CHART
        dashboard["area"] = px.area(
            df,
            x=x_col,
            y=y_col,
            title=f"{y_col} Trend"

        )

        #  horizontal bar
        dashboard["hbar"] = px.bar(
            df,
            x=y_col,
            y=x_col,
            orientation="h",
            title=f"{y_col} by {x_col}",
            color=y_col,
            color_continuous_scale="Plasma"
        )

        # Box plot
        dashboard["box"] = px.box(
            df,
            y=y_col,
            title=f"{y_col} distribution"
        )

    
        # TREEMAP
        if len(df) <= 50:

            dashboard["treemap"] = px.treemap(
                df,
                path=[x_col],
                values=y_col,
                color=y_col,
                color_continuous_scale="Blues",
                title=f"{y_col} by {x_col}"
                    
            )


        # SUNBURST
    
        if len(df) <= 50:

            dashboard["sunburst"] = px.sunburst(
                df,
                path=[x_col],
                values=y_col,
                title=f"{y_col} Breakdown",
            )


    # ------------------
    # HISTOGRAM
    # ------------------

    if len(numeric_cols) > 0:

        dashboard["histogram"] = px.histogram(
            df,
            x=numeric_cols[0],
            title=f"{numeric_cols[0]} Distribution",
            color_discrete_sequence=["#636EFA"]
        )

    return dashboard