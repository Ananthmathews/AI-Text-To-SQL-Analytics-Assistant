# Text-to-SQL + Dashboard Project — Master Guide

**Your goal:** Natural language → SQL → table → chart → insights (e.g. “Show monthly sales trend”).

**Stack:** VS Code, Python, LangChain, LangGraph, OpenAI (later Ollama), MySQL, ChromaDB RAG, Streamlit, Plotly.

**You code it yourself** — this file is your long-term reference. Follow phases in order.

---

## Final outcome (what you are building)

```
User asks: "Show monthly sales trend"

System returns:
  1. Generated SQL
  2. Result table (rows from MySQL)
  3. Chart (line for trends, bar for comparisons)
  4. Short insights (from real query results, not invented)
```

---

## Phase map — do NOT skip

| Phase | What you build | Success = |
|-------|----------------|-----------|
| **0** | VS Code, Python, MySQL, venv, packages | `SELECT 1` in Workbench |
| **1** | MySQL `ecommerce` DB + tables + sample data | `SELECT COUNT(*) FROM orders` works |
| **2** | `.env`, `config.py`, `database/db.py` | Python `run_query()` returns rows |
| **3** | RAG: schema → Chroma | `retrieve("monthly sales")` finds orders/sales tables |
| **4** | LLM generates SQL only | Valid SELECT for 5 test questions |
| **5** | Execute SQL + return table | Question → rows in Python |
| **6** | LangGraph + `main.py` | CLI: question → SQL + table + summary |
| **7** | Streamlit UI | Browser: SQL + dataframe |
| **8** | Charts + insights | “Monthly trend” → line chart + bullets |

**Start now:** Phase 0 → Phase 1.

---

## Where to get software

| Software | URL |
|----------|-----|
| Python 3.10/3.11 | https://www.python.org/downloads/ (check “Add to PATH”) |
| VS Code | https://code.visualstudio.com/ |
| MySQL Installer (Windows) | https://dev.mysql.com/downloads/installer/ |
| MySQL Workbench | Included with installer |
| OpenAI API key | https://platform.openai.com/api-keys |
| Ollama (later, Phase 6+) | https://ollama.com |

---

## VS Code setup (Phase 0)

1. Create folder: `C:\Users\lucky\PycharmProjects\text_sql_queries` (or open this repo folder in VS Code)
2. **File → Open Folder**
3. Extensions: **Python**, **Pylance**
4. Terminal:

```powershell
cd C:\Users\lucky\PycharmProjects\text_sql_queries
python -m venv .venv
.\.venv\Scripts\Activate.ps1
pip install -r requirements.txt
```

5. **Ctrl+Shift+P** → `Python: Select Interpreter` → `.venv`

### requirements.txt

```text
langchain
langchain-openai
langgraph
langchain-community
chromadb
sqlalchemy
pymysql
python-dotenv
pandas
plotly
streamlit
```

---

## Connections — ONLY in `.env`

**Never put API keys in `db.py`, `workflow.py`, etc.**

| Variable | Where to get it |
|----------|-----------------|
| `OPENAI_API_KEY` | platform.openai.com |
| `DATABASE_URL` | See below (MySQL) |
| `CHROMA_PATH` | `./data/chroma` (local folder) |
| `LLM_PROVIDER` | `openai` or later `ollama` |

### `.env` example

```env
OPENAI_API_KEY=sk-your-real-key-here
DATABASE_URL=mysql+pymysql://sqlagent:YourStrongPassword123!@localhost:3306/ecommerce
CHROMA_PATH=./data/chroma
LLM_PROVIDER=openai
OLLAMA_BASE_URL=http://localhost:11434
OLLAMA_MODEL=llama3
```

### `.gitignore`

```text
.env
.venv/
data/
__pycache__/
```

**Flow:** `.env` → `config.py` (load once) → `db.py`, `vector_store.py`, `openai_model.py`

---

## MySQL setup (Phase 1)

### 1. Create database + read-only user (Workbench)

```sql
CREATE DATABASE IF NOT EXISTS ecommerce;
USE ecommerce;

CREATE USER IF NOT EXISTS 'sqlagent'@'localhost' IDENTIFIED BY 'YourStrongPassword123!';
GRANT SELECT ON ecommerce.* TO 'sqlagent'@'localhost';
FLUSH PRIVILEGES;
```

