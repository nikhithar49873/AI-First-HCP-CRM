from app.ai.groq_client import llm


def edit_interaction_tool(text):

    prompt = f"""

The user wants to edit this interaction.

Identify what fields should change.

{text}

"""

    response = llm.invoke(prompt)

    return {

        "edit": response.content

    }