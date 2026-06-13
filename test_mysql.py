from sqlalchemy import create_engine

engine = create_engine("mysql+pymysql://sqlagent:Agent123@localhost:3306/ecommerce_ai")

with engine.connect() as conn:
    print("Connected to MySQL database successfully!")
