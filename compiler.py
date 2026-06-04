import google.generativeai as genai
from dotenv import load_dotenv
import os
import json

load_dotenv()

genai.configure(
    api_key=os.getenv("GEMINI_API_KEY")
)

model = genai.GenerativeModel(
    "gemini-2.5-flash"
)

def compile_application(user_prompt):

    prompt = f"""
You are an AI Application Compiler.

Convert the user request into a complete application specification.

Return ONLY valid JSON.

Structure:

{{
  "intent": {{
      "entities": [],
      "features": [],
      "roles": []
  }},
  "architecture": {{
      "modules": [],
      "flows": []
  }},
  "database": {{
      "tables": []
  }},
  "api": {{
      "endpoints": []
  }},
  "ui": {{
      "pages": []
  }},
  "auth": {{
      "roles": {{}}
  }}
}}

User Request:

{user_prompt}
"""

    response = model.generate_content(prompt)

    text = response.text
    text = text.replace("```json", "")
    text = text.replace("```", "")
    text = text.strip()

    try:
        return json.loads(text)

    except Exception:

        return {
            "error": "Invalid JSON returned",
            "raw_output": text
        }