from sql_generator import generate_sql

question = "What are the top 10 product categories by revenue?"
sql = generate_sql(question)
print(sql)