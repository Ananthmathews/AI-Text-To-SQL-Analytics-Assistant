from sqlalchemy import create_engine

engine = create_engine("MYSQL_CONNECTION_STRING")

with engine.connect() as conn:
    print("Connected to MySQL database successfully!")
