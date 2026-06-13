# AI-Powered Text-to-SQL Analytics Assistant

## Overview

AI-powered analytics application that converts natural language questions into SQL queries, executes them on a MySQL database, and automatically generates interactive dashboards and insights.

## Features

- Natural Language to SQL Generation
- RAG-based Schema Retrieval
- LangGraph Workflow Orchestration
- SQL Validation Layer
- MySQL Database Integration
- Interactive Plotly Dashboards
- KPI Metrics Generation
- Automated Business Insights
- Streamlit Web Interface

## Architecture

User Question
→ RAG Schema Retrieval
→ SQL Generation
→ SQL Validation
→ SQL Execution
→ Dashboard Generation
→ Insights

## Tech Stack

- Python
- Streamlit
- LangGraph
- OpenAI API
- MySQL
- Pandas
- Plotly

## Project Structure

```text
graph/
├── state.py
├── nodes.py
└── workflow.py

visualization/
├── dashboard_builder.py
├── chart_builder.py
├── chart_rules.py
└── insights.py

database/
└── db.py

prompts/
└── sql_prompt.py

rag/
└── retriever.py

app.py
```

## Sample Questions

- Show monthly revenue trend
- Which state generates the highest revenue?
- What is the average review score?
- Top 10 product categories by revenue
- How many orders were placed in each customer state?

## How to Run

1. Clone repository

```bash
git clone <repository-url>
```

2. Install dependencies

```bash
pip install -r requirements.txt
```

3. Run application

```bash
streamlit run app.py
```

## Future Improvements

- Multi-agent workflow
- SQL correction agent
- Database-agnostic support
- Export dashboards to PDF
- Conversational analytics