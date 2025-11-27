from serpapi import GoogleSearch
import os
from tavily import TavilyClient
from dotenv import load_dotenv

# Load environment variables from .env
load_dotenv()
# # Replace with your actual SerpAPI key
# os.environ['SERPAPI_API_KEY'] = "give your own"
# SERPAPI_API_KEY = os.getenv("SERPAPI_API_KEY")


TAVILY_API_KEY = os.getenv("web_search_api")  # Replace with your real Tavily API key
tavily_client = TavilyClient(TAVILY_API_KEY)

def search_medical_web(query: str) -> str:
    """
    Fetch medical search results from Tavily API
    """
    if not TAVILY_API_KEY:
        return "Error: TAVILY_API_KEY not set."

    try:
        response = tavily_client.search(query=query)
        results = response.get("results", []) 

        if not results:
            return "No relevant results found."

        # Concatenate top 10 results
        snippets = []
        for item in results[:10]:
            title = item.get("title", "")
            snippet = item.get("snippet", "")
            link = item.get("url", "")
            snippets.append(f"{title}\n{snippet}\n{link}")

        return "\n\n".join(snippets)

    except Exception as e:
        return f"Tavily API Error: {e}"
