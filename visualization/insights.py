import pandas as pd


def simple_insights(df: pd.DataFrame, question: str) -> list[str]:
    if df.empty:
        return ["No data returned for this question."]

    bullets = []
    bullets.append(f"Query returned **{len(df)}** rows.")

    cols = df.columns.tolist()
    if len(cols) >= 2:
        y_col = cols[1]
        if pd.api.types.is_numeric_dtype(df[y_col]):
            top = df.loc[df[y_col].idxmax()]
            bullets.append(
                f"Highest **{y_col}**: **{top[y_col]:,.2f}** ({top[cols[0]]})."
            )
            bullets.append(
                f"Total **{y_col}**: **{df[y_col].sum():,.2f}** across all rows."
            )

    return bullets