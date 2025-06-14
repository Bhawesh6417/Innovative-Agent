import requests
import os

def get_groq_llm_response(prompt, temp=0.7, max_tokens=512):
    url = "https://api.groq.com/openai/v1/chat/completions"
    headers = {
        "Authorization": f"Bearer {os.getenv('GROQ_API_KEY')}",
        "Content-Type": "application/json"
    }

    body = {
        "model": "llama3-8b-8192",  # ✅ Use a known working model name
        "messages": [
            {"role": "system", "content": "You are a helpful AI assistant for innovation guidance."},
            {"role": "user", "content": prompt}
        ],
        "temperature": temp,
        "max_tokens": max_tokens
    }

    try:
        response = requests.post(url, headers=headers, json=body)
        response.raise_for_status()
        data = response.json()

        if "choices" not in data:
            print("ERROR: Unexpected Groq response format:", data)
            return "Sorry, I couldn't generate a response. Please try again."

        return data["choices"][0]["message"]["content"]

    except requests.exceptions.HTTPError as http_err:
        print("HTTP Error:", response.status_code, response.text)
        return "Sorry, the language model could not process your request (HTTP Error)."
    except Exception as e:
        print("EXCEPTION during Groq API call:", e)
        return "Sorry, I encountered an error while contacting the LLM."
