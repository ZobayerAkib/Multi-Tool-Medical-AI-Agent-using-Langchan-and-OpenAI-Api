# 🧠 Multi-Tool Medical AI Agent using LangChain & OpenAI API
Query Medical Databases + Perform Web Search Automatically via AI Routing

Built with **FastAPI**, **LangChain**, **SQLite**, **GitHub OpenAI Models**, and **Tavily/SerpAPI**.

---

## 📌 Overview

This project is a **Multi-Tool Medical AI Agent** that can:

- Query **Heart Disease**, **Cancer**, and **Diabetes** datasets using SQL  
- Perform **medical web search** (symptoms, treatment, diagnosis, etc.)  
- Automatically **detect the correct tool** based on the question  
- Provide answers in **natural language**  
- Expose a clean **FastAPI backend** for external integration  

It is ideal for:  
- Medical research assistants  
- Data-driven healthcare analysis  
- Intelligent chatbot backends  
- AI-powered medical dashboards  

---
## 🎥 Demo Video (Google Drive)
Adjusting the resolution is recommended for the best experience.

[![Watch the video](https://img.youtube.com/vi/VIDEO_ID/0.jpg)](https://drive.google.com/file/d/1G9HuIK_MubR1BuD9o9616kb-bD7sOpE5/view?usp=sharing)

## 🚀 Features

### 🔍 Intelligent Tool Routing
You **do not** need to provide a tool name. The agent automatically selects the correct tool based on your query.

| Type of Question | Tool Used |
|-----------------|-----------|
| "How many patients...?" | SQL Database Tool |
| "Average cholesterol?" | SQL Database Tool |
| "Symptoms of breast cancer?" | Web Search Tool |
| "Treatment for diabetes?" | Web Search Tool |

### 🗄 SQLite Database Querying (LangChain SQL Agent)
Each dataset is stored as SQLite:

- `heart_disease.db`
- `cancer.db`
- `diabetes.db`

The AI writes SQL automatically and returns human-readable answers.

### 🌐 Medical Web Search (Tavily / SerpAPI)
Used when the query requires external knowledge.

Example:  
> “What are the symptoms of breast cancer?”

### ⚙️ Modular Architecture
| File | Description |
|------|-------------|
| `convert_csv_to_sqlite.py` | Converts CSV → SQLite DB |
| `tools.py` | Creates SQL database tools |
| `web_search_tool.py` | Medical web search (Tavily/SerpAPI) |
| `agent_runner.py` | Automatic tool routing logic |
| `app.py` | FastAPI backend |

---

## 📁 Project Structure

```
📁 Multi-Tool-Medical-AI-Agent
│── app.py # FastAPI backend
│── agent_runner.py # AI routing logic
│── tools.py # SQL DB tools using LangChain
│── web_search_tool.py # Tavily / SerpAPI medical search
│── convert_csv_to_sqlite.py # CSV → SQLite converter
│── heart_disease.db
│── cancer.db
│── diabetes.db
│── requirements.txt
└── README.md
```

---

## 🔧 Installation

### 1️⃣ Clone the repository
```bash
git clone https://github.com/ZobayerAkib/Multi-Tool-Medical-AI-Agent-using-Langchan-and-OpenAI-Api.git

cd Multi-Tool-Medical-AI-Agent-using-Langchan-and-OpenAI-Api
```
### 2️⃣ Create virtual environment
```bash
python -m venv venv
venv\Scripts\activate      # Windows
# OR
source venv/bin/activate   # Mac/Linux
```
### 3️⃣ Install dependencies
```bash
pip install -r requirements.txt
```
###🔑 Environment Variables
  -1. GitHub OpenAI Model Token
  ```bash
    export GITHUB_TOKEN="your_github_token"
  ```
  -2. Tavily Search Key (for web search)
  ```bash
    export TAVILY_API_KEY="your_tavily_api_key"
  ```
 - Optional: SerpAPI alternative
  ```bash
    export SERPAPI_API_KEY="your_serpapi_key"
  ```
###▶️ Running the Server

Start FastAPI:

```bash
uvicorn app:app --reload
```
Open API docs:
👉 http://127.0.0.1:8000/docs

### 📡 API Usage
```
Endpoint
POST /ask

Request
{
  "question": "How many heart disease patients are above age 50?",
  "tool": "auto"
}

Response (example)
{
  "tool_used": "HeartDiseaseDBTool",
  "response": "There are nth(number based on your dataset) heart disease patients above age 50."
}  

```

## 🔍 Tools Explanation

### 🗄 Database Tools (`tools.py`)
- **LangChain SQL Agent**  
- **SQLite**  
- **GitHub OpenAI Models**  

**Tools include:**
- `HeartDiseaseDBTool`  
- `CancerDBTool`  
- `DiabetesDBTool`  

### 🌐 Web Search Tool (`web_search_tool.py`)
- Supports **Tavily API** or **SerpAPI**  

### 🧠 Agent Router (`agent_runner.py`)
- Automatically chooses the tool based on query keywords:

```python
db_keywords = [
    "count", "total", "number of", "average",
    "patients", "age", "cholesterol", "bp",
    "compare", "below", "above"
```
### 🔄 Convert CSV → SQLite Database

Place your CSV files in the repo and run:

```bash
python convert_csv_to_sqlite.py

Generates:
heart_disease.db
cancer.db
diabetes.db
```

## 🛠 Tech Stack

| Technology            | Purpose                          |
|-----------------------|----------------------------------|
| FastAPI               | Backend API                      |
| LangChain             | SQL Agent + Tool Routing         |
| OpenAI GitHub Models  | NLP and reasoning                |
| SQLite                | Local medical datasets           |
| Tavily / SerpAPI      | Real-time medical search         |
| Python                | Main programming language        |

## 🤝 Contributing

Pull requests are welcome!  
If you have suggestions or questions, feel free to open an issue.

## ⭐ Support

If you found this project useful, please ⭐ star the repository to support further development.