### 2. Run `database/sample_data.sql`

Full script is in that file in this project folder. Tables:

- `customers` — id, name, state, city
- `products` — id, name, category, price
- `orders` — id, customer_id, order_date, total_amount
- `order_items` — order_id, product_id, quantity, line_total

### 3. Test in Workbench

```sql
USE ecommerce;
SELECT COUNT(*) FROM orders;

SELECT DATE_FORMAT(order_date, '%Y-%m') AS month,
       SUM(total_amount) AS total_sales
FROM orders
GROUP BY month
ORDER BY month;
```

Second query = target for **“Show monthly sales trend”**.

---

## Project folder structure

```
text_sql_queries/
├── PROJECT_MASTER_GUIDE.md    ← this file
├── .env
├── .env.example
├── .gitignore
├── requirements.txt
├── config.py
├── main.py
├── app.py
├── data/                      # Chroma + exports (gitignored)
├── database/
│   ├── __init__.py
│   ├── db.py
│   ├── schema_loader.py
│   └── sample_data.sql
├── rag/
│   ├── __init__.py
│   ├── schema_docs.py
│   ├── embeddings.py
│   ├── vector_store.py
│   └── retriever.py
├── prompts/
│   ├── __init__.py
│   ├── sql_prompt.py
│   └── insights_prompt.py
├── models/
│   ├── __init__.py
│   ├── openai_model.py
│   └── ollama_model.py
├── tools/
│   ├── __init__.py
│   ├── rag_tools.py
│   └── sql_tools.py
├── graph/
│   ├── __init__.py
│   ├── state.py
│   └── workflow.py
├── visualization/             # Phase 8
│   ├── __init__.py
│   ├── chart_rules.py
│   ├── chart_builder.py
│   └── insights.py
└── utils/
    ├── __init__.py
    ├── logger.py
    └── helpers.py
```

**Skip for v1:** spaCy, fine-tuning, Pinecone, multi-agent from day 1.

---

## What each file does

| File | Your job |
|------|----------|
| `config.py` | `load_dotenv()`, export all settings |
| `database/db.py` | `create_engine`, `run_query(sql) -> list[dict]` |
| `database/schema_loader.py` | Read MySQL schema (INFORMATION_SCHEMA / inspect) |
| `rag/schema_docs.py` | Format tables + **example Q&A SQL** per table |
| `rag/vector_store.py` | Build/load Chroma at `CHROMA_PATH` |
| `rag/retriever.py` | `retrieve(question, k=5) -> str` |
| `prompts/sql_prompt.py` | SELECT only, use schema context, LIMIT 100 |
| `models/openai_model.py` | `ChatOpenAI` gpt-4o-mini |
| `utils/helpers.py` | `clean_sql()`, `is_safe_select()` |
| `tools/sql_tools.py` | Execute after safety check |
| `graph/state.py` | TypedDict: question, sql, rows, error, final_answer, chart_type, insights |
| `graph/workflow.py` | LangGraph nodes (see below) |
| `main.py` | CLI entry: `graph.invoke()` |
| `app.py` | Streamlit: same graph + charts |
| `visualization/chart_rules.py` | trend → line, top/by → bar |
| `visualization/chart_builder.py` | rows → Plotly figure |
| `visualization/insights.py` | LLM bullets from real rows |

---

## LangGraph workflow (core)

```
START
  → retrieve_schema (RAG)
  → generate_sql (LLM)
  → validate_sql (SELECT only, block DROP/DELETE/UPDATE/INSERT)
  → execute_sql (run_query → rows)
  → format_answer (text summary)
  → [Phase 8] decide_chart → build_chart → generate_insights
END
```

### State fields

```python
question: str
schema_context: str
sql: str
rows: list          # list of dicts — source of truth for table + charts
error: str
final_answer: str
chart_type: str | None   # Phase 8
insights: str             # Phase 8
```

**Rule:** Charts and insights use **`rows` from the database** — never let the LLM invent numbers.

---

## RAG — what to put in Chroma

1. Table + column names + types  
2. Primary/foreign keys  
3. **2–3 example questions + SQL per table** (huge quality boost)  
4. Business notes (“AP” = Andhra Pradesh)  

