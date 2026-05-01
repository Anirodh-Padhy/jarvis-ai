import requests

OLLAMA_URL = "http://localhost:11434/api/generate"
MODEL = "phi3"

def ask_ai(prompt):
    try:
        response = requests.post(
            OLLAMA_URL,
            json={
                "model": MODEL,
                "prompt": f"""
You are Jarvis, a smart AI assistant.
- Be concise
- Be helpful
- Give clear answers
- Avoid long paragraphs

User: {prompt}
Jarvis:
""",
                "stream": False,
                "options": {
                    "temperature": 0.6,
                    "num_predict": 150
                }
            }
        )

        return response.json()["response"]

    except Exception as e:
        print("ERROR:", e)
        return "Sorry, I couldn't process that."