🧠 Multi-Tool Medical AI Agent using LangChain & OpenAI API
Query Medical Databases + Perform Web Search with Automatic AI Tool Routing

Built with FastAPI, LangChain, SQLite, GitHub OpenAI Models, and Tavily/SerpAPI.

📌 Overview

This project is a Multi-Tool Medical AI Agent that can:

✔️ Query Heart Disease, Cancer, and Diabetes datasets using SQL
✔️ Perform medical web search (symptoms, treatment, diagnosis, etc.)
✔️ Automatically detect the correct tool based on the question
✔️ Provide answers in natural language
✔️ Expose a clean FastAPI backend for external integration

It is ideal for:

Medical research assistants

Data-driven healthcare analysis

Intelligent chatbot backends

AI-powered medical dashboards

🚀 Features
🔍 1. Intelligent Tool Routing (No Need to Select Tool Manually)

You do not need to pass the tool name.

The agent routes the question automatically:

Type of Question	Tool Used
"How many patients...?"	SQL Database Tool
"Average cholesterol?"	SQL Database Tool
"Symptoms of breast cancer?"	Web Search Tool
"Treatment for diabetes?"	Web Search Tool
🗄 2. SQLite Database Querying (LangChain SQL Agent)

Each dataset is stored as SQLite:

heart_disease.db

cancer.db

diabetes.db

The AI writes SQL automatically and returns human-readable answers.

🌐 3. Medical Web Search (Tavily or SerpAPI)

Used when the query requires external knowledge.

Example:

“What are the symptoms of breast cancer?”

⚙️ 4. Modular Architecture

Your repo has 5 fully separated modules:

File	Description
convert_csv_to_sqlite.py	Converts CSV → SQLite DB
tools.py	Creates SQL database tools
web_search_tool.py	Medical web search (Tavily/SerpAPI)
agent_runner.py	Automatic tool routing logic
app.py	FastAPI backend
📁 Project Structure