**Not in RAG for v1:** full row data (only schema + examples).

**Rebuild index when:** schema changes → run `build_index()` again.

---

## Models

| Purpose | Start | Later |
|---------|-------|-------|
| SQL + insights | OpenAI `gpt-4o-mini` | Ollama `llama3` / `sqlcoder` |
| Embeddings | `text-embedding-3-small` | `BAAI/bge-small-en` local |

**No spaCy needed.** Transformers only if you use local embeddings.

---

## Commands cheat sheet

| When | Command |
|------|---------|
| Test config | `python -c "from config import DATABASE_URL; print(DATABASE_URL)"` |
| Test DB | `python -c "from database.db import run_query; print(run_query('SELECT COUNT(*) AS n FROM orders'))"` |
| Build RAG (once) | `python -c "from rag.vector_store import build_index; build_index()"` |
| Test retrieve | `python -c "from rag.retriever import retrieve; print(retrieve('monthly sales trend'))"` |
| Full app | `python main.py` |
| UI | `streamlit run app.py` |

---

## Phase 8 — Dashboard & charts

### Chart rules (start simple)

| Question / result | Chart |
|-------------------|--------|
| trend, monthly, over time | **Line** |
| top N, by category, by state | **Bar** |
| one number, one row | **No chart** (KPI text only) |

### Streamlit layout (`app.py`)

```
[ Chat input ]

--- Generated SQL ---     → st.code(sql, language="sql")
--- Results ---           → st.dataframe(rows)
--- Chart ---             → st.plotly_chart(figure)  # if exists
--- Insights ---          → st.markdown(insights)
```

### Libraries

- `pandas` — rows → DataFrame  
- `plotly` — interactive charts  
- `streamlit` — dashboard UI  

---

## When you change something

| You changed | Update / rerun |
|-------------|----------------|
| New table/column | `sample_data.sql` → Workbench → `build_index()` |
| MySQL password | `.env` only |
| New tool | `graph/workflow.py` + maybe `state.py` |
| Better SQL examples | `schema_docs.py` → `build_index()` |
| New chart type | `chart_rules.py` + workflow node |
| OpenAI → Ollama | `.env` `LLM_PROVIDER` + `ollama_model.py` |

**Usually do NOT change `main.py` when adding tools** — change `workflow.py`.

---

## Week-by-week plan

| Week | Phases | Deliverable |
|------|--------|-------------|
| 1 | 0–2 | MySQL + Python `run_query` |
| 2 | 3–4 | RAG + SQL generation |
| 3 | 5–6 | LangGraph end-to-end |
| 4 | 7 | Streamlit |
| 5 | 8 | Charts + insights |

---

## Professional response example

**Question:** Show monthly sales trend

**SQL:**
```sql
SELECT DATE_FORMAT(order_date, '%Y-%m') AS month,
       SUM(total_amount) AS total_sales
FROM orders
GROUP BY month
ORDER BY month;
```

**Table:** month | total_sales  
**Chart:** line (x=month, y=total_sales)  
**Insights:** 2–3 bullets from actual numbers in the table

---

## Checklist — Phase 0–2 (do first)

```
[ ] Python + VS Code + MySQL + Workbench installed
[ ] Project folder + .venv + pip install -r requirements.txt
[ ] ecommerce database + sample_data.sql run in Workbench
[ ] sqlagent user with SELECT only
[ ] .env with OPENAI_API_KEY + DATABASE_URL
[ ] config.py loads .env
[ ] database/db.py run_query works from terminal
```

When done → **Phase 3 (RAG)**.

---

## Common mistakes

1. Putting whole DB in prompt instead of RAG retrieval  
2. Skipping SQL validation (security risk)  
3. Starting charts before SQL works  
4. LLM inventing chart data instead of plotting `rows`  
5. Forgetting example SQL in vector store  
6. Not using `LIMIT` in generated SQL  

---

## How to get help from the AI assistant

In any new chat, say:

> “I'm building text_sql_queries — follow PROJECT_MASTER_GUIDE.md in my workspace. I'm on Phase X.”

Paste errors or file names. Ask for **one phase at a time** so you still code it yourself.

---

*Last updated: guide for VS Code + MySQL + text-to-SQL + Streamlit dashboard path.*
