import sqlite3
import os
from langchain_core.prompts import ChatPromptTemplate
from langchain_core.output_parsers import StrOutputParser
from langchain_core.runnables import RunnablePassthrough
from langchain_openai import OpenAI, ChatOpenAI
from langchain_core.tools import Tool
from langchain_community.utilities.sql_database import SQLDatabase
from langchain_community.agent_toolkits import create_sql_agent
from dotenv import load_dotenv

# Load environment variables from .env
load_dotenv()

# Initialize LLM

os.environ['GITHUB_TOKEN'] = os.getenv("API_KEY")   # Replace with your actual GitHub token
token = os.environ.get("GITHUB_TOKEN")
endpoint = os.getenv("BASE_URL") 
model_name = os.getenv("MODEL_NAME") 

if not token:
    raise ValueError("GITHUB_TOKEN environment variable not set. Please provide a valid token.")

llm =ChatOpenAI(
    model_name=model_name,
    openai_api_key=token,
    openai_api_base=endpoint,
    temperature=0.5,
)


# --- Function to make a SQL-based DB tool ---
def make_db_tool(db_path: str, tool_name: str, description: str) -> Tool:
    """
    Creates a LangChain SQL agent as a tool for a given SQLite database.
    """
    # Connect to SQLite database
    db = SQLDatabase.from_uri(f"sqlite:///{db_path}")

    # Create a SQL agent
    agent_executor = create_sql_agent(
        llm=llm,
        db=db,
        verbose=False
    )

    # Define run function
    def run(query: str) -> str:
        try:
            return agent_executor.run(query)
        except Exception as e:
            return f"Error: {e}"

    # Return as a Tool object
    return Tool(
        name=tool_name,
        func=run,
        description=description
    )

# --- Create DB tools dynamically ---
HeartDiseaseDBTool = make_db_tool(
    "heart_disease.db",
    "HeartDiseaseDBTool",
    "Answer questions using Heart Disease dataset via SQL."
)

CancerDBTool = make_db_tool(
    "cancer.db",
    "CancerDBTool",
    "Answer questions using Cancer dataset via SQL."
)

DiabetesDBTool = make_db_tool(
    "diabetes.db",
    "DiabetesDBTool",
    "Answer questions using Diabetes dataset via SQL."
)
