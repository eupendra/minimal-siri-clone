import requests
import os
from dotenv import load_dotenv

load_dotenv()
API_KEY = os.getenv("OPENAI_API_KEY")

def get_response(input_text, previous_response_id=None):
    payload = {
        "model": "gpt-4o",
        "input": input_text,
        "instructions": "You are siri. You understnad indian english accent and replies with minimal words.",
    }
    if previous_response_id:
        payload["previous_response_id"] = previous_response_id
    response = requests.post(
        "https://api.openai.com/v1/responses",
        headers={"Authorization": f"Bearer {API_KEY}", "Content-Type": "application/json"},
        json=payload,
    )
    result = response.json()
    response_text = result.get("output_text", result["output"][0]["content"][0]["text"])
    response_id = result.get("id")
    print(response_text)
    return response_text, response_id


if __name__ == "__main__":
    get_response("whats the first step of building a voice chatbot?")