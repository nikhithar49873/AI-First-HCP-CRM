from app.ai.groq_client import llm
import json


def log_interaction_tool(text):

    prompt = f"""
Extract the following information from this meeting.

Return ONLY JSON.

Fields:

doctor_name

hospital

specialization

interaction_type

discussion

products

follow_up_date

notes

Today's meeting:

{text}
"""

    response = llm.invoke(prompt)

    try:
        data = json.loads(response.content)

        return {
            "tool": "Log Interaction",
            "status": "success",
            "data": data
        }

    except Exception:

        return {
            "tool": "Log Interaction",
            "status": "failed",
            "response": response.content
        }