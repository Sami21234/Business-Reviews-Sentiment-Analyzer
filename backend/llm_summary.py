import requests

def generate_llm_summary(text):
    response = requests.post(
        "http://localhost:11434/api/generate",
        json={
            "model": "mistral",
            "prompt": f"""
You are a business analyst.

Summarize the following customer reviews into:
1. Key issues
2. Overall sentiment
3. Actionable suggestions

Reviews:
{text}
""",
            "stream": False
        }
    )

    return response.json()["response"]