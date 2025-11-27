from tools import HeartDiseaseDBTool, CancerDBTool, DiabetesDBTool
from web_search_tool import search_medical_web
from langchain_openai import ChatOpenAI
from langchain_openai import OpenAI, ChatOpenAI
import os
from langchain_core.tools import Tool 
import warnings
warnings.filterwarnings("ignore")
from dotenv import load_dotenv

# Load environment variables from .env
load_dotenv()
# Initialize LLM for routing
os.environ['GITHUB_TOKEN'] = os.getenv("API_KEY")   # Replace with your actual GitHub token
token = os.environ.get("GITHUB_TOKEN")
endpoint = os.getenv("BASE_URL") 
model_name = os.getenv("MODEL_NAME") 

if not token:
    raise ValueError("GITHUB_TOKEN environment variable not set. Please provide a valid token.")

router_llm =ChatOpenAI(
    model_name=model_name,
    openai_api_key=token,
    openai_api_base=endpoint,
    temperature=0.5,
)

# --- Keywords to detect DB questions ---
DB_KEYWORDS = [
    "count", "number of", "total", "average", "above", "below",
    "patients", "how many", "percentage", "rate", "incidence", "prevalence"
]

# --- Mapping tools ---
TOOLS_MAP = {
    "HeartDiseaseDBTool": HeartDiseaseDBTool,
    "CancerDBTool": CancerDBTool,
    "DiabetesDBTool": DiabetesDBTool,
    "MedicalWebSearchTool": search_medical_web
}

# --- Simple router ---
def route_question(question: str):
    q_lower = question.lower()
    for keyword in DB_KEYWORDS:
        if keyword in q_lower:
            # Choose DB tool based on keyword match
            if "heart" in q_lower or "cardio" in q_lower:
                return "HeartDiseaseDBTool"
            elif "cancer" in q_lower or "tumor" in q_lower:
                return "CancerDBTool"
            elif "diabetes" in q_lower or "sugar" in q_lower:
                return "DiabetesDBTool"
            else:
                # Default DB if keyword matches but no specific disease
                return "HeartDiseaseDBTool"
    # If no DB keyword, use Web search
    return "MedicalWebSearchTool"

# --- Ask question ---
def ask_question(question: str):
    tool_name = route_question(question)
    tool_func = TOOLS_MAP[tool_name]

    # Call the tool
    try:
        # Tools may be LangChain Tool objects or simple functions
        if isinstance(tool_func, Tool):
            response = tool_func.func(question)
        else:
            response = tool_func(question)
    except Exception as e:
        response = f"Error executing tool {tool_name}: {e}"

    return {
        "tool_used": tool_name,
        "response": response
    }

# --- CLI interface ---
def main():
    print("=== Multi-Tool Medical AI Agent ===")
    print("Type 'exit' to quit.\n")

    while True:
        question = input("Ask a question: ")
        if question.lower() in ["exit", "quit"]:
            break

        result = ask_question(question)
        print(f"\n=== Tool used: {result['tool_used']} ===")
        print(f"Response:\n{result['response']}")
        print("================\n")


if __name__ == "__main__":
    main()