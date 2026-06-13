from database.schema_loader import get_schema_documents

def table_to_text(table_doc):

    lines = [
        f"table: {table_doc['table']}",
        "columns:"
    ]
    for col in table_doc["columns"]:
        lines.append(f"  - {col}")
    return "\n".join(lines)

def get_all_documents():
    doc = []
    for table_doc in get_schema_documents():
        doc.append(table_to_text(table_doc))
    return doc

