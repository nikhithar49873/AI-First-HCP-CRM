from app.ai.groq_client import llm


def summary_tool(text):

    prompt = f"""

Summarize this meeting in less than 80 words.

{text}

"""

    response = llm.invoke(prompt)

    return {

        "summary": response.content

    }