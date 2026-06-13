from sqlalchemy import create_engine, text
from config import DATABASE_URL

engine = create_engine(DATABASE_URL)

def excute_query(query):
    with engine.connect() as conn:
        results = conn.execute(text(query))
        rows = results.mappings().all()  # Get results as list of dictionaries
        return [dict(row) for row in rows]  # Convert RowMapping to regular dict        
       
