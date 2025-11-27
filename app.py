from fastapi import FastAPI
from pydantic import BaseModel
from tools import HeartDiseaseDBTool, CancerDBTool, DiabetesDBTool
from web_search_tool import search_medical_web

app = FastAPI(title="Multi-Tool Medical AI Agent")

# -------------------------------
# Tools mapping
# -------------------------------
tools_map = {
    "HeartDiseaseDBTool": HeartDiseaseDBTool,
    "CancerDBTool": CancerDBTool,
    "DiabetesDBTool": DiabetesDBTool,
    "MedicalWebSearchTool": search_medical_web
}

# Keywords for DB routing
db_keywords = [
    "count", "number of", "total", "average", "above", "below",
    "patients", "how many", "diagnosed", "male", "female", "age",
    "glucose", "cholesterol", "tumor", "size", "blood pressure"
]

class QuestionRequest(BaseModel):
    question: str

def route_tool(question: str) -> str:
    """
    Choose the appropriate tool based on question keywords.
    """
    q_lower = question.lower()
    for kw in db_keywords:
        if kw in q_lower:
            # Decide which DB based on dataset-specific keywords
            if "heart" in q_lower or "cholesterol" in q_lower or "blood pressure" in q_lower:
                return "HeartDiseaseDBTool"
            elif "cancer" in q_lower or "tumor" in q_lower:
                return "CancerDBTool"
            elif "diabetes" in q_lower or "glucose" in q_lower:
                return "DiabetesDBTool"
            else:
                # default to HeartDisease if generic number/statistics
                return "HeartDiseaseDBTool"
    # If no DB keyword, use web search
    return "MedicalWebSearchTool"

@app.post("/ask")
def ask_question(req: QuestionRequest):
    tool_name = route_tool(req.question)
    tool = tools_map[tool_name]

    # Call DB tool or web search tool
    if hasattr(tool, "func"):  # DB tools are Tool objects
        response = tool.func(req.question)
    else:  # web search tool is a plain function
        response = tool(req.question)

    return {"tool_used": tool_name, "response": response}
