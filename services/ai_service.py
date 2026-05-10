import json
import os
from groq import Groq
from dotenv import load_dotenv

load_dotenv()
client = Groq(api_key=os.getenv("GROQ_API_KEY"))

import json
import re

def extract_user_intent(message: str):
    response = client.chat.completions.create(
        model="llama-3.1-8b-instant",
        messages=[
            {
                "role": "system",
                "content": """
                Return ONLY valid JSON in this exact format, no markdown, no explanation:
                {
                    "intent": "string",
                    "filters": {
                        "time_range": "this_month | last_month | all_time",
                        "category": "string or null"
                    }
                }
                """
            },
            {"role": "user", "content": message}
        ]
    )

    raw = response.choices[0].message.content or ""
    
    # Strip markdown code fences if present
    raw = re.sub(r"```(?:json)?\s*|\s*```", "", raw).strip()

    if not raw:
        raise ValueError("LLM returned empty response")

    return json.loads(raw)


def generate_explanation(user_message: str, breakdown: dict):
    response = client.chat.completions.create(
        model="llama-3.1-8b-instant",
        messages=[
            {
                "role": "system",
                "content": "You are a financial assistant. Explain spending insights clearly."
            },
            {
                "role": "user",
                "content": f"""
        User Query: {user_message}
        Category Breakdown: {json.dumps(breakdown)}

        Explain key insights.
        """
                    }
                ]
            )

    return response.choices[0].message.content