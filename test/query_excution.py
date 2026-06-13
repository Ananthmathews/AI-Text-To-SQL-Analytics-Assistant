import pandas as pd
from query_exc_service import query_and_answer

question = "How many orders were placed in each customer state?"

response = query_and_answer(question)

print(f"Return: {len(response['results'])} rows")

df = pd.DataFrame(response["results"])

print(df)