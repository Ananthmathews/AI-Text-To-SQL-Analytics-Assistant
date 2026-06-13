import re

def clean_sql(text: str) -> str:
    
    # Remove leading and trailing whitespace
    text = text.strip()

    if text.startswith("```"):
        text =re.sub(
            r"^```(?:sql)?\s*",
            "",
            text,
            flags=re.IGNORECASE
        )

        text = re.sub(
            r"\s*```$",
            "",
            text,
            flags=re.IGNORECASE
        )
    return text.strip().rstrip(";") + ";"

    
# Dangerous sql commands
FORBEDDIN = re.compile(
    r"\b(DROP|DELETE|UPDATE|INSERT|ALTER|TRUNCATE|CREATE|RENAME|GRANT|REVOKE|EXECUTE|MERGE|CALL)\b",
    re.IGNORECASE
)

def is_safe_sql(sql:str) ->bool:
    sql = sql.strip().rstrip(";")

    # Reject if any forbidden keywords are present
    if FORBEDDIN.search(sql):
        return False
    normalized = sql.strip().upper()
    return normalized.startswith("SELECT") or normalized.startswith("WITH")