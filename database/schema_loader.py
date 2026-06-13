from database.db import excute_query

def get_schema_documents():
    # Query to get table names and their columns
    query = """
    SELECT
        TABLE_NAME,
        COLUMN_NAME,
        DATA_TYPE
    FROM
        INFORMATION_SCHEMA.COLUMNS
    WHERE
        TABLE_SCHEMA = "ecommerce_ai"
        ORDER BY TABLE_NAME, ORDINAL_POSITION;
    """

    rows = excute_query(query)

    schema = {}

    skip_tables = {
        "train",
        "test",
        "sample_submission",
        "formulatedtest",
    }

    for row in rows:
        table_name = row["TABLE_NAME"]
        if table_name in skip_tables:
            continue
        column_info = f"{row['COLUMN_NAME']} ({row['DATA_TYPE']})"

        schema.setdefault(table_name, [])
        schema[table_name].append(column_info)
    # Convert the schema dictionary to a list of documents
    documents = []
    for table_name, columns in schema.items():
        documents.append({"table": table_name, "columns": columns})

    return documents
if __name__ == "__main__":
    doc = get_schema_documents()
    print(f"found {len(doc)} tables in the database")
    print(doc[0])