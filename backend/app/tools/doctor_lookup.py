from app.ai.groq_client import llm


def doctor_lookup_tool(name):

    prompt = f"""

Tell me basic information about

{name}

Keep answer within 40 words.

"""

    response = llm.invoke(prompt)

    return {

        "doctor": response.content

    }