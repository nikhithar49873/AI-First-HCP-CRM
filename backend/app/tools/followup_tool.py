from app.ai.groq_client import llm


def followup_tool(text):

    prompt = f"""

When should the sales representative follow up?

{text}

"""

    response = llm.invoke(prompt)

    return {

        "followup": response.content

    }