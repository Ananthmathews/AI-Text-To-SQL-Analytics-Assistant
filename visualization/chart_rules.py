def pick_chart_type(question: str, df):

    q = question.lower()

    cols = df.columns.tolist()

    numeric_cols = df.select_dtypes(
        include=["number"]
    ).columns.tolist()

    # KPI
    if len(df.columns) == 1:
        return "kpi"

    # Time Series
    if any(
        w in q
        for w in [
            "trend",
            "monthly",
            "daily",
            "yearly",
            "over time"
        ]
    ):
        return "line"

    # Pie
    if any(
        w in q
        for w in [
            "share",
            "percentage",
            "proportion",
            "contribution",
            "market share"
        ]
    ):
        return "pie"

    # Scatter
    if "relationship" in q or "correlation" in q:
        return "scatter"

    # Histogram
    if "distribution" in q:
        return "histogram"

    return "bar"